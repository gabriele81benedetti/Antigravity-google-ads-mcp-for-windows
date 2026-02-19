la guida in italiano si trova dopo la guida in inglese

# English Version

# Google Ads MCP Server Core (Windows & Public version)

This repository contains the MCP server to integrate Google Ads with AI agents such as Antigravity or Claude.
Don't worry if you're a beginner: once you open this folder in Antigravity, you'll be guided step-by-step through an interactive setup process.

## 🚀 Quick Setup for Windows
If you are using Antigravity on Windows, we have included an automatic workflow:
1. [Download](https://github.com/gabriele81benedetti/Antigravity-google-ads-mcp-for-windows/archive/refs/heads/main.zip) the ZIP file.
2. **Extract the ZIP file** into a folder of your choice on your PC (e.g., `C:\Projects\google_ads_mcp`).
3. Open that specific folder in Antigravity.
4. **Type `/setup-mcp-windows` in the AI Chat window** (NOT in the system terminal/PowerShell).

### 🆘 Troubleshooting the `/setup` command
If your agent says the command does not exist:
*   **Check Hidden Folders**: Ensure the `.agent` folder exists in your directory. On Windows, folders starting with a dot might be hidden.
*   **Folder Level**: Make sure you opened the folder that *contains* the `ads_mcp` and `.agent` folders, not a parent folder.
*   **Reserved Names**: Do not place this project inside a folder named `.antigravity`. Use a neutral path like `C:\Projects\google_ads`.

> [!WARNING]
> Do not type this command in the terminal. It must be typed in the Antigravity chat interaction box.

---

### 4. Configure Antigravity (Add, don't overwrite!)
Open your `mcp_config.json` file (located at `%USERPROFILE%\.gemini\antigravity\mcp_config.json`).
**Add** the following `GoogleAds` block inside the `mcpServers` object. Do not delete your existing servers (like Meta Ads or others).

```json
/* inside mcpServers: { ... } */
"GoogleAds": {
  "command": "uv",
  "args": [
    "run",
    "--directory",
    "C:/Path/To/Folder/Antigravity-google-ads-mcp-for-windows",
    "-m",
    "ads_mcp.server"
  ],
  "cwd": "C:/Path/To/Folder/Antigravity-google-ads-mcp-for-windows",
  "timeout": 30000
}
```
*Tip: Ensure you put a comma `,` between different server objects and use forward slashes `/`.*

---

## 🔐 Credentials Configuration (Essential)
For security reasons, this repository **DOES NOT** include access credentials. You must generate your own by following these steps:

### 1. Get API Keys (Google Cloud Console)
1.  Create a project on [Google Cloud Console](https://console.cloud.google.com/).
2.  Enable the **Google Ads API** from the API library.
3.  Configure the **OAuth Consent Screen**:
    *   Choose "External".
    *   Add your email address as a **Test user** (mandatory to generate the token).
4.  Create **Credentials**:
    *   Click on "Create Credentials" -> "OAuth Client ID".
    *   Application type: **Desktop App**.
    *   Download the JSON file and rename it to `client_secrets.json` in the project root.
5.  **Developer Token**: Copy it from your Google Ads Manager (MCC) account -> Tools & Settings -> API Center.

### 2. Generate the Refresh Token
Antigravity can do this for you!
1. Make sure `client_secrets.json` is in the folder.
2. In the AI chat, ask/wait for the step: `uv run get_refresh_token.py -c client_secrets.json`.
3. A URL will be printed. Click it, log in to your Google account, and click "Allow".
4. The script will automatically capture the token and print it in the chat.

### 3. Create the `google-ads.yaml` file
Rename `google-ads.yaml.example` to `google-ads.yaml` and fill in the fields:
```yaml
developer_token: "YOUR_TOKEN"
client_id: "YOUR_CLIENT_ID"
client_secret: "YOUR_CLIENT_SECRET"
refresh_token: "YOUR_REFRESH_TOKEN"
login_customer_id: "YOUR_MCC_ID" # Optional
use_proto_plus: True
```

---

## 🛠️ Requirements
- [uv](https://astral.sh/uv/) installed on the system.
- Python 3.10 or higher.

---
---

# Versione Italiana

# Google Ads MCP Server Core (Version)

Questo repository contiene il server MCP per integrare Google Ads con agenti AI come Antigravity o Claude.
Non preoccuparti se sei alle prime armi: una volta aperta questa cartella in Antigravity, verrai guidato passo dopo passo da una procedura interattiva.

## 🚀 Setup Rapido per Windows
Se usi Antigravity e sei su Windows, abbiamo incluso un workflow automatico:
1. [Scarica](https://github.com/gabriele81benedetti/Antigravity-google-ads-mcp-for-windows/archive/refs/heads/main.zip) il file ZIP.
2. **Estrai il file ZIP** in una cartella a tua scelta sul tuo PC (es. `C:\Progetti\google_ads_mcp`).
3. Apri quella specifica cartella in Antigravity.
4. **Digita `/setup-mcp-windows` nella finestra della Chat AI** (NON nel terminale di sistema/PowerShell).

### 🆘 Risoluzione problemi comando `/setup`
Se l'agente dice che il comando non esiste:
*   **Cartelle Nascoste**: Assicurati che la cartella `.agent` esista. Su Windows, i file che iniziano con un punto potrebbero essere nascosti.
*   **Livello Cartella**: Assicurati di aver aperto la cartella che *contiene* direttamente `ads_mcp` e `.agent`, non una cartella superiore.
*   **Nomi Riservati**: Non posizionare il progetto dentro una cartella chiamata `.antigravity`. Usa un percorso neutro come `C:\Progetti\google_ads`.

> [!IMPORTANT]
> Non scrivere questo comando nel terminale. Deve essere digitato nel box di chat con Antigravity.

---

### 4. Configura Antigravity (Aggiungi, non sovrascrivere!)
Apri il tuo file `mcp_config.json` (che si trova in `%USERPROFILE%\.gemini\antigravity\mcp_config.json`).
**Aggiungi** il seguente blocco `GoogleAds` dentro l'oggetto `mcpServers`. Non cancellare i server esistenti (come Meta Ads o altri).

```json
/* dentro mcpServers: { ... } */
"GoogleAds": {
  "command": "uv",
  "args": [
    "run",
    "--directory",
    "C:/Percorso/Alla/Cartella/Antigravity-google-ads-mcp-for-windows",
    "-m",
    "ads_mcp.server"
  ],
  "cwd": "C:/Percorso/Alla/Cartella/Antigravity-google-ads-mcp-for-windows",
  "timeout": 30000
}
```
*Tip: Assicurati di mettere una virgola `,` tra i diversi server e usa le slash in avanti `/`.*

---

## 🔐 Configurazione Credenziali (Fondamentale)
Per motivi di sicurezza, questo repository **NON** include le credenziali di accesso. Dovrai generare le tue seguendo questi passaggi:

### 1. Ottieni le API Keys (Google Cloud Console)
1.  Crea un progetto su [Google Cloud Console](https://console.cloud.google.com/).
2.  Abilita le **Google Ads API** dalla libreria API.
3.  Configura la **Schermata di consenso OAuth**:
    *   Scegli "External".
    *   Aggiungi il tuo indirizzo email come "Test user".
4.  Crea le **Credenziali**:
    *   Clicca su "Crea credenziali" -> "ID client OAuth".
    *   Tipo di applicazione: **Applicazione desktop**.
    *   Scarica il file JSON e rinominalo in `client_secrets.json` nella radice del progetto.
5.  **Developer Token**: Copialo dal tuo account Google Ads Manager (MCC) -> Strumenti -> Centro API.

### 2. Genera il Refresh Token
Antigravity può farlo per te!
1. Assicurati che `client_secrets.json` sia nella cartella.
2. Nella chat AI, chiedi o aspetta lo step: `uv run get_refresh_token.py -c client_secrets.json`.
3. Verrà stampato un URL. Cliccaci, accedi al tuo account Google e clicca su "Consenti".
4. Lo script catturerà automaticamente il token e lo stamperà nella chat.

### 3. Crea il file `google-ads.yaml`
Rinomina `google-ads.yaml.example` in `google-ads.yaml` e riempi i campi:
```yaml
developer_token: "IL_TUO_TOKEN"
client_id: "IL_TUO_CLIENT_ID"
client_secret: "IL_TUO_CLIENT_SECRET"
refresh_token: "IL_TUO_REFRESH_TOKEN"
login_customer_id: "IL_TUO_MCC_ID" # Facoltativo
use_proto_plus: True
```

---

## 🛠️ Requisiti
- [uv](https://astral.sh/uv/) installato sul sistema.
- Python 3.10 o superiore.
