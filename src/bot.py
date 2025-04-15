import asyncio

from aiogram import Bot
from aiogram.types import Message, BotCommand
from os import getenv

from assist import *
from commands import *
from replies import *


#
# Системная штука
#

# Добавление команд в меню бота
async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command='scp', description='СЦП СОСА-А-А-А-АТЬ!!'),
        BotCommand(command='roll', description='Прям как в доте'),
        BotCommand(command='ping', description='Статус бота'),
    ]
    await bot.set_my_commands(main_menu_commands)


# Обработка обычных сообщений 
@dp.message()
async def handle_message(message: Message) -> None:
    if message.text is None: return
    if message.from_user.id == LEXA: return

    message_words = message.text.lower().split()

    if reg_match(DA_REGEX)(message_words[-1]):
        await da_reply(message)

    if reg_match(NET_REGEX)(message_words[-1]):
        await net_reply(message)

    if 'кт' in message_words:
        await kt_reply(message)

    if any([reg_match(ROSKOMNADZOR_REGEX)(x) for x in message_words]):
        await roskomnadzor_reply(message)

    if any([reg_match(PHYSICS_REGEX)(x) for x in message_words]):
        await physics_reply(message)
    
    if any([reg_match(KAZAKHSTAN_REGEX)(x) for x in message_words]):
        await kazakhstan_reply(message)


async def main() -> None:

    TOKEN = getenv('TELEGRAM_BOT_TOKEN')

    bot = Bot(TOKEN)
    await set_main_menu(bot)

    print(f'[{timestamp()}] Working?..')
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
