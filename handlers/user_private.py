from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command, or_f
from aiogram.utils.formatting import as_list, as_marked_section, Bold

from filters.chat_types import ChatTypeFilter
from keyboards.reply import get_keyboard

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private', ]))


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(
        'Привет! Я виртуальный помощник.',
        reply_markup=get_keyboard(
            'Меню',
            'О магазине',
            'Варианты оплаты',
            'Варианты доставки',
            placeholder='Что вас интересует?',
            sizes=(2, 2),
        )
    )


# @user_private_router.message(F.text.lower().contains('меню'))
@user_private_router.message(or_f(Command('menu'), F.text.lower() == 'меню', CommandStart()))
async def menu_cmd(message: types.Message):
    await message.answer('Привет! Я виртуальный помощник.',
                         reply_markup=get_keyboard(
                             'Меню',
                             'О магазине',
                             'Варианты оплаты',
                             'Варианты доставки',
                             placeholder='Что вас интересует?',
                             sizes=(2, 2),
                         ))


@user_private_router.message(F.text.lower().contains('о нас'))
@user_private_router.message(Command('about'))
async def about_cmd(message: types.Message):
    await message.answer('О нас:')


@user_private_router.message(F.text.lower().contains('оплат'))
@user_private_router.message(Command('payment'))
async def payment_cmd(message: types.Message):
    text = as_marked_section(
        Bold('Варианты оплаты:'),
        'Картой в боте',
        'При получении карта/наличные',
        'В заведении',
        marker='✔ '
    )
    await message.answer(text.as_html())


@user_private_router.message(F.text.lower().contains('доставк'))
@user_private_router.message(Command('shipping'))
async def shipping_cmd(message: types.Message):
    text = as_list(
        as_marked_section(
            Bold('Варианты доставки:'),
            'Курьер',
            'Самовывоз',
            'В заведении',
            marker='✔ '
        ),
        as_marked_section(
            Bold('Невозможно: '),
            'Почта',
            'Голуби',
            marker='❌ '
        ),
        sep='\n---------------------------------\n',
    )
    await message.answer(text.as_html())


@user_private_router.message(F.contact)
async def get_contact(message: types.Message):
    await message.answer(f'Номер получен')
    await message.answer(str(message.contact))


@user_private_router.message(F.location)
async def get_location(message: types.Message):
    await message.answer(f'Локация получен')
    await message.answer(str(message.location))
