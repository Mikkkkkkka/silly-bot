import time

from aiogram.types import Message

from utils import *

#
# Ответы
#

@user_action_logger
async def da_reply(message: Message):
    await message.reply('ПИЗДА, АХАХАХАХА')
    return message, 'пизданулся!'


@user_action_logger
async def net_reply(message: Message):
    await message.reply('ПИДОРА ОТВЕТ')
    return message, 'пидорнулся!'


@user_action_logger
async def kt_reply(message: Message):
    for i in range(5):
        await message.reply('КТ СОСАТЬ!!!')
    return message, 'пускай сосут'


@user_action_logger
async def physics_reply(message: Message):
    await message.reply('Хуизика!!!')
    return message, 'произошла физика'


@user_action_logger
async def kazakhstan_reply(message: Message):
    for _ in range(3):
        await message.reply('КАЗАХСТАН УГРОЖАЕТ НАМ БОМБАРДИРОВКОЙ')
        time.sleep(1)
    return message, 'призвал казахов'

@user_action_logger
async def roskomnadzor_reply(message: Message):
    s = 'Роскомнадзор запретил букву '
    rep = ''
    for i in 'абвгдежзийклмнопрсту':
        rep += s + i + '\n'
        s = s.replace(i, '')
        s = s.replace(i.capitalize(), '')
        s = s.replace('  ', ' ')
    await message.reply(rep)
    return message, 'роскомнадзорнулся'

# Гоблин mentioned
@user_action_logger
async def ochevidno_reply(message: Message):
    time.sleep(1)
    await message.reply('Очевидно')
    time.sleep(1)
    await message.reply('Мало ли что очевидно')
    time.sleep(0.75)
    await message.reply('Вы все пидоры, вот что очевидно')
    return message, 'доочевидился'
