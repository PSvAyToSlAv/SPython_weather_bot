from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def weather_keyboard():
    keyboard_weather = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Погода ☁️", callback_data="weather_in_city")],
                                                             [InlineKeyboardButton(text="Город 🏙️", callback_data="change_city")]])
    return keyboard_weather

#def next_video_keyboard():
#    keyboard_next = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Далее>>", callback_data="next_watch_video")],
#                                                          [InlineKeyboardButton(text="в избранное", callback_data="like_watch_video")]])
#    return keyboard_next