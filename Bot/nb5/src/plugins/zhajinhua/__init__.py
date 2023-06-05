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
from .zjhcore import Card

parser = ArgumentParser("炸金花", description="炸")
game=Card()
zhajinhua = on_shell_command("炸金花",aliases={"炸金花","加入","炸"}, parser=parser, block=True, priority=13)
@zhajinhua.handle()
async def begin(bot: Bot, event: GroupMessageEvent, state: T_State):
    newplayer=event.get_user_id()
    name=str(event.sender.card)
    if game.game_running:
        await zhajinhua.send("游戏正在进行中哦，请稍后加入。")
    elif game.player_number==0:
        game.host=newplayer
        game.add_player(player=newplayer,name=name)
        await zhajinhua.send(name+"开始了一局游戏，还有人要加入吗？\n\n输入[炸金花，加入，炸]加入一局游戏\n")
    else:
        await add_person(newplayer,name)

async def add_person(newplayer,name):
    game.add_player(player=newplayer,name=name)
    await zhajinhua.send(name + "已加入游戏，目前共"+str(game.player_number)+"人游戏。")


def meikai(event: MessageEvent) -> bool:
    return not game.game_running
def kaishiyouxi(state: T_State = State(), msg: str = EventPlainText()) -> bool:
    if msg in ['开','开始','开始游戏']:
        return True
    return False
startgame = on_message(Rule(meikai) & kaishiyouxi, block=True, priority=1)
@startgame.handle()
async def start(matcher: Matcher, event: MessageEvent, state: T_State = State()):
    sender=event.get_user_id()
    if game.game_running:
        await startgame.send("游戏已经开始了哦")
    elif sender!=game.host:
        await startgame.send("你不是房主，无法开始游戏")
    elif game.player_number<2:
        await startgame.send("人太少，无法开始游戏")
    else:
        game.start_game()
        game.host=sender
        await startgame.send("游戏开始！请房主设定游戏轮次！")

pao = on_shell_command("跑",aliases={"跑","溜了","润了"}, parser=parser, block=True, priority=13)
@pao.handle()
async def _pao(bot: Bot, event: GroupMessageEvent, state: T_State):
    sender=event.get_user_id()
    global game
    if sender==game.all_player[game.now_host]:
        game.status[game.now_host]='quit'
        game.remain_player-=1
        if game.remain_player == 1:
            winner=1
            for i in range(1,game.player_number+1,1):
                if game.status[i]!='quit': winner=i
            game.money[winner] += game.all_money
            await pao.send('本轮的赢家是' + game.group_name[winner])
            await pao.send('第'+str(game.game_round)+'轮的积分表')
            await pao.send(
                game.group_name[i] + ':' + str(game.money[i]) + '\n' for i in range(1, game.player_number + 1, 1))
            _response = game.new_round()
            if game.game_round > game.all_round:
                await pao.send('游戏轮次已到，游戏结束！')
                game2 = Card();
                game = game2;
                del game2
            elif _response == 'breakdown':
                await pao.send('有人破产了，游戏结束！')
                game2 = Card();
                game = game2;
                del game2
            elif _response == 'good':
                await pao.send("第"+str(game.game_round)+"轮游戏开始了，现在轮到" + game.group_name[game.now_host] + "了")

see = on_shell_command("看",aliases={"看","看牌"}, parser=parser, block=True, priority=11)
@see.handle()
async def seecard(bot: Bot, event: Event, state: T_State):
    sender=event.get_user_id()
    now_host=game.all_player[game.now_host]
    if sender!=now_host:
        await startgame.send("还没有轮到你！")
    else:
        #给他看牌
        i=game.now_host
        msg='你的牌是:['+game.cardlvlindex[game.cardlvl[i]]+']'+ game.parsecard(i)
        await get_bot().send_private_msg(user_id=game.all_player[i], message=msg)\
            # (game.group_name[i]+'的牌是:['+game.cardlvlindex[game.cardlvl[i]]+']'+ game.parsecard(i))
        game.status[i]='clear'
        await see.send('请下注！')

def wait_money(event: MessageEvent) -> bool:
    if game.set_money==0: return True
    if game.all_round==0: return True
    return game.wait_money
def get_money_input(state: T_State = State(), msg: str = EventPlainText()) -> bool:
    if re.fullmatch(r"\d+", msg):
        state["money"] = msg
        return True
    return False
