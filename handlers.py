from aiogram import types, Router, Bot
from aiogram.filters import Command
from config import ADMIN_IDS, CHANNEL_ID
from database import add_movie, get_message_id

router = Router()

@router.message(Command("start"))
async def start_handler(msg: types.Message):
    await msg.answer("🎬 Kino kodini kiriting:")

@router.message(Command("add"))
async def add_movie_handler(msg: types.Message):
    if msg.from_user.id not in ADMIN_IDS:
        return await msg.answer("⛔ Siz admin emassiz.")

    try:
        _, code, message_id = msg.text.split()
        add_movie(code, int(message_id))
        await msg.answer(f"✅ Kod '{code}' bilan kino qo‘shildi (ID: {message_id})")
    except:
        await msg.answer("❌ Format: /add <kod> <message_id>")

@router.message()
async def movie_code_handler(msg: types.Message, bot: Bot):
    code = msg.text.strip()
    message_id = get_message_id(code)

    if message_id:
        try:
            await bot.copy_message(
                chat_id=msg.chat.id,
                from_chat_id=CHANNEL_ID,
                message_id=message_id
            )
        except Exception as e:
            await msg.answer(f"⚠️ Kino yuborishda xatolik: {str(e)}")
    else:
        await msg.answer("❌ Bunday koddagi kino topilmadi.")
