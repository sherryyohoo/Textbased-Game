
import time
import sys

line1 = "                __ \n"
linea = " a           __/1  \__ \n" 
lineb = "b       __/1  \ __/2  \__ \n" 
linec = "c   __/1  \ __/2  \ __/3  \__ \n"
lined = "d /1  \ __/2  \ __/3  \ __/4  \ \n"
linee = "e \ __/1  \ __/2  \ __/3  \ __/ \n"
linef = "f /1  \__ /2  \ __/3  \ __/4  \ \n"
lineg = "g \ __/1  \ __/2  \ __/3  \ __/ \n"
lineh = "h /1  \ __/2  \ __/3  \ __/4  \ \n"
linei = "i \ __/1  \ __/2  \ __/3  \ __/ \n"
linej = "j /1  \ __/2  \ __/3  \ __/4  \ \n"
linek = "k \ __/1  \ __/2  \ __/3  \ __/ \n"
linel = "l     \ __/1  \ __/2  \ __/ \n"
linem = "m         \ __/3  \ __/ \n"
line15 = "              \ __/ \n"
board={'a':linea, 'b':lineb, 'c':linec,'d':lined, 'e':linee, 'f':linef, 'g':lineg, 'h':lineh, 'i':linei, 'j':linej, 'k':linek, 'l':linel, 'm':linem}

copy2=list(linea)
copy3=list(lineb)
copy4=list(linec)
copy5=list(lined)
copy6=list(linee)
copy7=list(linef)
copy8=list(lineg)
copy9=list(lineh)
copy10=list(linei)
copy11=list(linej)
copy12=list(linek)
copy13=list(linel)
copy14=list(linem)

availableSpots=['a1','b1','b2','c1','c2','c3','d1','d2','d3','d4','e1','e2','e3','f1','f2','f3','f4','g1','g2','g3','h1','h2','h3','h4','i1','i2','i3','j1','j2','j3','j4','k1','k2','k3','l1','l2','m1']
#planting={'1':['a1'],'2':['j1'],'3':['m1'],'4':['d4']}

lines=[[copy2,[16]],[copy3,[11,19]],[copy4,[7,15,23]],[copy5,[3,11,19,27]],[copy6,[7,15,23]],[copy7,[3,11,19,27]],[copy8,[7,15,23]],[copy9,[3,11,19,27]],[copy10,[7,15,23]],[copy11,[3,11,19,27]],[copy12,[7,15,23]],[copy13,[11,19]],[copy14,[15]]]

NUM_SEED=6;
NUM_SMALL=8;
NUM_MEDIUM=4;
NUM_LARGE=2;
NUM_ROUNDS=5;
TOTAL_ROUNDS=5;
NUM_DAYS=0;
NUM_PLAYERS=0
PLAYERS=[]
PLAYER_NAMES=[]

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)

def modifyBoard(place,new):
	global lines,board
	place=list(place)
	lineId=place[0]
	numberId=int(place[1])
	new=list(new)
	treeSize=new[0]
	playerID=new[1]

	for line in lines:
		if lineId in line[0]:
			index=line[1][numberId-1]
			line[0][index]=treeSize
			line[0][index+1]=playerID
			newline="".join(line[0])
			board[lineId]=newline

def printBoard():
	global line1,line15,board
	print(line1+board['a'],board['b'],board['c'],board['d'],board['e'],board['f'],board['g'],board['h'],board['i'],board['j'],board['k'],board['l'],board['m'],line15)

def intro():
	global NUM_PLAYERS,PLAYERS,availableSpots

	intro1="Welcom to The Mysterious Forest.\n"
	delay_print(intro1)
	input()
	intro2="In this game, each player can buy seeds or trees, plant seeds, and grow trees using light points. The larger the trees are, the more the light points you get each round.\n"
	delay_print(intro2)
	input()
	intro3="Each seed gets 1 light point, small tree gets 2 light points, medium tree gets 3 light points, and large tree gets 4 light points.\n"
	delay_print(intro3)
	input()
	intro4="Each player has 2 seeds, 2 small trees, and 1 medium tree available to plant and grow at the beginning of the game. Each player also has 1 small tree already planted.\n"
	delay_print(intro4)
	input()

	while 1:
		NUM_PLAYERS=input("Now tell me how many players are playing the game? [1,2,3,4]\n>>")
		if NUM_PLAYERS in ["1","2","3","4"]:
			NUM_PLAYERS=int(NUM_PLAYERS)
			break
		else:
			print("Please give correct number of players.")
	print("\nNow you can choose your name in the game. For convenience, please choose names of different initials.")
	input()
	for i in range(NUM_PLAYERS):
		playername=input("\nWhat do you want to be called, player{}?\n>>".format(i+1))
		initial=playername[:1].lower()
		PLAYER_NAMES.append(playername)
		PLAYERS.append(initial)

	if(NUM_PLAYERS==1):
		availableSpots.remove('a1')
		modifyBoard('a1','S'+PLAYERS[0])
	if(NUM_PLAYERS==2):
		availableSpots.remove('a1')
		availableSpots.remove('m1')
		modifyBoard('a1','S'+PLAYERS[0])
		modifyBoard('m1','S'+PLAYERS[1])
	if(NUM_PLAYERS==3):
		availableSpots.remove('a1')
		availableSpots.remove('m1')
		availableSpots.remove('j1')
		modifyBoard('a1','S'+PLAYERS[0])
		modifyBoard('j1','S'+PLAYERS[1])
		modifyBoard('m1','S'+PLAYERS[2])
	if(NUM_PLAYERS==4):
		availableSpots.remove('a1')
		availableSpots.remove('m1')
		availableSpots.remove('j1')
		availableSpots.remove('d4')
		modifyBoard('a1','S'+PLAYERS[0])
		modifyBoard('j1','S'+PLAYERS[1])
		modifyBoard('m1','S'+PLAYERS[2])
		modifyBoard('d4','S'+PLAYERS[3])

	print("\nNow the forest is set up for you. The first letter represents the tree size, and the second letter is your name initial. Let's take a look.")
	input()
	printBoard()
	input()
	print("\nAre you ready to start the game?")
	input()


