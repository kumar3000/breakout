# breakout

Small Gemini test script.

## Setup (PowerShell)

```powershell
py -m pip install -r .\requirements.txt

# Option A: keep using this repo's env file
Copy-Item .\env.example .\GEMINI_API_KEY.env
notepad .\GEMINI_API_KEY.env

# Option B: use a standard .env file (recommended)
# (create it manually; dotfiles may be hidden in Explorer)
# GEMINI_API_KEY=your_key_here
# (no quotes, no spaces around '=')
```

## Run

```powershell
py .\main.py
```

## Security note

If you previously committed a real API key, rotate it in Google AI Studio / Google Cloud immediately.
