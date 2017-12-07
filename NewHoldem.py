class Hand:
    def __init__(self):
        self.hand=[]
        self.value=['',0,'']
        self.colors=['H','D','S','C']
        self.values=[14,13,12,11,10,9,8,7,6,5,4,3,2]

    def add(self,card):
        self.hand.append(card)
        self.hand.sort()
        self.hand.reverse()

    def isStraightFlush(self):
        values=[]
        colors=[]
        for card in self.hand:
            values.append(card[0])
            colors.append(card[1])
        for color in self.colors:
            if colors.count(color)>=5:
                for value in range(len(values)-4):
                    if values[value+1]==values[value]-1 and values[value+2]==values[value]-2 and values[value+3]==values[value]-3 and values[value+4]==values[value]-4:
                        self.value=['Poker',values(value),color]
                        return self.value


    def isFour(self):
        values=[]
        colors=[]
        for card in self.hand:
            values.append(card[0])
            colors.append(card[1])
        for value in self.values:
            if values.count(value)==4:
                self.value=['Kareta',value,'']
                return self.value

    def isFull(self):
        values=[]
        colors=[]
        for card in self.hand:
            values.append(card[0])
            colors.append(card[1])
        for value in self.values:
            if values.count(value)==3:
                for value2 in self.values:
                    if values.count(value2)>=2 and value!=value2:
                        self.value=['Full',value,value2]
                        return self.value

    def isFlush(self):
        values=[]
        colors=[]
        for card in self.hand:
            values.append(card[0])
            colors.append(card[1])
        for color in self.colors:
            if colors.count(color)>=5:
                self.value=['Kolor',0,color]
                return self.value

    def isStraight(self):
        values=[]
        colors=[]
        for card in self.hand:
            values.append(card[0])
            colors.append(card[1])
        for value in range(len(values)-4):
            if values[value+1]==values[value]-1 and values[value+2]==values[value]-2 and values[value+3]==values[value]-3 and values[value+4]==values[value]-4:
                self.value=['Strit',value,'']
                return self.value

    def isThree(self):
        values=[]
        colors=[]
        for card in self.hand:
            values.append(card[0])
            colors.append(card[1])
        for value in self.values:
            if values.count(value)==3:
                self.value=['Trójka',value,'']
                return self.value

    def isTwo(self):
        values=[]
        colors=[]
        for card in self.hand:
            values.append(card[0])
            colors.append(card[1])
        for value in self.values:
            if values.count(value)==2:
                for value2 in self.values:
                    if values.count(value2)==2 and value!=value2:
                        self.value=['Dwie pary',value,value2]
                        return self.value
    def isPair(self):
        values=[]
        colors=[]
        for card in self.hand:
            values.append(card[0])
            colors.append(card[1])
        for value in self.values:
            if values.count(value)==2:
                self.value=['Para',value,'']
                return self.value

    def isHigh(self):
        self.value=['Wysoka karta',values[0],colors[0]]
        return self.value

    def check(self):
        none=['',0,'']
        self.isStraightFlush()
        if self.value==none:
            self.isFour()
        if self.value==none:
            self.isFull()
        if self.value==none:
            self.isFlush()
        if self.value==none:
            self.isStraight()
        if self.value==none:
            self.isThree()
        if self.value==none:
            self.isTwo()
        if self.value==none:
            self.isPair()
        if self.value==none:
            self.isHigh()
        return self.value


class player:
    def __init__(self,name,chips=0,AI=0):
        self.name=name
        self.chips=0
        self.bet=0
        self.AI=0
        self.lastaction=''
        self.hand=Hand()
    def bet(self,chips):
        self.lastaction='bet'
        self.bet+=chips
        self.chips-=chips
    def call(self):
        self.lastaction='check'
    def fold(self):
        self.lastaction='fold'
        self.hand=[]

class game:
    def __init__(self,player1,player2,player3=None,player4=None,chips=150,bigblind=2,progress=5):
        self.player1=player(player1,chips)
        self.player2=player(player2,chips)
        if player3!=None:
            self.player3=player(player3,chips)
            if player4!=None:
                self.player4=player(player4,chips)
        self.BB=bigblind
        self.SB=self.BB/2
        self.progress=progress
        self.progresscount=0
        self.actions=[]
        values=[14,13,12,11,10,9,8,7,6,5,4,3,2]
        colors=['H','D','C','S']
        self.deck=[]
        for value in values:
            for color in colors:
                self.deck.append[value,color]
        self.nextplayer=[self.player1,self.player2]
        if player3!=None:
            self.nextplayer.append(self.player3)
            if player4!=None:
                self.nextplayer.append(self.player4)
        self.activeplayers=self.nextplayer[:]
        self.activedeck=[]
        self.hands=[]
        self.bets={}
        for player in self.nextplayer:
            self.bets[player]=0
        self.bets['highest bet']=0

    def round(self):
        players=self.activeplayers
        move=players.pop[0]
        players.append(move)
        move=players.pop[0]
        players.append(move)
        turn=True
        bidded=False
        while turn==True:
            for x in range(len(self.activeplayers)):
                bidded=False
                play=input(players[0].name+' Action:')
                if play=='hand':
                    print(players[0].check)
                elif play=='bet':
                    ammount=int(input('how much:'))
                    move=players[0]
                    if ammount>self.bets['highest bet']-self.bets[move]:
                        move=players.pop[0]
                        players.append(move)
                        bidded=True
                        return move.bet(ammount)
                    else:
                        return('Not enough chips')
                elif play=='fold':
                    move=players.pop[0]
                    return move.fold()
                elif play=='call':
                    move=players[0]
                    if self.bets['highest bet']-self.bets[move]<move.chips:
                        move=players.pop[0]
                        players.append(move)
                        return move.bet(self.bets['highest bet']-self.bets[move])
                    else:
                        move=players.pop[0]
                        return move.bet(chips)
            if bidded==False:
                turn==False
                

    def phase1(self):
        self.count+=1
        self.activedeck=self.deck[:]
        for card in range(2):
            for player in self.nextplayer:
                random=self.activedeck.pop(random.randint(0,len(self.activedeck)))
                player.add(random)
        players=self.nextplayer[:]
        self.activeplayers=players[:]
        players[0].bet(self.SB)
        move=players.pop[0]
        players.append(move)
        players[0].bet(self.BB)
        move=players.pop[0]
        players.append(move)
        return self.round()

    def phase2(self):
        self.count+=1
        for card in range(3):
            random=self.activedeck.pop(random.randint(0,len(self.activedeck)))
            for player in self.activeplayers:
                player.add(random)
        return self.round()

    def phase3(self):
        self.count+=1
        random=self.activedeck.pop(random.randint(0,len(self.activedeck)))
        for player in self.activeplayers:
            player.add(random)
        return self.round()

    def phase4(self):
        self.count+=1
        random=self.activedeck.pop(random.randint(0,len(self.activedeck)))
        for player in self.activeplayers:
            player.add(random)
        return self.round()
            
        
    def endphase(self):
        self.progresscount+=1
        if self.progresscount==self.progress:
            self.progresscount=0
            self.BB*=2
            self.SB*=2
        for player in self.nextplayer:
            self.hands.append(player.hand())
        self.hands.sort()
        for player in self.activeplayers:
            if self.hands[0]==player.hand:
                winner(player)
        return self.clean()
        
        
    def winner(self,player):
        player.chips+=(self.table)

    def clean():
        self.count=0
        move=self.nextplayer.pop[0]
        self.nextplayer.append(move)