class player:
	global lines,board,NUM_SEED,NUM_SMALL,NUM_MEDIUM,NUM_LARGE
	def __init__(self,playerId,turn,points,canPlantsmall,canPlantmedium,canPlantlarge,canPlantseeds,buySeeds,buySmall,buyMedium,buyLarge,tokens,plantSeeds,plantSmall,plantMedium,plantLarge):
		self.id=playerId
		self.points=points
		self.canSmall=canPlantsmall
		self.canMedium=canPlantmedium
		self.canLarge=canPlantlarge
		self.canSeeds=canPlantseeds
		self.buySeeds=buySeeds
		self.buySmall=buySmall
		self.buyMedium=buyMedium
		self.buyLarge=buyLarge
		self.plantSeeds=plantSeeds
		self.plantSmall=plantSmall
		self.plantMedium=plantMedium
		self.plantLarge=plantLarge
		self.tokens=tokens
		self.turn=turn

	def actionBuy(self):
		if (self.points>0):
			canSeed = "seeds"
			canSmall = "small trees"
			canMedium = "medium trees"
			canLarge = "large trees"
			if (self.buySeeds==NUM_SEED-2):
				canSeed=""
			if (self.buySeeds==0) or (self.buySmall==NUM_SMALL-2) or (self.points<2):
				canSmall = ""
			if (self.buySmall==0) or (self.buyMedium==NUM_MEDIUM-1) or (self.points<3):
				canMedium = ""
			if (self.buyMedium==0) or (self.buyLarge==NUM_LARGE) or (self.points<4):
				canLarge = ""
			if (canSeed=="") and (canSmall=="") and (canMedium=="") and (canLarge== ""):
				print("You cannot buy anything, please choose another action\n")
				input()
				self.play()
			else:
				print("You can only buy {} {} {} {}".format(canSeed,canSmall,canMedium,canLarge))

				buy_action=input("\nWhat are you going to do? [GoBack, Buy]\n>>")
				if buy_action=="GoBack":
					self.play()
				else:
					buy_action2=input("\nWhat do you want to buy? [{},{},{},{}]\n>>".format(canSeed,canSmall,canMedium,canLarge))
					if buy_action2=="seeds" and canSeed=="seeds":
						print("You bought a seed successfully")
						input()
						self.canSeeds+=1
						self.buySeeds+=1
						self.points-=1
					if buy_action2=="small trees" and canSmall == "small trees":
						print("You bought a small tree successfully")
						input()
						self.canSmall+=1
						self.buySmall+=1
						self.points-=2
					if buy_action2=="medium trees" and canMedium == "medium trees":
						print("You bought a medium tree successfully")
						input()
						self.canMedium+=1
						self.buyMedium+=1
						self.points-=3
					if buy_action2=="large trees" and canLarge == "large trees":
						print("You bought a large tree successfully")
						input()
						self.canLarge+=1
						self.buyLarge+=1
						self.points-=4
					print("You still have {} points".format(self.points))
					input()
				canSeed = "seeds"
				canSmall = "small trees"
				canMedium = "medium trees"
				canLarge = "large trees"
				next_action=input("\nwhat are you going to do? [Skip,Buy more,Another action]\n>>")
				if next_action == "Buy more":
					self.actionBuy()
				elif next_action == "Another action":
					self.play()
				else:
					self.turn=False
		else:
			print("\nYou don't have enough light points.\n")
			self.turn=False

	def actionGrow(self):
		if (self.points>0):
			canSeed = "seeds"
			canSmall = "small trees"
			canMedium = "medium trees"
			if (not self.plantSeeds) or (self.canSmall == 0):
				canSeed=""
			if (not self.plantSmall) or (self.points<2) or (self.canMedium == 0):
				canSmall=""
			if (not self.plantMedium) or (self.points<3) or (self.canLarge == 0):
				canMedium=""
			if (canSeed=="") and (canSmall=="") and (canMedium==""):
				print("You cannot grow anything, please choose another action\n")
				input()
				self.play()
			else:
				print("You can only grow {} {} {}".format(canSeed,canSmall,canMedium))
				grow_action=input("\nWhat are you going to do? [GoBack, Grow]\n>>")
				if grow_action=="GoBack":
					self.play()
				else:
					grow_action2=input("\nWhat do you want to grow? [{},{},{}]\n>>".format(canSeed,canSmall,canMedium))
					if grow_action2=="seeds" and canSeed=="seeds":
						print("\nAvailable seeds to grow: {}".format(self.plantSeeds))
						input()
						while 1:
							seedtoGrow=input("\nWhich seed do you want to grow?\n>>")
							if seedtoGrow in self.plantSeeds:
								modifyBoard(seedtoGrow,'S'+self.id)
								printBoard()
								self.points-=1
								self.canSmall-=1
								self.plantSeeds.remove(seedtoGrow)
								self.plantSmall.append(seedtoGrow)
								break
					if grow_action2=="small trees" and canSmall=="small trees":
						print("Available small trees to grow: {}".format(self.plantSmall))
						input()
						while 1:
							smalltoGrow=input("\nWhich small tree do you want to grow?\n>>")
							if smalltoGrow in self.plantSmall:
								modifyBoard(smalltoGrow,'M'+self.id)
								printBoard()
								self.points-=2
								self.canMedium-=1
								self.plantSmall.remove(smalltoGrow)
								self.plantMedium.append(smalltoGrow)
								break
					if grow_action2=="medium trees" and canMedium=="medium trees":
						print("Available medium trees to grow: {}".format(self.plantMedium))
						input()
						while 1:
							mediumtoGrow=input("\nWhich medium tree do you want to grow?\n>>")
							if mediumtoGrow in self.plantMedium:
								modifyBoard(mediumtoGrow,'L'+self.id)
								printBoard()
								self.points-=3
								self.canLarge-=1
								self.plantMedium.remove(mediumtoGrow)
								self.plantLarge.append(mediumtoGrow)
								break
					print("You still have {} points".format(self.points))
					input()
				canSeed = "seeds"
				canSmall = "small trees"
				canMedium = "medium trees"
				next_action=input("\nwhat are you going to do? [Skip,Grow more,Another action]\n>>")
				if next_action == "Grow more":
					self.actionGrow()
				elif next_action == "Another action":
					self.play()
				else:
					self.turn=False
		else:
			print("\nYou don't have enough light points.\n")



	def actionPlant(self):
		global board, availableSpots
		if (self.points>0):
			if(self.canSeeds == 0):
				print("\nYou don't have enough seeds to plant, please choose another action.")
				input()
				self.play()
			else:
				print("\nYou have {} seeds that you can plant.".format(self.canSeeds))
				input()
				plant_action=input("What are you going to do? [GoBack, Plant]\n>>")
				if plant_action=="GoBack":
					self.play()
				else:
					printBoard()
					while 1:
						plant_action2=input("\nWhere do you want to plant?\n>>")
						if (plant_action2 in availableSpots):
							self.plantSeeds.append(plant_action2)
							availableSpots.remove(plant_action2)
							self.canSeeds -= 1
							self.points -= 1
							modifyBoard(plant_action2,'s'+self.id)
							printBoard()
							print("You still have {} points".format(self.points))
							input()
							break
						else:
							print("The spot is not available.")
			while 1:
				next_action=input("\nWhat are you going to do? [Skip,Plant more,Another action]\n>>")
				if next_action == "Plant more":
					self.actionPlant()
					break
				elif next_action == "Another action":
					self.play()
					break
				elif next_action == 'Skip':
					self.turn=False
					break
				else:
					print("Give a correct response [Skip,Plant more,Another action]")
		else:
			print("\nYou don't have enough light points.\n")
			self.turn=False

	def play(self):
		if (self.points>0):
			action = input("\nWhat are you going to do? [Skip,Buying,Planting,Growing]\n>>")
			if (action == "Buying"):
				self.actionBuy()
			if (action == "Growing"):
				self.actionGrow()
			if (action == "Planting"):
				self.actionPlant()
		else:
			print("You don't have enough light points.")

	def addPoints(self):
		seedPoints = len(self.plantSeeds)
		smallPoints = len(self.plantSmall)*2
		mediumPoints = len(self.plantMedium)*3
		largePoints = len(self.plantLarge)*4
		addPoints=seedPoints+smallPoints+mediumPoints+largePoints
		self.points += addPoints

	def getPoints(self):
		seedPoints = len(self.plantSeeds)
		smallPoints = len(self.plantSmall)*2
		mediumPoints = len(self.plantMedium)*3
		largePoints = len(self.plantLarge)*4
		addPoints=seedPoints+smallPoints+mediumPoints+largePoints
		return addPoints

	def getTotal(self):
		seedPoints = len(self.plantSeeds)
		smallPoints = len(self.plantSmall)*3
		mediumPoints = len(self.plantMedium)*7
		largePoints = len(self.plantLarge)*14
		lightPoints = round(self.points/1.5)
		return seedPoints+smallPoints+mediumPoints+largePoints+lightPoints

	def getSmall(self):
		return len(self.plantSmall)

	def getMedium(self):
		return len(self.plantMedium)

	def getLarge(self):
		return len(self.plantLarge)

	def getLight(self):
		return self.points


