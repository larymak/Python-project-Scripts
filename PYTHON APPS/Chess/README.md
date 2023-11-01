# Two Player Chess

This is a simple two-player chess game built in Python. It uses the standard rules of chess and allows two players to play against each other on the same computer.

## Installation

To install and run the game, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Install pygame , a Python library for creating games, by running the following command:

    ```
    pip install pygame
    ```

4. Start the game by running the following command:

    ```
    python main.py
    ```

## How to Play

The game is played using the standard rules of chess. Each player takes turns moving their pieces on the board until one player is in checkmate or a draw is declared.

To move a piece, select it with your mouse and drag it to the desired square. If the move is legal, the piece will be placed on the new square. If the move is not legal, the piece will return to its original position.

## Features

- `En Passant`: Special pawn capture move inclusion
- `Castling`: Ability to perform the castling maneuver
- `Checkmate and Stalemate Detection`: Logic for detecting game-ending states
- `User Interface`: Graphical representation of the board with mouse controls
- `Standard Chess Rules`: Adherence to traditional chess rules
- `Two-Player Mode`: Enable two human players to compete on the same device

## Code Overview

The game is built using two Python files:

- `engine.py`: This file contains the logic for the chess game, including the rules for moving pieces and checking for checkmate and stalemate.
- `main.py`: This file contains the user interface for the game, including the graphical representation of the board and the mouse controls for moving pieces.

Build with :heart: by [Purna Shrestha](https://github.com/purnasth)