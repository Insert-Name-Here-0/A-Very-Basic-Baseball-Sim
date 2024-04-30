#Baseball Sim
import random
import time 

print("Inspired by Blaseball and Terror Ball.")

Texas_Austins = ["player1", "player2", "player3", "player4"]
Wyoming_Footprints = ["player5", "player6", "player7", "player8"]
Denver_Cheeseburgers = ["player9", "player10", "player11", "player12"]
New_Mexico_Dancing_Sombreros = ["player13", "player14", "player15", "player16"]
teams = [Texas_Austins,Wyoming_Footprints,Denver_Cheeseburgers,New_Mexico_Dancing_Sombreros]
teamnames = ["Texas Austins","Wyoming Footprints","Denver Cheeseburgers","New Mexico Dancing Sombreros"]

basepicker = 0

ballsmax = 4
strikemax = 3
outsmax = 3
hometeam = 0
awayteam = 0

inning = 0
balls = 0
strikes = 0
outs = 0

hitting = 0
fielding = 0
basestaken = 0
totalinnings = 1
maxinnings = 2
base1 = 0
base2 = 0
base3 = 0
bases = [base1, base2, base3]
baseindex = 0
playerIndex=0
awayrunstotal=0
homerunstotal=0
runscheck=0

balllocations= ["outfield right","infield right","outfield left","infield left","infield center","outfield center"]
fouls = ["outfield right","infield right","outfield left","infield left"]

#programming a match

hometeamnumber = random.randint(0,3)
hometeamname = teamnames[hometeamnumber]
hometeam = teams[hometeamnumber]
teams.remove(hometeam)
teamnames.remove(hometeamname)

awayteamnumber = random.randint(0,2)
awayteam = teams[awayteamnumber]
awayteamname = teamnames[awayteamnumber]

activeteamIndex = 0
activeteams=[awayteam , hometeam] #player names
activeteamsnames = [awayteamname,hometeamname] #team names
activeteamsscores = [awayrunstotal,homerunstotal] #team total scores
def game_reset():
    global playerIndex
    global inning
    global balls
    global strikes
    global outs
    global base1
    global base2
    global base3
    global basestaken
    global awayrunstotal
    global runscheck
    global homerunstotal
    playerIndex = 0
    inning = 0
    balls = 0
    strikes = 0
    outs = 0
    base1 = 0
    base2 = 0
    base3 = 0
    basestaken = 0
    awayrunstotal=0
    runscheck = 0
    homerunstotal=0

def inning_reset():
    global playerIndex
    global outs
    global bases
    global basestaken
    playerIndex = 0
    outs = 0
    bases[0] = 0
    bases[1] = 0
    bases[2] = 0
    basestaken = 0

def atbat_reset():
    global balls
    global strikes
    strikes=0
    balls=0

print("Before we start a match, would you like to change a rule?")
print("a. Yes")
print("b. No")
ans = input("Type a or b:")
if ans == "a":
    print("a. Would you like to increase ball count, strike count, or out count.")
    print("b. Alternatively, you can decrease those counts.")
    ans2=input("Type a or b:")
    if ans2 == "a":
        print("What would you like to increase:")
        print("a. Ball count")
        print("b. Strike count")
        print("c. Out count")
        ans3=input("Type a or b or c:")
        if ans3 == "a":
            ballsmax = 5
            print("Ball count increased to 5, are you trying to make it hard to get walks?")
        if ans3=="b":
            strikemax = 4
            print("Strike count increased to 4, how nice of you to make batters lives easier.")
        if ans3=="c":
            outsmax=4
            print("Out count increased to 4, these innings are going to take a bit to run through, aren't they?")
    if ans2=="b":
        print("What would you like to decrease:")
        print("a. Ball count")
        print("b. Strike count")
        print("c. Out count")
        ans3=input("Type a or b or c:")
        if ans3 == "a":
            ballsmax = 3
            print("Ball count decreased to 3, how kind of you to make walks more likely.")
        if ans3=="b":
            strikemax = 2
            print("Strike count decreased to 2, how nice of you to make pitchers lives easier.")
        if ans3=="c":
            outsmax=2
            print("Out count decreased to 2, this match is gonna be quick.")
if ans == "b":
    print("You don't want to anything alright then")

