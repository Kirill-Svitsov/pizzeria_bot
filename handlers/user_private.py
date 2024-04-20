from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command, or_f

from filters.chat_types import ChatTypeFilter
from keyboards.reply import start_kb, start_kb2, start_kb3, del_kbd, test_keyboard

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private', ]))


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет! Я виртуальный помощник.',
                         reply_markup=start_kb3.as_markup(
                             resize_keybord=True,
                             input_field_placeholder='Что вас интересует?',
                         ))


# @user_private_router.message(F.text.lower().contains('меню'))
@user_private_router.message(or_f(Command('menu'), F.text.lower() == 'меню'))
async def menu_cmd(message: types.Message):
    await message.answer('Вот меню:', reply_markup=test_keyboard)


@user_private_router.message(F.text.lower().contains('о нас'))
@user_private_router.message(Command('about'))
async def about_cmd(message: types.Message):
    await message.answer('О нас:')


@user_private_router.message(F.text.lower().contains('оплат'))
@user_private_router.message(Command('payment'))
async def payment_cmd(message: types.Message):
    await message.answer('Способы оплаты:')


@user_private_router.message(F.text.lower().contains('доставк'))
@user_private_router.message(Command('shipping'))
async def shipping_cmd(message: types.Message):
    await message.answer('Способы доставки:')


@user_private_router.message(F.contact)
async def get_contact(message: types.Message):
    await message.answer(f'Номер получен')
    await message.answer(str(message.contact))


@user_private_router.message(F.location)
async def get_location(message: types.Message):
    await message.answer(f'Локация получен')
    await message.answer(str(message.location))
