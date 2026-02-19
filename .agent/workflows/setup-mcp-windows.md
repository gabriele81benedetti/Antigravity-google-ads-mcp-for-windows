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

3. **SE IL FILE NON ESISTE**, l'agente DEVE eseguire i seguenti passaggi fornendo le istruzioni esatte:
   
   - **Step 3.1: Developer Token**
     *   *Istruzione per l'utente*: "Vai sul tuo account Google Ads Manager (MCC) -> Strumenti e Impostazioni -> Configurazione -> Centro API. Lì troverai il Developer Token (una stringa di caratteri). Copialo e incollalo qui."
   
   - **Step 3.2: Client ID & Client Secret**
     *   *Istruzione per l'utente*: "Vai su [Google Cloud Console](https://console.cloud.google.com/), seleziona il tuo progetto, vai in 'API e Servizi' -> 'Credenziali'. Cerca l'ID client OAuth 2.0 che hai creato (tipo 'Desktop App'). Clicca sull'icona della matita o scarica il JSON per vedere il 'Client ID' e il 'Client Secret'. Incollali qui."
   
   - **Step 3.3: Script Refresh Token (Interattivo)**
     *   *Azione*: L'agente informa l'utente: "Adesso lancerò lo script. **Si aprirà una finestra del browser**. Dovrai accedere con l'account Google Ads, cliccare su 'Continua' e poi su 'Consenti'. Una volta fatto, torna qui."
     *   *Comando*: `uv run get_refresh_token.py -c client_secrets.json`
     *   *Nota*: L'agente deve mostrare il link all'utente se il browser non si apre automaticamente e attendere che lo script stampi "SUCCESS!".
   
   - **Step 3.4: Recupero Refresh Token**
     *   *Azione*: L'agente legge l'output dello script precedente e cattura automaticamente il valore dopo "YOUR REFRESH TOKEN IS:".
   
   - **Step 3.5: Login Customer ID**
     *   *Istruzione per l'utente*: "Inserisci l'ID del tuo account Manager (MCC) a 10 cifre senza trattini (es. 1215695365). Se non lo hai, scrivi 'none'."

   - **Step 3.6: CREAZIONE FILE**
     *   *Azione*: L'agente genera il file `google-ads.yaml` usando i dati raccolti.

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
