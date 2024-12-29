from aiogram import Bot, Dispatcher, Router, types
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery
from aiogram.filters import Command
import asyncio
from config import TOKEN

# Инициализация бота
bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()

# Локальная база данных для хранения баланса
user_balances = {}

# Обработчик команды /start
@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Добро пожаловать! Вы можете пополнить баланс с помощью команды /donate."
    )

# Обработчик команды /donate
@router.message(Command("donate"))
async def cmd_donate(message: Message):
    amount = 1  # Установлено значение для 1 XTR

    prices = [LabeledPrice(label="⭐ Telegram Stars", amount=amount * 10)]  # Цена указывается в копейках

    await bot.send_invoice(
        chat_id=message.chat.id,
        title="Пополнение баланса",
        description="Оплата ⭐ Telegram Stars",
        payload="donate_stars",
        provider_token="",  # Оставьте пустым для Telegram Stars
        currency="XTR",  # Внутренняя валюта Telegram Stars
        prices=prices,
        start_parameter="donate"
    )

# Обработчик предчекового запроса
@router.pre_checkout_query()
async def pre_checkout_query_handler(pre_checkout_q: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)

# Обработчик успешного платежа
@router.message()
async def on_successful_payment(message: Message):
    if hasattr(message, "successful_payment") and message.successful_payment:
        payment = message.successful_payment
        user_id = message.from_user.id

        # Добавляем XTR на баланс пользователя
        if user_id not in user_balances:
            user_balances[user_id] = 0
        user_balances[user_id] += payment.total_amount // 100  # Конвертируем копейки в целое число

        await message.answer(
            f"Платеж успешно выполнен!\n"
            f"Сумма: {payment.total_amount // 100} {payment.currency}\n"
            f"Ваш новый баланс: {user_balances[user_id]} ⭐"
        )
    else:
        await message.answer("Ошибка: сообщение не содержит данных о платеже.")

# Обработчик команды /balance
@router.message(Command("balance"))
async def cmd_balance(message: Message):
    user_id = message.from_user.id
    balance = user_balances.get(user_id, 0)
    await message.answer(f"Ваш баланс: {balance} ⭐")

# Регистрация маршрутов и запуск
dp.include_router(router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())