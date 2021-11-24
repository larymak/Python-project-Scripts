import random as rn
deck = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
suit = ['spade' , 'heart' , 'diamond' , 'club']
arr = []
pl = []
dl = []

# Check Blackjack__________________________________________
def check_Twenty_One(s):
    if s==21:
        return True
    else:
        return False

# Check Bust_______________________________________________
def Bust(s):
    if s>21:
        return True
    else:
        return False

# Check Ace is 1 or 11_____________________________________
def check_For_Ace(s):
    if (s+11)<=21:
        return 11
    else:
        return 1

# Adjust the sum___________________________________________
def check_sum(s):
    if s < 21:
        return s

    for i in range(len(pl)-1,-1,-1):
        if pl[i] == 'A':
            s -= 10
            break
    return s

# creating a well shuffled pack of cards___________________
def startGame():
    print("Welcome to the BlackJack Game:\n")
    for i in suit:
        for j in deck:
            arr.append([i,j])
    rn.shuffle(arr)
    
    pl.append(arr[0])
    pl.append(arr[1])
    dl.append(arr[2])
    dl.append(arr[3])
    
    print(f'\nDealer draws {dl[0]} and [xxxxxx,xx]\n')
    s = 0
    for i in range(0,2):
        if arr[i][1] == 'J' or arr[i][1] == 'K' or arr[i][1] == 'Q':
            s += 10
        elif arr[i][1] == 'A':
            s += check_For_Ace(s)
        else:
            s += arr[i][1]
    return s

# player's chance__________________________________________
def playersTurn(s):
    print("You are currently at " + str(s))
    print(f'Current Hand: {pl}')

    s = check_sum(s)

    if (check_Twenty_One(s)):
        #Check Blackjack_______________________________________
        if len(pl) == 2:
            print("Hurray......It's a BLACKJACK....You Won\n")
        #Check if player made 21_______________________________
        else:
            print("Awesome!!!......You made 21!....You Won\n")
        return 2
    elif (Bust(s)):
        print("You got Bust.....You Lost\n")
        return 3

    while(1):
        i = int(input("\nHit(Press 1) or Stay(Press 0): "))
        if i==1 or i==0:
            return i
        else:
            print("Enter a valid number....\n")

if __name__ == '__main__':
    s = startGame()
    c = j = 0
    for i in range(4,len(arr)):
        
        j = playersTurn(s)
        if j == 2 or j == 3:
            j = i
            break
        elif j == 0:
            j = i
            c = 100
            break
        print(f'You draw {arr[i]}\n')

        if arr[i][1] == 'J' or arr[i][1] == 'K' or arr[i][1] == 'Q':
            c = 10
        elif arr[i][1] == 'A':
            c = check_For_Ace(s)
        else:
            c = arr[i][1]
        s += c
        pl.append(arr[i])

    if c == 100:
        sp = s
        s = 0
        for i in range(2,4):
            if arr[i][1] == 'J' or arr[i][1] == 'K' or arr[i][1] == 'Q':
                s += 10
            elif arr[i][1] == 'A':
                s += check_For_Ace(s)
            else:
                s += arr[i][1]
        print(f"\nDealer's second card was {dl[1]}")

        for i in range(j,len(arr)):
            print(f"\nDealer is at {s}")
            print(f"\nDealer's current hand: {dl}\n")

            s = check_sum(s)
            if (check_Twenty_One(s)):
                if len(dl) == 2:
                    print("Dealer got a BlackJack and won the Game\nYou Lost\n")
                else:
                    print("Dealer made 21 and won the Game\nBetter Luck Next Time!\n")
                break
            elif (Bust(s)):
                print("Dealer got Busted\nYou Won\n")
                break
            elif (sp < s):
                print("Dealer Won the Game\n")
                break

            print(f"Dealer draws {arr[i]}")
            dl.append(arr[i])
            if arr[i][1] == 'J' or arr[i][1] == 'K' or arr[i][1] == 'Q':
                s += 10
            elif arr[i][1] == 'A':
                s += check_For_Ace(s)
            else:
                s += arr[i][1]
