import asyncio
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не найден")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "👋 Привет!\n\n"
        "Я твой персональный бот для английского 🇬🇧✨\n\n"
        "📚 Каждый день:\n"
        "• современная грамматика\n"
        "• примеры из фильмов и сериалов\n"
        "• живая лексика\n\n"
        "Напиши /lesson — и начнём первый урок 🔥"
    )


@dp.message(Command("lesson"))
async def lesson(message: Message):
    await message.answer(
        "🎬 *Present Simple — как говорят в жизни*\n\n"
        "We use it when:\n"
        "• facts: *I live in Berlin*\n"
        "• habits: *I watch Netflix every night*\n\n"
        "❌ I watching Netflix every night\n"
        "✅ I watch Netflix every night\n\n"
        "📺 Из сериала:\n"
        "— *I work here.*\n\n"
        "📝 Попробуй:\n"
        "Напиши предложение про себя в Present Simple 👇",
        parse_mode="Markdown"
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
