# Railway Telegram Admin Bot (safe build)

This package starts from the supplied `custombomberbot.py` and preserves its owner/admin IDs, menus, user controls, and credit-management handlers. Automated SMS dispatch and the background device scanner are disabled.

## Deploy
1. Upload these files to a GitHub repository.
2. In Railway, deploy that repository.
3. In the service's **Variables** tab add `BOT_TOKEN` as the variable name and your **new** Telegram token as the value.
4. Start command: `python custombomberbot.py` (also configured in `railway.toml` and `Procfile`).
5. Check deployment logs, then test `/start`.

The Telegram token is deliberately not included in this source. Since the previously shared token was exposed, revoke it with @BotFather and use a newly generated token.

Note: features that depend on external Firebase/device APIs or media URLs may still require their original configuration and valid credentials.
