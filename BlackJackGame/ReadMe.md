# Black Jack Game in Python

A simplified game of 21 made for Python! 

## Card Values
Suits do not affect card values.

2 - 10 all are the same value as the card name.
J, Q, and K are all worth 10.
Aces: If adding 11 would make the score go over 21, then the ace is worth 1. Otherwise, it is worth 11.

## Gameplay
Simply run the script to begin playing. The hand begins with both the player and dealer receiving two cards. The player only sees one of the dealer's cards at the start. The player goes first, choosing to Hit (Press 1) or Stay (Press 0). If the player recieves more than 21 points then they are Bust and have lost the hand. After the player selects Stay, it is then the dealers turn. The dealer Hits until they either receive a higher score than the player (player loses) or Bust (player wins).

## Blackjack
A player gets a 'Blackjack' if they are dealt a card worth 10 and an Ace at the beginning of the hand. This automatically wins the game.


**Note that for the purpose of this script is to allow the user to play a simple hand of Blackjack without some of the higher level parts of the game like betting or splitting doubles. All ties go to the player in this version of the game.

## Demo

![image](https://user-images.githubusercontent.com/48007679/136310729-e354ab8f-c5d5-4eee-bd9c-14857be688d3.png)


  
## Deployment

To deploy this project run

```bash
  python BlackJackGame.py
```

  
