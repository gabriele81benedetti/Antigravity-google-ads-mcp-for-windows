la guida in italiano e dopo la guida in inglese

# English Version

# Google Ads MCP Server Core (Windows & Public version)

This repository contains the MCP server to integrate Google Ads with AI agents such as Antigravity or Claude.

## 🚀 Quick Setup for Windows
If you are using Antigravity on Windows, we have included an automatic workflow:
1. Download and open this folder.
2. Type `/setup-mcp-windows` in your agent's chat.

---

### 4. Configure Antigravity (The final step)
Copy this block into your `mcp_config.json` file (located at `%USERPROFILE%\.gemini\antigravity\mcp_config.json`). 
**Remember to replace the path `C:/Path/To/Folder/` with the actual path on your PC.**

```json
{
  "mcpServers": {
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
  }
}
```
*Tip: Use forward slashes `/` in the JSON file.*

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
Run in your terminal:
```bash
uv run get_refresh_token.py
```
Follow the on-screen instructions to authenticate and obtain your `refresh_token`.

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

## 🚀 Setup Rapido per Windows
Se usi Antigravity e sei su Windows, abbiamo incluso un workflow automatico:
1. Scarica e apri questa cartella.
2. Digita `/setup-mcp-windows` nella chat del tuo agente.

---

### 4. Configura Antigravity (Il pezzo finale)
Copia questo blocco nel tuo file `mcp_config.json` (che si trova in `%USERPROFILE%\.gemini\antigravity\mcp_config.json`). 
**Ricorda di cambiare il percorso `C:/Percorso/Alla/Cartella/` con quello reale sul tuo PC.**

```json
{
  "mcpServers": {
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
  }
}
```
*Tip: Usa le slash in avanti `/` nel file JSON.*

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
Esegui nel terminale:
```bash
uv run get_refresh_token.py
```
Segui le istruzioni a video per ottenere il `refresh_token`.

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
