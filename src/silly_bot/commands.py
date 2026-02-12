import random
import time

from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from aiogram.utils.formatting import Text, Strikethrough, Bold

from utils import dp, user_action_logger_async, RESOURCES_DIR

#
# Команды
#


@dp.message(CommandStart())
@user_action_logger_async
async def handle_start(message: Message) -> tuple[Message, str]:
    formatted = Text(
        "Привет! Я Ебобот\nРазраб - ", Strikethrough("даун"), " @mishakashaa"
    )
    await message.reply(**formatted.as_kwargs())
    return message, "МОЖЕТ НАПИСАТЬ!"


@dp.message(Command("ping"))
async def handle_ping(message: Message) -> None:
    ping_photo = FSInputFile(str(RESOURCES_DIR / "why_tag.png"))
    await message.answer_photo(ping_photo)


@dp.message(Command("scp"))
@user_action_logger_async
async def handle_scp(message: Message) -> tuple[Message, str]:
    user = message.from_user

    await message.reply("СЦП СОСА-А-А-АТЬ")
    time.sleep(1)
    await message.reply("ВАМ ВСЕМ ПИЗДЕЦ")
    time.sleep(1)
    await message.reply("ВАШЕ НТФ БЫЛО УНИЧТОЖЕНО")
    time.sleep(1)
    await message.reply("ХАОС ИНСЕРЖЕНСИ ПРАВИТ ЭТИМ")
    time.sleep(1)
    await message.reply("...")
    time.sleep(1)
    await message.reply("МЕСТОМ")
    time.sleep(1)
    await message.reply("ЭТО ТЕПЕРЬ")
    time.sleep(1)
    await message.reply("НАШЕ ФАСИЛИТИ")
    time.sleep(2)
    await message.reply("СЦП СОСА-А-А-А-А-А-А-А-АТЬ")

    return message, "любит лаборатории"


@dp.message(Command("roll"))
@user_action_logger_async
async def handle_roll(message: Message):

    message_text = message.text
    if message_text is None:
        return message, "не рандомит"

    com_args = message_text.split()[1::]

    try:
        if len(com_args) == 0:
            formatted = Text("1-100:\n", Bold(f"{random.randint(1, 100)}"))
            await message.reply(**formatted.as_kwargs())

        elif len(com_args) == 1:
            formatted = Text(
                f"1-{com_args[0]}:\n", Bold(f"{random.randint(1, int(com_args[0]))}")
            )
            await message.reply(**formatted.as_kwargs())

        elif len(com_args) == 2:
            if com_args[0] > com_args[1]:
                com_args[0], com_args[1] = com_args[1], com_args[0]

            formatted = Text(
                f"{com_args[0]}-{com_args[1]}:\n",
                Bold(f"{random.randint(int(com_args[0]), int(com_args[1]))}"),
            )
            await message.reply(**formatted.as_kwargs())

        else:
            raise ValueError()

    except ValueError:
        await message.reply("/roll [число?] [число?]")

    return message, "рандомит"
