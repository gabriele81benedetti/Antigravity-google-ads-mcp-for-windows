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
