from aiogram import types, F


from loader import dp, bot

@dp.message()
async def echo_handler(message: types.Message):
    await message.answer(message.text)