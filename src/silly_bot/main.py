import asyncio

from aiogram import Bot
from aiogram.types import Message, BotCommand
from os import getenv

from silly_bot.utils import (
    dp,
    reg_match,
    timestamp,
    expanded_word_regex, matches_with_any, expanded_word_with_multiple_endings,
)
from silly_bot.commands import *
from silly_bot.replies import *


#
# Системная штука
#


# Добавление команд в меню бота
async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command="scp", description="СЦП СОСА-А-А-А-АТЬ!!"),
        BotCommand(command="roll", description="Прям как в доте"),
        BotCommand(command="ping", description="Статус бота"),
    ]
    await bot.set_my_commands(main_menu_commands)


# Обработка обычных сообщений
@dp.message()
async def handle_message(message: Message) -> None:
    if message.text is None:
        return

    message_words = message.text.lower().split()

    if reg_match(expanded_word_regex("да"))(message_words[-1]):
        await da_reply(message)

    if reg_match(expanded_word_regex("нет"))(message_words[-1]):
        await net_reply(message)

    if any(reg_match(expanded_word_regex("очевидно"))(x) for x in message_words[-2::]):
        await ochevidno_reply(message)

    if any([reg_match(expanded_word_regex("роскомнадзор"))(x) for x in message_words]):
        await roskomnadzor_reply(message)

    if any([reg_match(expanded_word_regex("физика"))(x) for x in message_words]):
        await physics_reply(message)

    if any([reg_match(expanded_word_regex("казахстан"))(x) for x in message_words]):
        await kazakhstan_reply(message)

    if any([matches_with_any([
        expanded_word_with_multiple_endings("лесб"),
        expanded_word_with_multiple_endings("ге"),
        expanded_word_with_multiple_endings("бисекс"),
        expanded_word_with_multiple_endings("транс"),
        expanded_word_with_multiple_endings("гомос"),
        expanded_word_regex("квир"),
        expanded_word_regex("пидор"),
        expanded_word_regex("лгбт"),
    ])(x) for x in message_words]):
        await forbidden_reply(message)

    if "кт" in message_words:
        await kt_reply(message)


async def main() -> None:

    TOKEN = getenv("TELEGRAM_BOT_TOKEN")
    if TOKEN is None:
        print("Error: TELEGRAM_BOT_TOKEN environment variable is not set.")
        exit(1)

    bot = Bot(TOKEN)
    await set_main_menu(bot)

    print(f"[{timestamp()}] Working?..")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
