from random import random
class Card:
    host=''
    player_number=0
    all_player=[];cards=[];money=[];status=[]
    allcards=[]
    all_money=0
    moneylvl=0
    next_player=''
    remain_player=0
    iddict={}
    game_running=False

    def __init__(self):
        host=''
        self.player_number=0
        for i in range(53):
            self.allcards.append(True)

    def sort_key(self,num):
        return num%13
    def get_card(self):
        tmpcard=[]
        count=0
        while(count<3):
            x=int(random()*52)
            if(self.allcards[x]):
                count+=1
                tmpcard.append(x)
        tmpcard.sort(key=self.sort_key)
        return tmpcard

    def add_player(self,player):
        self.player_number+=1
        self.remain_player+=1
        self.iddict[player]=self.player_number
        self.all_player.append(player)
        self.cards.append(self.get_card())
        self.money.append(0)
        self.status.append('shade')

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
        return tmp

    def add_money(self,player,money):
        if self.status=='shade':
            if self.moneylvl>money: return False
            self.moneylvl=money
        elif self.status=='clear':
            if money%2==1 or money//2<self.moneylvl: return False
            self.moneylvl=money//2
        self.all_money+=money
        while(self.status[self.next_player]=='quit'):
            self.next_player+=1
            if self.next_player>self.all_player: self.next_player=1
        return True

    def compare(self,p1,p2):
        f1=p1[1]

    def open(self,p1,p2):
        1

if __name__ == '__main__':
    t=Card()
    t.add_player('zkj')
    t.add_player('lbh')
    print(t.parsecard(0))
    print(t.parsecard(1))
    print(t.iddict)

