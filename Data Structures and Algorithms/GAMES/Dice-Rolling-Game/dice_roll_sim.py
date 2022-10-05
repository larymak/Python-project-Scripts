import random


Points = []
minPlayer = 2
players = 0
maxscore = 100
DiceNum = 2
gameRound = 0

def setPlayers():
    while True:
        players = input("How many players are playing?\n")
        if players.isdigit():
            players = int(players)
            if minPlayer <= players:
                for i in range(players):
                    Points.append(0)
                return players

def diceroll(player, DiceNum):
    throw = 0
    print("\n\tPlayer {0}s turn:".format(player + 1),end = "")
    for i in range(DiceNum):
        print("\n\tHit Space Bar and Enter to throw die !!",end = " ")
        sp = input()
        if sp == " ":
            die = random.randint(1, 6)
            print("\t \tPlayer {0} has thrown die {1} which landed on {2}".format(player + 1, i + 1, die))
            throw += die
        else:
            print("your turn skipped!!")
    Points[player] += throw
    print("\n \tPlayer {0}s score for this round is : {1}".format(player + 1 , throw))
    print("\tPlayer {0}s total score is now: {1}".format(player + 1, Points[player]))
    return throw

def checkWin(maxscore):
    for player in range(players):
        if (Points[player] >= maxscore):
            print("\nPlayer {0} wins!! Congratulations!!".format(player + 1))
            return True

    return False


if __name__ == "__main__":
    players = setPlayers()
    while True:
        gameRound += 1
        print("\nRound: {0}".format(gameRound))
        for i in range(players):
            diceroll(i, DiceNum)
        print("\nScores after round {0} ".format(gameRound))
        for i in range(players):
            print("Player {0} --> {1}".format(i+1,Points[i]))
        if (checkWin(maxscore)):
            break
