# Google Ads MCP Server Core (Version)

Questo repository contiene il server MCP per integrare Google Ads con agenti AI come Antigravity o Claude.

## 🚀 Setup Rapido per Windows
Se usi Antigravity e sei su Windows, abbiamo incluso un workflow automatico:
1. Scarica e apri questa cartella.
2. Digita `/setup-mcp-windows` nella chat del tuo agente.

---

## 🔐 Configurazione Credenziali (Fondamentale)
Per motivi di sicurezza, questo repository **NON** include le credenziali di accesso. Dovrai generare le tue seguendo questi passaggi:

### 1. Ottieni le API Keys (Google Cloud Console)
1.  Crea un progetto su [Google Cloud Console](https://console.cloud.google.com/).
2.  Abilita le **Google Ads API** dalla libreria API.
3.  Configura la **Schermata di consenso OAuth**:
    *   Scegli "External" (se non hai un'organizzazione Google Workspace).
    *   Aggiungi il tuo indirizzo email come "Test user" (fondamentale per poter generare il token).
4.  Crea le **Credenziali**:
    *   Clicca su "Crea credenziali" -> "ID client OAuth".
    *   Tipo di applicazione: **Applicazione desktop**.
    *   Scarica il file JSON e rinominalo in `client_secrets.json` nella radice del progetto.
5.  **Developer Token**: Recati nel tuo account Google Ads Manager (MCC) -> Strumenti e impostazioni -> Centro API e copia il tuo Developer Token.

### 2. Genera il Refresh Token
Questo è il passaggio che autorizza l'agente ad agire per tuo conto.
1.  Assicurati di avere `uv` installato.
2.  Esegui lo script:
    ```bash
    uv run get_refresh_token.py
    ```
3.  Lo script aprirà il browser. Accedi con l'account Google che ha accesso a Google Ads.
4.  Copia il codice di autorizzazione restituito dal browser e incollalo nel terminale.
5.  Lo script ti mostrerà il tuo `refresh_token`. Copialo.

### 3. Configura `google-ads.yaml`
Rinomina `google-ads.yaml.example` in `google-ads.yaml` e compila i campi:
- `developer_token`: Quello ottenuto dal centro API.
- `client_id`: Dal file `client_secrets.json`.
- `client_secret`: Dal file `client_secrets.json`.
- `refresh_token`: Quello appena generato.
- `login_customer_id`: L'ID dell'account manager (MCC) senza trattini.
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
