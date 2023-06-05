from random import random
class Card:
    host=''
    player_number=0
    all_player=[];group_name=[];cards=[];cardlvl=[];money=[];status=[]
    cardlvlindex=['','高牌','对子','顺子','同花','同花顺','豹子']
    allcards=[]
    all_money=0;set_money=0;moneylvl=0
    now_host=0;next_player=0;remain_player=0
    iddict={}
    game_running=False;wait_money=False
    game_round=0;all_round=0

    def __init__(self):
        host=''
        self.player_number=0
        for i in range(53):
            self.allcards.append(True)
        self.all_player.append('none')
        self.group_name.append('none')
        self.status.append('quit')
        self.set_money=0
        self.moneylvl=1
        self.game_round=1

    def sort_key(self,num):
        return num%13
    def deal(self,playernum):
        tmpcard=[]
        count=0
        while(count<3):
            x=int(random()*52)
            if(self.allcards[x]):
                count+=1
                tmpcard.append(x)
                self.allcards[x]=False
        tmpcard.sort(key=self.sort_key)
        self.cards[playernum]=tmpcard
        f1=tmpcard[0]//13;f2=tmpcard[1]//13;f3=tmpcard[2]//13;
        n1=tmpcard[0]% 13;n2=tmpcard[1]% 13;n3=tmpcard[2]% 13;
        #同花
        if n1==n2 and n2==n3:
            self.cardlvl[playernum]=6
        elif f1==f2 and f2==f3:
            if n1+1==n2 and (n2+1)%13==n3: self.cardlvl[playernum]=5
            else: self.cardlvl[playernum]=4
        elif n1+1==n2 and (n2+1)%13==n3:
            self.cardlvl[playernum]=3
        elif n1==n2 or n2==n3 or n1==n3:
            self.cardlvl[playernum] =2
        else:self.cardlvl[playernum]=1

    def add_player(self,player,name):
        self.player_number+=1
        self.remain_player+=1
        self.iddict[player]=self.player_number
        self.all_player.append(player)
        self.group_name.append(name)

    def start_game(self):
        for i in range(self.remain_player+1):
            self.money.append(0)
            self.cardlvl.append([])
            self.cards.append([])
            self.status.append('shade')
        for i in range(53):
            self.allcards[i]=True
        for i in range(1,self.player_number+1,1):
            self.deal(i)
        self.game_running=True
        self.game_round=1
    #def new_round(self,host=now_host):

    def parsecard(self,number):
        tmp=[]
        flower=['黑桃','红桃','梅花','方片']
        for i in range(3):
            tmpflower=flower[self.cards[number][i]//13]
            tmpnum=self.cards[number][i]%13
            if   tmpnum==9: tmpflower+='J'
            elif tmpnum==10: tmpflower+='Q'
            elif tmpnum==11: tmpflower+='K'
            elif tmpnum == 12: tmpflower+='A'
            else: tmpflower+=str(tmpnum+2)
            tmp.append(tmpflower)
        tmpcard=tmp[0]+','+tmp[1]+','+tmp[2]
        return tmpcard

    def add_money(self,playernum,admoney):
        if self.money[playernum]<admoney: return 'balance'
        if self.status[playernum]=='shade':
            if self.moneylvl>admoney: return 'insufficient'
            self.moneylvl=admoney
        elif self.status[playernum]=='clear':
            if admoney%2==1 or admoney//2<self.moneylvl: return 'insufficient'
            self.moneylvl=admoney//2
        self.all_money+=admoney
        self.money[playernum]-=admoney
        self.next_player = self.now_host+1
        if self.next_player > self.player_number: self.next_player = 1
        while(self.status[self.next_player]=='quit'):
            self.next_player+=1
            if self.next_player>self.player_number: self.next_player=1
        return 'good'

    def open(self,p1,p2):
        self.remain_player-=1
        if self.cardlvl[p1]>self.cardlvl[p2]:
            return p1,p2
        elif self.cardlvl[p1]<self.cardlvl[p2]:
            return p2,p1
        else:
            if self.cardlvl[p1]!=2:
                if self.cards[p1][2]%13>self.cards[p2][2]%13: return p1,p2
                elif self.cards[p1][2]%13<self.cards[p2][2]%13: return p2,p1
                elif self.cards[p1][1]%13>self.cards[p2][1]%13: return p1,p2
                elif self.cards[p1][1]%13<self.cards[p2][1]%13: return p2,p1
                elif self.cards[p1][0]%13>self.cards[p2][1]%13: return p1,p2
                else: return p2,p1
            else:
                if self.cards[p1][1]%13>self.cards[p2][1]%13: return p1,p2
                elif self.cards[p1][1]%13<self.cards[p2][1]%13: return p2,p1
                elif self.cards[p1][2]%13>self.cards[p2][2]%13: return p1,p2
                elif self.cards[p1][0]%13>self.cards[p2][0]%13: return p1,p2
                else: return p2,p1
    def new_round(self):
        for i in range(53): self.allcards[i]=True
        self.remain_player=0
        self.moneylvl=0
        self.all_money=0
        self.game_round+=1
        self.now_host=self.game_round%self.player_number+1
        self.remain_player=self.player_number
        self.wait_money=True
        for i in range(1,self.player_number+1,1):
            self.status[i]='shade'
            if self.money[i]<=0:
                return 'breakdown'
            self.deal(i)
        return 'good'


if __name__ == '__main__':
    t=Card()
    t.add_player('zkj')
    t.add_player('lbh')
    t.start_game()
    print(t.parsecard(1))
    print(t.parsecard(2))
    print(t.add_money(1,100))
    print(t.add_money(2,10))
    print(t.open(1,2))
    print(t.cardlvlindex[t.cardlvl[1]])
    print(t.cardlvlindex[t.cardlvl[2]])
