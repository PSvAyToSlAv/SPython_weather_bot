import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


from config import TOKEN
from keyboard import weather_keyboard
from find_weather import check_weather
from user_tabel import write_user, find_city, update_city, find_user


bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)



class Form(StatesGroup):
    waiting_for_city = State()


@dp.message(CommandStart())
async def start_command(message: Message):
    # Обрабатывает команду /start, отправляет приветственное сообщение и кнопки.
    await message.answer("👋 Хотите узнать, какая погода на улице? 🧐\n\nЯ вам помогу! ☀️\n\nВведите свой город, чтобы узнать прогноз.",
                         reply_markup=weather_keyboard())


# Обработка нажатии на крнопку "weather_in_city"
@dp.callback_query(F.data == 'weather_in_city')
async def watch(callback: CallbackQuery):
    # Обрабатывает нажатие на кнопку "Погода в моем городе", выводит погоду или просит ввести город.
    await callback.answer()
    user_id = callback.message.chat.id
    city_ = find_city(user_id)
    weather = check_weather(city=city_)
    if weather != None and city_ != None:
        await callback.message.edit_text(weather, reply_markup=weather_keyboard())
    elif city_ == None:
        await callback.message.edit_text("🗺️ Нажми на кнопку “Город 🏙️” и введи название своего города, чтобы узнать прогноз погоды.", reply_markup=weather_keyboard())
    else:
        await callback.message.edit_text("Просим прошения, что-то пошло не так... 😕", reply_markup=weather_keyboard())


# Обработка нажатии на крнопку "profile"
@dp.callback_query(F.data == 'change_city')
async def watch(callback: CallbackQuery, state: FSMContext):
    # Обрабатывает нажатие на кнопку "Изменить город", показывает текущий профиль или просит ввести город.
    await callback.answer()
    user_id = callback.message.chat.id
    profile = find_user(user_id)
    await state.set_state(Form.waiting_for_city)
    if profile != None:
        await callback.message.edit_text(f"👤 Ваши данные:\n\n📍 user_id: {profile[0]}\n🏙️ Город: {profile[1]}",
                                        reply_markup=weather_keyboard())
    else:
        await callback.message.edit_text(f"👤 Ваши данные:\n\n📍 user_id: .......\n🏙️ Город: .......",
                                        reply_markup=weather_keyboard())


# Обработка ввода города
@dp.message(Form.waiting_for_city)
async def process_city(message: Message, state: FSMContext):
    # Обрабатывает ввод пользователем города, обновляет его в БД и показывает обновлённый профиль.
    user_id = message.from_user.id
    city = message.text
    update_city(user_id, city)
    profile = find_user(user_id)
    if profile != None:
        await message.answer(f"👤 Ваши данные успешно обновлены:\n\n📍 user_id: {profile[0]}\n🏙️ Город: {profile[1]}", reply_markup=weather_keyboard())
    await state.clear()


async def main():
    # Запускает бот в режиме polling.
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())