# add_money_matcher = on_message(get_money_input, block=True, priority=11)
add_money_matcher = on_message(Rule(wait_money) & get_money_input, block=True, priority=11)
@add_money_matcher.handle()
async def _(matcher: Matcher, event: MessageEvent, state: T_State = State()):
    sender=event.get_user_id()
    money=int(event.raw_message)
    if game.all_round == 0 and game.host == sender:
        game.all_round=money
        await startgame.send("轮次设定完毕！\n请设定所有人的初始积分。")
    elif game.set_money == 0 and game.host == sender:
        game.set_money=money
        for i in range(1,game.player_number+1,1): game.money[i]=money
        await startgame.send("积分设定完毕")
        # await startgame.send(game.group_name[i]+'的牌是:['+game.cardlvlindex[game.cardlvl[i]]+']'+game.parsecard(i)+'\n'for i in range(1,game.player_number+1,1))
        game.now_host=2
        game.next_player=2
        await startgame.send("现在轮到"+game.group_name[game.now_host]+"操作了！")
        game.wait_money = True
    elif sender==game.all_player[game.now_host]:
        response=game.add_money(game.now_host,money)
        if response=='balance':
            await add_money_matcher.send('你的积分不足！')
        elif response=='insufficient':
            await add_money_matcher.send('你加的不够！')
        else:
            await add_money_matcher.send('收到'+game.group_name[game.now_host]+'的'+str(money)+'点积分，他还剩'+str(game.money[game.now_host])+'点积分。'
                                         +'\n现在轮到'+game.group_name[game.next_player]+'操作了！')
            game.now_host=game.next_player

def kai_at(state: T_State = State(), msg: str = EventPlainText()) -> bool:
    if re.fullmatch(r"开.*", msg):
        state["kai"] = msg
        return True
    return False
# add_money_matcher = on_message(get_money_input, block=True, priority=11)
kai = on_message(kai_at, block=True, priority=2)
@kai.handle()
async def _kai(matcher: Matcher, event: MessageEvent, state: T_State = State()):
    sender=str(event.user_id)
    a = str(event.raw_message)
    b = re.search('at,qq=\d*]', a)
    c = b[0].strip('at,qq=').strip(']')
    # await kai.send(sender)
    # await kai.send(game.all_player[game.now_host])
    global game
    if sender in game.iddict and sender==game.all_player[game.now_host]:
        kaier=game.iddict[sender]
        if game.status[kaier]=='quit': await kai.send('你已出局！')
        elif c not in game.iddict: await kai.send('你开的人不在游戏中！')
        else:
            kaiee=game.iddict[c]
            if game.status[kaiee]=='quit': await kai.send('你开的人已出局！')
            else:
                if game.status[kaier]=='shade': response = game.add_money(game.now_host, game.moneylvl)
                else:response = game.add_money(game.now_host, game.moneylvl*2)
                if response == 'balance':
                    await add_money_matcher.send('你的积分不足！')
                else:
                    winner, loser = game.open(kaier, kaiee)
                    await kai.send(game.group_name[kaier]+'开了'+game.group_name[kaiee]+'\n'+game.group_name[winner]+'赢了！')
                    # await kai.send(str(loser))
                    # await kai.send(game.status[loser])
                    # await kai.send(game.status[winner])
                    game.status[loser]='quit'
                    if game.remain_player==1:
                        game.money[winner]+=game.all_money
                        await kai.send('第'+str(game.game_round)+'轮的赢家是'+game.group_name[winner])
                        await kai.send('第'+str(game.game_round)+'轮的积分表')
                        await kai.send(game.group_name[i]+':'+str(game.money[i])+'\n' for i in range(1,game.player_number+1,1))
                        _response=game.new_round()
                        if game.game_round>game.all_round:
                            await kai.send('游戏轮次已到，游戏结束！')
                            game2 = Card();
                            game = game2;
                            del game2
                        elif _response=='breakdown':
                            await kai.send('有人破产了，游戏结束！')
                            game2=Card();game=game2;del game2
                        elif _response=='good':
                            await kai.send("第"+str(game.game_round)+"轮游戏开始了，现在轮到"+game.group_name[game.now_host]+"了")

    else:
        await kai.send('你不在游戏中！')
