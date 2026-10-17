# Axiom Railway Telegram Bot Starter

This is a safe, minimal Telegram bot starter with the supplied owner/admin IDs and log channel ID configured.

## Deploy
1. Upload the files in this folder to a GitHub repository.
2. In Railway, deploy that repository.
3. Open the service's **Variables** tab.
4. Add `BOT_TOKEN` as the variable name and paste a newly generated Telegram bot token as its value.
5. Deploy/restart the service.

The token is intentionally not embedded in `main.py` or included in this ZIP. A token committed to a public repository can be stolen. Since the previously shared token was exposed, revoke it with `@BotFather` and use a fresh one.

## Included commands
- `/start` — confirms the bot is online and shows the configured super-admin contact.
- `/whoami` — shows your Telegram ID and whether it matches the configured owner/super-admin list.

This is a starter template, not the original bot. It does not include the original bot's device-based or bulk SMS functionality.
