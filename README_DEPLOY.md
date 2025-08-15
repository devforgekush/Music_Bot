# Audify Deployment Guide

## Railway Deployment

### Steps:
1. **Connect GitHub Repo**: Go to [Railway](https://railway.app/), create a new project, and link your GitHub repository.
2. **Environment Variables**: Add the following variables in Railway's dashboard (use `.railway.env.sample` as reference):
   - BOT_TOKEN
   - SESSION_STRING
   - API_ID
   - API_HASH
   - CUSTOM_API_KEY
   - LOG_CHANNEL_ID
    - OWNER_ID
    - OWNER_USERNAME (set to `@i_am_alive_as_fumk`)
    - CHANNEL_USERNAME (set to `@alpha_dead4`)
    - CHANNEL_USERNAME (set to `@alpha_dead`)
   - KEEP_ALIVE=false
3. **Startup Command**: Railway will auto-detect the `Procfile` (`web: python -m Audify`).
4. **Deploy**: Click deploy. View logs in the Railway dashboard.

---

## Replit Deployment

### Steps:
1. **Import Repo**: Go to [Replit](https://replit.com/), create a new Python repl, and import your repo.
2. **Environment Variables**: Add the required variables in Replit's Secrets tab (see `.railway.env.sample`).
3. **Keep Alive**: The bot will start a minimal Flask server if `KEEP_ALIVE=true` (handled in `keep_alive.py`).
4. **Uptime Pings**: Use [UptimeRobot](https://uptimerobot.com/) or similar to ping `https://<your-repl-username>.<your-repl-name>.repl.co/` every 5 minutes.
5. **Start Bot**: Run the repl. Logs appear in the console.

---

## Separation of Concerns

- Use `.env.railway` and `.env.replit` for different environments.
- Example switch script:

```python
import os
from dotenv import load_dotenv

env = os.environ.get("DEPLOY_ENV", "railway")
if env == "replit":
    load_dotenv(".env.replit")
else:
    load_dotenv(".env.railway")
```

Add this to your config loading logic if you want to auto-switch based on environment.
