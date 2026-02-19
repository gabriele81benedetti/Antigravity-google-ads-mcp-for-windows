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

3. **SE IL FILE NON ESISTE**, l'agente deve attivare la **Guida Passo-Passo alle Credenziali**:
   
   *   **Passaggio A (Google Cloud)**: Chiedi all'utente di andare su [Google Cloud Console](https://console.cloud.google.com/), creare un progetto e abilitare la **Google Ads API**.
   *   **Passaggio B (OAuth)**: Spiega come configurare la schermata di consenso (User Type: External) e aggiungere la propria email come **Test User** (fondamentale!).
   *   **Passaggio C (Client Secrets)**: Spiega come creare le credenziali "OAuth Client ID" (Desktop App), scaricare il JSON e rinominarlo in `client_secrets.json` nella cartella attuale.
   *   **Passaggio D (Developer Token)**: Spiega dove trovarlo nell'account Google Ads (Strumenti -> Centro API).
   *   **Passaggio E (Refresh Token)**: Una volta caricato `client_secrets.json`, l'agente deve proporre di eseguire lo script:
     `uv run get_refresh_token.py`
   *   **Passaggio F (Creazione YAML)**: L'agente raccoglie i dati (Developer Token, Client ID, Secret, Refresh Token) e si offre di creare il file `google-ads.yaml` per l'utente.

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
