import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import router
from database import init_db
from keep_alive import keep_alive  # 👈 qo‘shildi

async def main():
    init_db()
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    keep_alive()            # 👈 qo‘shildi
    asyncio.run(main())
