#!/usr/bin/env python
import argparse
import hashlib
import os
import re
import socket
import sys
from urllib.parse import unquote
from google_auth_oauthlib.flow import Flow

_SCOPES = [
    "https://www.googleapis.com/auth/adwords",
    "https://www.googleapis.com/auth/analytics.readonly",
    "https://www.googleapis.com/auth/script.external_request",
    "https://www.googleapis.com/auth/analytics",
    "https://www.googleapis.com/auth/webmasters.readonly",
]
_SERVER = "127.0.0.1"
_PORT = 8080
_REDIRECT_URI = f"http://{_SERVER}:{_PORT}"

def main(client_secrets_path):
    print(f"Using client secrets from: {client_secrets_path}")
    flow = Flow.from_client_secrets_file(client_secrets_path, scopes=_SCOPES)
    flow.redirect_uri = _REDIRECT_URI

    passthrough_val = hashlib.sha256(os.urandom(1024)).hexdigest()

    authorization_url, state = flow.authorization_url(
        access_type="offline",
        state=passthrough_val,
        prompt="consent",
        include_granted_scopes="true",
    )

    print("\n" + "="*60)
    print("PASTE THIS URL INTO YOUR BROWSER:")
    print(authorization_url)
    print("="*60 + "\n")
    print(f"Waiting for authorization callback at {_REDIRECT_URI}...")

    params = get_authorization_code(passthrough_val)
    code = unquote(params.get("code"))
    returned_scopes = unquote(params.get("scope"))

    flow.scope = returned_scopes.split(" ")
    flow.fetch_token(code=code)
    refresh_token = flow.credentials.refresh_token

    print("\n" + "!"*60)
    print(f"SUCCESS! YOUR REFRESH TOKEN IS:")
    print(refresh_token)
    print("!"*60 + "\n")

def get_authorization_code(passthrough_val):
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((_SERVER, _PORT))
    sock.listen(1)
    connection, address = sock.accept()
    data = connection.recv(1024)
    params = parse_raw_query_params(data)

    try:
        if not params.get("code"):
            error = params.get("error")
            message = f"Failed to retrieve authorization code. Error: {error}"
            raise ValueError(message)
        elif params.get("state") != passthrough_val:
            message = "State token does not match the expected state."
            raise ValueError(message)
        else:
            message = "Authorization code was successfully retrieved."
    except ValueError as error:
        print(error)
        sys.exit(1)
    finally:
        response = (
            "HTTP/1.1 200 OK\n"
            "Content-Type: text/html\n\n"
            f"<html><body><b>{message}</b><p>You can close this tab and return to the terminal.</p></body></html>"
        )
        connection.sendall(response.encode())
        connection.close()
        sock.close()

    return params

def parse_raw_query_params(data):
    decoded = data.decode("utf-8")
    match = re.search(r"GET\s\/\?(.*)\s", decoded)
    if not match:
        return {}
    params_str = match.group(1)
    pairs = [pair.split("=") for pair in params_str.split("&") if "=" in pair]
    return {key: val for key, val in pairs}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--client_secrets_path", default="client_secrets.json")
    args = parser.parse_args()
    
    if not os.path.exists(args.client_secrets_path):
        print(f"ERROR: File {args.client_secrets_path} NOT FOUND.")
        print("Please download your client_secrets.json from Google Cloud Console first.")
        sys.exit(1)
        
    main(args.client_secrets_path)
