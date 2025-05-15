from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token='7501896012:AAGCwfmVRI9fvjBj2AgW5K5xmMITfmauPjA')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привет! Я живой!")

if __name__ == '__main__':
    from aiogram import asyncio
    loop = asyncio.get_event_loop()
    executor.start_polling(dp, skip_updates=True)
