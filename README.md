# Choul Chnam Thmey Quest

## Project Overview

**Choul Chnam Thmey Quest** is a small Python Pygame educational game about Khmer New Year, also known as **Choul Chnam Thmey**.

The player moves around the screen, collects cultural items, reads short explanations about each item, and then answers a final quiz based on what they learned.

The aim of this project is not to fully represent Cambodian culture, but to respectfully introduce selected Khmer New Year traditions through a simple interactive game.

## Project Purpose

This project shows how programming can be used to support cultural learning. It connects to a Cambodian cultural perspective by using Khmer New Year as the main theme.

The game encourages players to learn through interaction. Instead of only reading information, players collect items, view their meaning, and apply that knowledge in a quiz.

## Features

* Player movement using arrow keys or WASD
* Khmer New Year cultural items
* Images for each item
* Learning box after each item is collected
* Final quiz based on collected item information
* Score system
* High score saving using file input/output
* Countdown timer during item collection
* Simple game states: start, playing, learning, quiz, and game over

## Cultural Items Included

The game includes the following cultural items:

* Flower
* Water Bowl
* Traditional Food
* Pagoda
* Traditional Game

Each item has a short explanation and a related quiz question.

## Tools and Libraries

This project uses:

* Python
* Pygame
* VS Code
* GitHub
* GitHub Desktop

## Installation

Make sure Python is installed on your computer.

Install Pygame:

```bash
pip install pygame
```

## How to Run the Game

Run this command in the project folder:

```bash
python main.py
```

If using a virtual environment, activate it first or run the Python file using the virtual environment interpreter.

## Controls

| Key        | Action                                      |
| ---------- | ------------------------------------------- |
| Arrow Keys | Move player                                 |
| WASD       | Move player                                 |
| SPACE      | Start game / continue after learning screen |
| A, B, C    | Answer quiz questions                       |
| R          | Restart after game over                     |
| ESC        | Quit game                                   |

## Game Flow

1. The player starts the game.
2. The player moves around and collects cultural items.
3. After collecting an item, the game shows the item image and cultural meaning.
4. The player presses SPACE to continue.
5. After all items are collected, the final quiz starts.
6. The quiz questions are based on the collected item information.
7. The final score is shown at the end.

## File Structure

```text
COS60018-project-2026-S1/
│
├── main.py
├── README.md
├── .gitignore
└── images/
    ├── flower.jpg
    ├── food.jpg
    ├── game.png
    ├── pagoda.jpg
    └── water.png
```

## GitHub Workflow

GitHub was used to manage the project development. The project includes issues, branches, commits, and pull requests.

Examples of GitHub workflow used:

* Created an initial project repository
* Created an issue to fix image loading lag
* Created a branch for fixing image loading lag
* Created a pull request and merged it into main
* Created an issue to add a collection timer
* Created a branch for the timer feature
* Created a pull request and merged it into main

This helped track progress and manage changes more professionally.

## Programming Concepts Demonstrated

This project demonstrates:

* Sequence
* Selection using `if`, `elif`, and `else`
* Iteration using loops
* Functions
* Lists and dictionaries
* File input/output
* Game states
* Basic debugging
* Use of an external Python library

## Responsible Programming Consideration

Because this project uses cultural content, it is important to be respectful. The game only introduces selected Khmer New Year items in a simple way. It does not claim to fully represent Cambodian culture or speak for all Cambodian people.

The cultural information is used to support basic learning and awareness through a beginner-friendly game.

## Future Improvements

Possible future improvements include:

* Adding background music
* Adding more Khmer New Year items
* Adding Khmer language text
* Improving the character design
* Adding more levels
* Adding sound effects
* Improving the quiz feedback system
