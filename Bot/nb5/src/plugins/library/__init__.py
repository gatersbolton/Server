from nonebot import on_command, on_startswith, get_bot, on_shell_command, on_message
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.rule import Rule, to_me, ArgumentParser
from dataclasses import dataclass
from nonebot.exception import ParserExit
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, NoticeEvent
from nonebot.params import ShellCommandArgv, CommandArg, EventPlainText, State
from nonebot.adapters.onebot.v11 import MessageEvent, GroupMessageEvent, Message, MessageSegment
from typing import Dict, List, Optional, NoReturn
import urllib3
import re
import json
from .libraryspider import libspider

parser = ArgumentParser("lib", description="图书馆预约")
parser.add_argument('-t', '--starttime', help='预约开始时间，接受小数，24小时制')
parser.add_argument('-d', '--duration', help='持续时长')
parser.add_argument('-s', '--seat', help='座位号，只支持3楼')
parser.add_argument('-a', '--account', help='使用系统中的哪个帐号，123表示')
parser.add_argument('-c', '--cancel', help='取消预约')
parser.add_argument('-u', '--use_now', help='转移到大号使用')
parser.add_argument('-jt', '--today', help='今天')
parser.add_argument('-mt', '--tomorrow', help='明天')
parser.add_argument("word", nargs="?", help="单词")

@dataclass
class Options:
    starttime: float = 18.5
    duration: float = 4
    seat: int = 12
    account: int = 1
    cancel: bool = False
    use_now: bool = False
    today: bool = True
    tomorrow: bool = False
    word: str = ""


library = on_shell_command("lib", parser=parser, block=True, priority=13)
@library.handle()
async def begin(matcher: Matcher, event: MessageEvent, argv: List[str] = ShellCommandArgv()):
    await handle_lib(matcher, event, argv)

async def handle_lib(matcher: Matcher, event: MessageEvent, argv: List[str]):
    try:
        args = parser.parse_args(argv)
        # await library.send(str(args))

    except ParserExit as e:
        if e.status == 0:
            await library.send("图书馆预约")#发送使用方法
        await library.send("预约图书馆")
    log=""
    options = Options(**vars(args))
    spider = libspider(user=1)
    if options.cancel:
        log, date, start_time, duration, seat, cancelable=spider.Cancel(True)
        await library.send(log)
    elif options.use_now:
        log, date, starttime, duration,seat,cancelable=spider.cancel()
        spider=libspider(user=0)
        log=spider.book(date=date,starttime=starttime,duration=duration,seat=seat)
        await library.send(log)
    else:
        spider=libspider(user=int(options.account))
        starttime=float(options.starttime)
        try:
            duration=float(options.duration)
        except:
            duration=4.0
        date='today'
        if options.tomorrow: date='tomorrow'
        log=spider.book(date=date,starttime=starttime,duration=duration,seat=int(options.seat))
        await library.send(log)


