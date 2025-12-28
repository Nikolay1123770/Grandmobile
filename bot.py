import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart

from pts_parser import parse_pts
from pts_description import build_pts_description

BOT_TOKEN = "8495248952:AAGuDm-AeeJyWyUJzJtaRqmacmMNg09Jed4"

async def start(message: Message):
    await message.answer("📸 Отправь фото ПТС")

async def handle_photo(message: Message, bot: Bot):
    photo = message.photo[-1]
    file = await bot.get_file(photo.file_id)

    path = f"pts_{message.from_user.id}.jpg"
    await bot.download_file(file.file_path, path)

    data = parse_pts(path)
    text = build_pts_description(data)

    await message.answer(text)

async def main():
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()

    dp.message.register(start, CommandStart())
    dp.message.register(handle_photo, F.photo)

    print("✅ Bot started")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
