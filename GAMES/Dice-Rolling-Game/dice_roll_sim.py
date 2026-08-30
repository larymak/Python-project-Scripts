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

def diceroll(player, DiceNum, points):
    throw = 0
    print(f"\n\tPlayer {player + 1}'s turn:")
    for i in range(DiceNum):
        input("\n\tPress Enter to throw die!")
        die = random.randint(1, 6)
        print(f"\tPlayer {player + 1} rolled a {die}")
        throw += die
    points[player] += throw

    print(f"\n\tPlayer {player + 1}'s score this round: {throw}")
    print(f"\tPlayer {player + 1}'s total score: {points[player]}")

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
