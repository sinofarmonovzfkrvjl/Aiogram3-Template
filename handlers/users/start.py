import asyncio

from aiogram import types
from aiogram.filters import CommandStart

from handlers.users.scarper import detect_alphabet, translate_text
from loader import dp, bot

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(f"Salom {message.from_user.full_name}")

@dp.message()
async def start_handler(message: types.Message):
    text = detect_alphabet(message.text)
    if text == "Lotin va Krill":
        lotinkrill = translate_text('cyrtolat', message.text)
        await message.answer(lotinkrill['result'])
        print(lotinkrill)
        await asyncio.sleep(0.001)
        lotinkrill = translate_text('lattocyr', message.text)
        await message.answer(lotinkrill['result'])
        print(lotinkrill)
    elif text == "Lotin":
        lotinkrill = translate_text('lattocyr', message.text)
        await message.answer(lotinkrill['result'])
    elif text == "Krill":
        lotinkrill = translate_text('cyrtolat', message.text)
        await message.answer(lotinkrill['result'])
    else:
        await message.answer(message.text)