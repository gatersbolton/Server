from nonebot import on_command, on_startswith, get_bot, on_shell_command, on_message
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.rule import Rule, to_me, ArgumentParser
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, NoticeEvent
from nonebot.params import ShellCommandArgv, CommandArg, EventPlainText, State
from nonebot.adapters.onebot.v11 import MessageEvent, GroupMessageEvent, Message, MessageSegment
import urllib3
import re
import json
import openai
openai.api_key = "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"

tmp=""

async def AI_checker(event: Event) -> bool:
    rawmsg=str(event.get_message())
    global tmp
    tmp=rawmsg
    if(rawmsg.startswith("ai") or rawmsg.startswith("Ai") or rawmsg.startswith("aI") or
    rawmsg.startswith("AI") or rawmsg.startswith("chat") or rawmsg.startswith("Chat")):
        return True
    return False

chat = on_message(rule=AI_checker)
@chat.handle()
async def begin(bot: Bot, event: MessageEvent, state: T_State):
    rawmsg=str(event.raw_message)
    rawmsg=rawmsg.lstrip("AI");rawmsg=rawmsg.lstrip("ai");rawmsg=rawmsg.lstrip("Ai");
    rawmsg=rawmsg.lstrip("aI");rawmsg=rawmsg.lstrip("chat");rawmsg=rawmsg.lstrip("Chat");
    rawmsg=rawmsg.lstrip(" ")
    # airesponse=rawmsg
    prompt = rawmsg
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        temperature=0.5,
    )
    airesponse=str(response["choices"][0]["text"])
    airesponse=airesponse.lstrip("\n");
    await chat.send(airesponse)


