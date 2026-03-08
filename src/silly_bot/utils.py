import time
import re
from pathlib import Path
from typing import Callable, Awaitable, List

from aiogram import Dispatcher
from aiogram.types import Message

#
# Константы
#

# Файлы
PACKAGE_ROOT = Path(__file__).resolve().parent
RESOURCES_DIR = PACKAGE_ROOT / "resources"

#
# Вспомогательные штуки
#

def expanded_word_regex(word: str) -> str:
    regex = [r"\W*"]
    for char in word:
        regex.append(f"{char}+")
    regex.append(r"\W*")
    return "".join(regex)


def reg_match(regex: str) -> Callable[[str], re.Match[str]]:
    return lambda x: re.fullmatch(regex, x)


def matches_with_any(regexes: List[str]) -> Callable[[str], bool]:
    def _inner(test: str) -> bool:
        for regex in regexes:
            if re.fullmatch(regex, test):
                return True
        return False
    return _inner


def timestamp():
    return f"{'{:02d}'.format(time.localtime().tm_mday)}/{'{:02d}'.format(time.localtime().tm_mon)}/{'{:04d}'.format(time.localtime().tm_year)} | {'{:02d}'.format(time.localtime().tm_hour)}:{'{:02d}'.format(time.localtime().tm_min)}:{'{:02d}'.format(time.localtime().tm_sec)}"


def user_action_logger(
    func: Callable[[Message], tuple[Message, str]],
):
    async def wrap(*args):

        try:
            message, log_from_func = func(*args)
            user = message.from_user
            if user is None:
                print("user_action_logger expects user to be non None")
                return

            log_message = f"[ {timestamp()} ] @{user.username}: {log_from_func}"
            print(log_message)
            with open("./ebobot_log.txt", "a") as f:
                f.write(log_message + "\n")

        except Exception as e:
            pass
        return

    return wrap


def user_action_logger_async(
    func: Callable[[Message], Awaitable[tuple[Message, str]]],
):
    async def wrap(*args):

        try:
            message, log_from_func = await func(*args)
            user = message.from_user
            if user is None:
                print("user_action_logger expects user to be non None")
                return

            log_message = f"[ {timestamp()} ] @{user.username}: {log_from_func}"
            print(log_message)
            with open("./ebobot_log.txt", "a") as f:
                f.write(log_message + "\n")

        except Exception as e:
            pass
        return

    return wrap


dp = Dispatcher()
