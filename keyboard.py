from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def weather_keyboard():
    # Функция для создания инлайн клавиатуры с кнопками "Погода" и "Город".
    keyboard_weather = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Погода ☁️", callback_data="weather_in_city")],
                                                             # Кнопка "Погода" с callback_data "weather_in_city".
                                                             [InlineKeyboardButton(text="Город 🏙️", callback_data="change_city")]])
                                                             # Кнопка "Город" с callback_data "change_city".
    return keyboard_weather
    # Возвращает созданную инлайн клавиатуру.