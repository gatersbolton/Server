from nonebot import on_command, on_startswith, get_bot
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
import urllib3
import json

today = on_command("today", aliases={'trytest1','trytest2'}, priority=5)

@today.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    uid=event.get_user_id()
    print(uid)
    print(type(uid))
    await get_bot().send_private_msg(user_id=uid, message="好！！！")
    await today.send("测试成功！")

# parser = ArgumentParser("炸金花", description="猜单词")
# game=card
# zhajinhua = on_shell_command("wordle", parser=parser, block=True, priority=13)
#
#
# @zhajinhua.handle()
# async def begin(bot: Bot, event: Event, state: T_State):
#     await zhajinhua.send("开炸！")
#     await add_person()
#
# async def add_person(bot: Bot, event: Event, state: T_State):
#     newplayer=event.user_id
#     game.add_player(player=newplayer)
#     await send(newplayer+"已加入游戏")