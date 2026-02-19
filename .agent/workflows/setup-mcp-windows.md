---
description: Configurazione automatizzata del server MCP Google Ads su sistemi Windows.
---

Questo workflow guiderà l'utente nella configurazione del server MCP su Windows.

### Fase 1: Verifica Ambiente e Guida alle Credenziali
L'agente verifica se si trova su Windows e aiuta l'utente a configurare le API di Google.

// turbo
1. Verifica sistema operativo:
   `powershell -Command "Write-Output 'Sistema:'; $PSVersionTable"`

2. Verifica presenza file credenziali:
   `powershell -Command "Test-Path google-ads.yaml"`

3. **SE IL FILE NON ESISTE**, l'agente DEVE eseguire i seguenti passaggi in ordine:
   
   - **Step 3.1**: Chiedi all'utente di fornire il **Developer Token** (si trova nel Centro API di Google Ads).
   - **Step 3.2**: Chiedi all'utente di fornire il **Client ID** e il **Client Secret** (si trovano nel file `client_secrets.json` scaricato dalla Cloud Console).
   - **Step 3.3**: Esegui lo script per ottenere il Refresh Token: `uv run get_refresh_token.py`.
   - **Step 3.4**: Chiedi all'utente il **Refresh Token** generato dallo script sopra.
   - **Step 3.5**: Chiedi all'utente il **Login Customer ID** (l'ID dell'account MCC, opzionale).
   - **Step 3.6**: **CREAZIONE FILE**: L'agente deve usare lo strumento `write_to_file` per creare il file `google-ads.yaml` nella cartella corrente con questa struttura:

   ```yaml
   developer_token: "VALORE_RICEVUTO"
   client_id: "VALORE_RICEVUTO"
   client_secret: "VALORE_RICEVUTO"
   refresh_token: "VALORE_RICEVUTO"
   login_customer_id: "VALORE_RICEVUTO"
   use_proto_plus: True
   ```

### Fase 2: Pulizia ed Installazione
Se `uv` non è installato, l'agente deve proporre l'installazione. Deve anche rimuovere residui di macOS.

2. Se `uv` non è presente, installalo:
   `powershell -c "irm https://astral.sh/uv/install.ps1 | iex"`

3. Rimuovi la cartella `.venv` se esiste (residuo Mac):
   `powershell -Command "if (Test-Path .venv) { Remove-Item -Recurse -Force .venv }"`

### Fase 3: Generazione Configurazione
L'agente deve trovare il percorso assoluto della cartella attuale e generare il blocco JSON.

// turbo
4. Ottieni il percorso assoluto della cartella:
   `powershell -Command "(Get-Item .).FullName"`

### Fase 4: Scrittura File di Configurazione (NON SOVRASCRIVERE!)
L'agente deve aggiungere il server Google Ads alla configurazione esistente di Antigravity senza cancellare gli altri server (es. Meta Ads).

// turbo
5. Leggi il file di configurazione esistente se presente:
   `powershell -Command "if (Test-Path $HOME\.gemini\antigravity\mcp_config.json) { Get-Content $HOME\.gemini\antigravity\mcp_config.json } else { Write-Output 'File non trovato' }"`

6. **OPERAZIONE DI MERGE**: 
   *   Se il file esiste, l'agente deve **aggiungere** l'oggetto `GoogleAds` all'interno dell'oggetto `mcpServers` già presente.
   *   Se il file non esiste, crealo da zero.
   *   **Mostra il risultato finale all'utente** e chiedi conferma prima di salvare, assicurandoti che i server precedenti siano ancora presenti nel testo.

### Fase 5: Test Finale
7. Chiedi all'utente di riavviare l'agente e provare il comando: `Riesci a vedere l'mcp GoogleAds?`