print("PLAY BALL!")
print(awayteamname,"vs", hometeamname)
game_reset()
if totalinnings <= maxinnings:
    if outs < outsmax:
        while strikes < strikemax:
                if outs==outsmax:
                    activeteamIndex=1
                    totalinnings=totalinnings+1
                    print(totalinnings)
                    print("Current score:", activeteamsscores[0],"-",activeteamsscores[1])
                    print("Bottom of the 1st inning")
                    inning_reset()
                if playerIndex == 4:
                    playerIndex = 0
                if balls == 0 and strikes == 0:
                    print(activeteams[activeteamIndex][playerIndex], "is up to bat")
                hitting = random.randint(1,10)
                print(hitting)
                time.sleep(1)
                if hitting <=3: #strike/out
                    strikes = strikes+1
                    print("Strike!",activeteams[activeteamIndex][playerIndex],"is caught looking")
                    time.sleep(1)
                    if strikes == strikemax:
                        print(activeteams[activeteamIndex][playerIndex], "is struck out")
                        time.sleep(1)
                        outs = outs + 1
                        playerIndex = playerIndex+1
                        atbat_reset()
                    print(strikes,"-",balls,"-",outs)
                if hitting == 4 or hitting == 5: #fouls
                    print(activeteams[activeteamIndex][playerIndex],"fouls it into", random.choice(fouls))
                    time.sleep(1)
                    if strikes < (strikemax-1):
                        strikes = strikes +1
                        time.sleep(2)
                    print(strikes,"-",balls,"-",outs)
                if hitting >= 6 and hitting <= 8: #balls
                    balls = balls +1
                    print("Ball!", strikes,"-",balls,"-",outs)
                    time.sleep(1)
                    if balls == ballsmax:
                        if basestaken == 0: #bases empty
                            bases[0] = bases[0] +1
                            basestaken = basestaken + 1
                        elif basestaken == 1 and bases[0]==1:#player on 1st
                            bases[0] = bases[0]+1
                            bases[1] = bases[1]+1
                            basestaken = basestaken + 1
                        elif basestaken ==2 and bases[0] ==2 and bases[1] == 1:
                            bases[0] = bases[0]+1
                            bases[1] = bases[1]+1
                            bases[2] = bases[1]+1
                            basestaken=basestaken+1
                        elif basestaken ==1 and bases[0] >= 2:#player on 2nd or 3rd
                            bases[1] = bases[1]+1
                            basestaken = basestaken+1
                        elif basestaken == 2 and bases[0] == 3 and bases[1] ==2: #player on 3rd+2nd
                            bases[2] = bases[2]+1
                            basestaken = basestaken +1
                        atbat_reset()
                        playerIndex = playerIndex + 1
                if hitting >=9: #hit the ball :)
                    print("Hit!")
                    print(activeteams[activeteamIndex][playerIndex],"bat it into", random.choice(balllocations))
                    time.sleep(1)
                    fielding = random.randint(1,13)
                    print(fielding)
                    atbat_reset()
                    if fielding <= 3: #out
                        if activeteamIndex == 0:
                            print(random.choice(hometeam), "catches the ball. Out!")
                        if activeteamIndex == 1:
                            print(random.choice(awayteam), "catches the ball. Out!")
                        outs = outs+1
                        print(strikes,"-",balls,"-",outs)
                        time.sleep(1)
                    if fielding >= 4 and fielding<=7: #1st base
                        print(activeteams[activeteamIndex][playerIndex],"has hit a single!")
                        time.sleep(1)
                        if basestaken == 0:
                            bases[0] = bases[0] +1
                            basestaken = basestaken + 1
                        elif basestaken == 1:
                            bases[0] = bases[0] + 1
                            bases[1] = bases[1]+1
                            basestaken = basestaken + 1
                        elif basestaken == 2:
                            bases[0] =bases[0] + 1
                            bases[1] = bases[1] + 1
                            bases[2] = bases[2] + 1
                            basestaken = basestaken + 1
                        print(bases)
                    if fielding == 8 or fielding == 9 or fielding == 10: #2nd base
                        print(activeteams[activeteamIndex][playerIndex],"has hit a double!")
                        time.sleep(1)
                        if basestaken == 0:
                            bases[0] = bases[0] + 2
                            basestaken = basestaken + 1
                        elif basestaken == 1:
                            if bases[0] >= 2:
                                bases[0] = 2
                                runscheck=runscheck+1
                            elif bases[0] == 1:
                                bases[0] = bases[0]+2
                                bases[1] = bases[1]+2
                                basestaken = basestaken+1
                        elif basestaken == 2:
                            bases[0] =bases[0] + 2
                            bases[1] = bases[1] + 2
                            basestaken = basestaken-1
                            bases[2] = bases[2] + 2
                        print(bases)
                    if fielding == 11 or fielding == 12: #3rd base
                        print(activeteams[activeteamIndex][playerIndex], "has hit a triple!")
                        time.sleep(1)
                        if basestaken == 0:
                            bases[0] = bases[0] + 3
                            basestaken = basestaken + 1
                        elif basestaken == 1:
                            bases[0] = bases[0] + 3
                            bases[1] = bases[1]+3
                            basestaken = basestaken + 1
                        elif basestaken == 2:
                            bases[0] =bases[0] + 3
                            bases[1] = bases[1] + 3
                            bases[2] = bases[2] + 3
                        elif basestaken == 3:
                            bases[0] =bases[0] + 3
                            bases[1] = bases[1] + 3
                            bases[2] = bases[2] + 3
                    if fielding == 13: #Homerun
                        print(activeteams[activeteamIndex][playerIndex],"has hit a homerun!")
                        time.sleep(1)
                        if basestaken == 0:
                            bases[0] = bases[0] + 4
                            basestaken = 1
                        elif basestaken == 1:
                            bases[0] = bases[0] + 4
                            bases[1] = bases[1]+4
                            basestaken = 2
                        elif basestaken == 2:
                            bases[0] =bases[0] + 4
                            bases[1] = bases[1] + 4
                            bases[2] = bases[2] + 4
                            basestaken = 3
                        elif basestaken == 3:
                            bases[0] =bases[0] + 4
                            bases[1] = bases[1] + 4
                            bases[2] = bases[2] + 4
                            awayrunstotal = awayrunstotal + 1
                            runscheck = runscheck + 1
                    atbat_reset()
                    playerIndex = playerIndex+1
                print(basestaken, bases)
                time.sleep(1)
                for x in bases:
                    if basestaken<0:
                        basestaken=0
                    if basestaken==0:
                        bases[basepicker]=0
                    if bases[basepicker]>=4:
                        activeteamsscores[activeteamIndex]=activeteamsscores[activeteamIndex]+1
                        runscheck=runscheck+1
                        if fielding >= 4 and fielding<=7 and basestaken >= 1: #single when bases loaded
                            bases[basepicker] =bases[basepicker]+1
                        if fielding >= 4 and fielding<=7 and basestaken >=1:
                            bases[0]=bases[1]
                            bases[1]=bases[2]
                        if fielding >= 8 and fielding <= 10 and basestaken == 2 and bases[0]>=2:
                            bases[0]=bases[1]
                            bases[1]=bases[2]
                            basepicker=0
                        if fielding >= 8 and fielding <= 10 and basestaken == 1 and bases[0]>=2: #Double when 2nd or 3rd are taken
                            bases[basepicker]=0
                            bases[0] = 2
                        if fielding == 11 or fielding == 12 and basestaken >= 1:
                            bases[2]=0
                            bases[1]=0
                            bases[0]=3
                            if basestaken == 2:
                                runscheck = runscheck+ 1
                                activeteamsscores[activeteamIndex]=activeteamsscores[activeteamIndex]+1
                            basestaken = basestaken - 1
                        if fielding == 11 or fielding == 12 and basestaken == 3:
                            bases[0]=3
                            bases[1]=0
                            bases[2]=0
                            basestaken = 1
                        else:
                            basestaken = basestaken - 1
                            bases[basepicker] = 0
                        basepicker = basepicker +1
                        time.sleep(1)
                if runscheck >= 1:
                    print(activeteamsnames[activeteamIndex], "has scored", runscheck)
                runscheck=0
                basepicker=0
                print(basestaken, bases)
if totalinnings > maxinnings:
    print("Game end!")            

if activeteamsscores[1] > activeteamsscores[0]: #hometeam wins
    print(activeteamsnames[1],"won the match!", activeteamsscores[1],"-",activeteamsscores[0])
if activeteamsscores[1] < activeteamsscores[0]: #awayteam wins
    print(activeteamsnames[0],"won the match!", activeteamsscores[0],"-",activeteamsscores[1])
if activeteamsscores[0] == activeteamsscores[1]:
    print("It's a tie, wowzers!")