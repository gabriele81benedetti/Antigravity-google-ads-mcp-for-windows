---
description: Configurazione automatizzata del server MCP Google Ads su sistemi Windows.
---

Questo workflow guiderà l'utente nella configurazione del server MCP su Windows.

### Fase 1: Verifica Ambiente e Credenziali
L'agente verifica se si trova su Windows e se i file di configurazione necessari sono presenti.

// turbo
1. Verifica sistema operativo e presenza file credenziali:
   `powershell -Command "Write-Output 'Sistema:'; $PSVersionTable; Write-Output '---'; Write-Output 'Verifica credenziali:'; Test-Path google-ads.yaml"`

*Nota: Se 'Test-Path google-ads.yaml' restituisce False, l'agente deve istruire l'utente a configurare le sue credenziali seguendo il README.*

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

### Fase 4: Scrittura File di Configurazione
L'agente deve guidare l'utente a scrivere il file `mcp_config.json` nella cartella corretta di Antigravity su Windows.

5. Identifica il percorso di configurazione di Antigravity:
   Solitamente è `$HOME\.gemini\antigravity\mcp_config.json`.

6. Mostra all'utente il contenuto finale del file JSON, formattato con i percorsi corretti appena rilevati, e chiedi conferma per procedere o istruisci su come incollarlo manualmente.

### Fase 5: Test Finale
7. Chiedi all'utente di riavviare l'agente e provare il comando: `Riesci a vedere l'mcp GoogleAds?`
