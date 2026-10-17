import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

# Owner/admin configuration
MAIN_OWNER = 8618826475
SUPER_ADMIN_NAME = "@Realegoalive"
SUPER_ADMIN_LINK = "https://t.me/Realegoalive"
SUPER_ADMINS = [8793132805]
LOG_CHANNEL_ID = -1003884046710

# Set BOT_TOKEN in Railway > Variables. Do not commit a live token to GitHub.
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError("Missing BOT_TOKEN. Add it in Railway > Variables.")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

def is_admin(user_id: int) -> bool:
    return user_id == MAIN_OWNER or user_id in SUPER_ADMINS

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Bot is online.\\n"
        f"Super admin: {SUPER_ADMIN_NAME}\\n"
        f"Contact: {SUPER_ADMIN_LINK}"
    )

@dp.message(Command("whoami"))
async def whoami(message: Message):
    uid = message.from_user.id if message.from_user else 0
    await message.answer(
        f"Your Telegram ID: {uid}\\n"
        f"Owner access: {'yes' if is_admin(uid) else 'no'}"
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
