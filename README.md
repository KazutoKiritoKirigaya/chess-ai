# Chess AI

This is a AI Chess game developed using the Pygame library in Python. The game boasts a graphical chessboard where players can engage in matches against an AI opponent that employs simple chess logic.

## Table of Contents

-   [Introduction](#introduction)
-   [Features](#features)
-   [Installation](#installation)
-   [Usage](#usage)
-   [Game Controls](#game-controls)
-   [AI Logic](#ai-logic)

## Introduction

This is an implementation of the game of Chess with a simple AI player. The game provides an interactive graphical interface built using Pygame.

## Features

-   Graphical chessboard with intuitive controls
-   Two-player mode
-   Easy-to-use interface and gameplay
-   AI player for single-player mode, which utilises simple chess logic
-   A plethora of themes
-   Recognises castling moves as valid

## Installation

1. Make sure you have Python installed on your computer. If not, download and install Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Clone this repository to your local machine using Git or download it as a ZIP file and extract it.

3. Open a terminal and navigate to the project's root directory.

4. Install the required dependencies by running the following command:

    ```bash
    pip install pygame
    ```

## Usage

1. After completing the installation steps, navigate to the project directory in a terminal.

2. Run the following command to start the Chess AI game:

    ```bash
    python src/main.py
    ```

3. The game window will open, showing the chessboard and pieces.

4. Use the mouse to click and drag the chess pieces to make your moves.

## Game Controls

-   **Mouse Click:** Select a chess piece and move it by dragging it to the desired square.

-   **Right Click:** Deselect a piece (unselect the current selection).

-   **"T" key:** Changes the board theme.

-   **"R" key:** Restarts the game.

## AI Logic

-   The AI opponent in this chess game uses a simple heuristic-based approach for its moves. It evaluates the board state for all possible moves and selects the move that maximizes its chances of winning while minimizing the opponent's winning chances.

Enjoy playing Chess and have fun challenging the AI opponent! If you encounter any issues or have suggestions for improvements, feel free to open an issue or create a pull request. **Buena suerte!**
