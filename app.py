import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

bot = Bot(token='7517430742:AAEE3q7fvhCiVuGwTOeIDAFOHKW_S9sueVk')

dp = Dispatcher()

@dp.message(CommandStart()) 
async def start_cmd(message: types.Message)  -> None:
    await message.answer('Это была команда старт')

@dp.message()
async def echo(message: types.Message)  -> None:
    text = message.text
    if text in ['Привет', 'привет', 'hello', 'hi']:
        await message.answer('И тебе привет!')
    elif text in ['Пока', 'пока', 'до свидания', 'bye']:
        await message.answer('И тебе пока!')
    else:
        await message.answer(message.text)

async def  main() -> None:
    await dp.start_polling(bot)

asyncio.run(main())