def main():
	global board, NUM_ROUNDS, NUM_DAYS,PLAYERS,PLAYER_NAMES,NUM_PLAYERS,TOTAL_ROUNDS
	#printBoard()
	#turn,points,canPlantsmall,canPlantmedium,canPlantlarge,canPlantseeds,buySeeds,buySmall,buyMedium,buyLarge,tokens,plantSeeds,plantSmall,plantMedium,plantLarge
	intro()

	players=[]
	totalPoints=[]

	if(NUM_PLAYERS==1):
		player1=player(PLAYERS[0],True,0,2,1,0,2,0,0,0,0,0,[],["a1"],[],[])
		players.append(player1)
	if(NUM_PLAYERS==2):
		player1=player(PLAYERS[0],True,0,2,1,0,2,0,0,0,0,0,[],["a1"],[],[])
		player2=player(PLAYERS[1],True,0,2,1,0,2,0,0,0,0,0,[],["m1"],[],[])
		players.append(player1)
		players.append(player2)
	if(NUM_PLAYERS==3):
		player1=player(PLAYERS[0],True,0,2,1,0,2,0,0,0,0,0,[],["a1"],[],[])
		player2=player(PLAYERS[1],True,0,2,1,0,2,0,0,0,0,0,[],["j1"],[],[])
		player3=player(PLAYERS[2],True,0,2,1,0,2,0,0,0,0,0,[],["m1"],[],[])
		players.append(player1)
		players.append(player2)
		players.append(player3)
	if(NUM_PLAYERS==4):
		player1=player(PLAYERS[0],True,0,2,1,0,2,0,0,0,0,0,[],["a1"],[],[])
		player2=player(PLAYERS[1],True,0,2,1,0,2,0,0,0,0,0,[],["j1"],[],[])
		player3=player(PLAYERS[2],True,0,2,1,0,2,0,0,0,0,0,[],["m1"],[],[])
		player4=player(PLAYERS[3],True,0,2,1,0,2,0,0,0,0,0,[],["d4"],[],[])
		players.append(player1)
		players.append(player2)
		players.append(player3)
		players.append(player4)

	#play game
	while NUM_ROUNDS > 0:
		print("The trees are using their leaves to trap the sun's energy...")
		input()
		roundPoints=[]
		for p in players:
			p.addPoints()
			roundPoints.append(p.getPoints())
		print("In this round,",end=" ")
		for i in range(NUM_PLAYERS):
			print("{} gets {} points,".format(PLAYER_NAMES[i],roundPoints[i]), end=" ")
		print()
		input()
		for n in range(NUM_PLAYERS):
			print("\nNow it is {}'s turn".format(PLAYER_NAMES[n]))
			players[n].play()
		NUM_DAYS+=1
		NUM_ROUNDS-=1
		print("The {} day passed, there are {} days remain".format(NUM_DAYS, NUM_ROUNDS))
		input()

	#end of game
	print("\nCongratulations! {} days passed and you all contributed to the growth of the forest.".format(TOTAL_ROUNDS))
	input()
	for m in range(NUM_PLAYERS):
		result="\n{} planted {} small trees, {} medium trees, {} large trees, and has {} remaining light points\n".format(PLAYER_NAMES[m],players[m].getSmall(),players[m].getMedium(),players[m].getLarge(),players[m].getLight())
		delay_print(result)
		totalPoints.append(players[m].getTotal())
	input()

	maxPoints = max(totalPoints)
	winners=[i for i, j in enumerate(totalPoints) if j == maxPoints]
	if len(winners)==1:
		print("\nSo the winner is")
		input()
		print(PLAYER_NAMES[winners[0]])
	else:
		print("\nSo the winners are")
		input()
		for numWinners in range(len(winners)):
			print(PLAYER_NAMES[winners[numWinners]])


main()