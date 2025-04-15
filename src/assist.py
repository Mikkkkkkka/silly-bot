import time
import re

from aiogram import Dispatcher
from aiogram.types import Message, FSInputFile
from typing import Callable

#
# Константы
#

# Регулярки
DA_REGEX = r'\W*д+а+\W*'
NET_REGEX = r'\W*н+е+т+\W*'
PHYSICS_REGEX = r'\W*ф+и+з+и+к+\w*\W*'
KAZAKHSTAN_REGEX = r'\W*к+а+з+а+х+с+т+а+н+\w*\W*'
ROSKOMNADZOR_REGEX = r'\W*р+о+с+к+о+м+н+а+д+з+о+р+\w*\W*'
EXIT_REGEX = r'.*exit(.*).*'
SYS_REGEX = r'.*sys.*'

# Айдишки пользователей
FATHER = 1868524158
LEXA = 659819125
THE_HATERS = 4001669564

# Файлы
FATHER_LIGOLAMBI = FSInputFile("father_ligolambi.gif")
LIGOLAMBI = FSInputFile("ligolambi.gif")


#
# Вспомогательные штуки
#

def reg_match(regex):
    return lambda x : re.fullmatch(regex, x)


def timestamp():
    return f'{'{:02d}'.format(time.localtime().tm_mday)}/{'{:02d}'.format(time.localtime().tm_mon)}/{'{:04d}'.format(time.localtime().tm_year)} | {'{:02d}'.format(time.localtime().tm_hour)}:{'{:02d}'.format(time.localtime().tm_min)}:{'{:02d}'.format(time.localtime().tm_sec)}'


def user_action_logger(func: Callable[[Message], tuple[Message, str]]):
    async def wrap(*args):

        try:
            message, log_from_func = await func(*args)
            log_message = f'[{timestamp()}] @{message.from_user.username}: {log_from_func}'

            print(log_message)
            with open('./ebobot_log.txt', 'a') as f:
                f.write(log_message + '\n')

        except TypeError:
            None
        return
    return wrap 


hod_leaderboard = []


dp = Dispatcher()