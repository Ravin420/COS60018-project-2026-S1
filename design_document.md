# Design Document

## Project Title

**Choul Chnam Thmey Quest**

## Project Description

This project is a small educational game created with Python and Pygame. The game is based on Khmer New Year, also known as **Choul Chnam Thmey**.

The player moves around the screen and collects cultural items. After collecting each item, the game shows an image and a short explanation about its cultural meaning. After all items are collected, the player answers a final quiz based on the information they learned.

## Problem Being Addressed

Some people may not know much about Khmer New Year or Cambodian cultural traditions. This game provides a simple and interactive way to introduce selected cultural items and their meaning.

The project does not try to fully represent Cambodian culture. Instead, it uses a few selected examples to support respectful cultural learning.

## Target Users

The target users are students, beginners, or people who want to learn basic information about Khmer New Year through a simple game.

## Main Game Features

* Start screen
* Player movement
* Cultural item collection
* Item images
* Learning box with cultural explanation
* Countdown timer
* Final quiz
* Score system
* High score file saving
* Game over screen

## Cultural Items

The game includes five cultural items:

1. Flower
2. Water Bowl
3. Traditional Food
4. Pagoda
5. Traditional Game

Each item has:

* Name
* Image
* Points
* Position
* Cultural explanation
* Quiz question
* Multiple-choice answers
* Correct answer

## Algorithm / Game Flow

1. Start the game.
2. Show the start screen.
3. Player presses SPACE to begin.
4. Player moves using WASD or arrow keys.
5. Timer starts counting down.
6. Player collects a cultural item.
7. Game shows image and explanation of the item.
8. Player presses SPACE to continue.
9. Repeat until all items are collected.
10. Start final quiz.
11. Player answers quiz questions using A, B, or C.
12. Add points for correct answers.
13. Show final score and high score.
14. Player can restart or quit.

## Pseudocode

```text
START

Load high score
Create game window
Create player
Create cultural items
Set score to 0
Set timer

WHILE game is running:

    Check user input

    IF game state is start:
        Show start screen
        IF player presses SPACE:
            Reset game
            Change state to playing

    ELSE IF game state is playing:
        Start countdown timer
        Move player using keyboard input

        IF timer reaches zero:
            Change state to game over

        FOR each item:
            IF player touches item:
                Mark item as collected
                Add item points to score
                Save item into learned items list
                Change state to learning

    ELSE IF game state is learning:
        Show item image
        Show item cultural meaning
        IF player presses SPACE:
            IF all items are collected:
                Change state to quiz
            ELSE:
                Change state to playing

    ELSE IF game state is quiz:
        Show quiz question based on learned item
        IF player chooses correct answer:
            Add points
        Move to next question

        IF all questions are answered:
            Save high score if needed
            Change state to game over

    ELSE IF game state is game over:
        Show final score
        Show high score
        IF player presses R:
            Restart game
        IF player presses ESC:
            Quit game

END
```

## Flowchart Description

The flowchart for this project follows this structure:

```text
Start
  ↓
Start Screen
  ↓
Press SPACE?
  ↓
Playing State
  ↓
Move Player + Countdown Timer
  ↓
Collect Item?
  ↓
Learning Screen
  ↓
All Items Collected?
  ↓
Final Quiz
  ↓
All Questions Answered?
  ↓
Game Over
  ↓
Restart or Quit
```

## Data Structures Used

The project uses a list of dictionaries to store cultural item information.

Each item dictionary stores:

* `name`
* `image`
* `color`
* `points`
* `position`
* `detail`
* `question`
* `choices`
* `answer`

This makes the code easier to manage because all item information is stored in one structured place.

## File Input / Output

The game uses file input/output to save and load the high score.

* `load_highscore()` reads the saved high score from `highscore.txt`.
* `save_highscore()` writes the new high score into `highscore.txt`.

This demonstrates basic file handling in Python.

## Decomposition

The program is broken into smaller functions to make it easier to read and manage.

Important functions include:

* `load_highscore()`
* `save_highscore()`
* `draw_text()`
* `draw_wrapped_text()`
* `load_image()`
* `create_items()`
* `reset_game()`
* `draw_top_bar()`
* `draw_detail_box()`
* `main()`

## Tools Used

* Python
* Pygame
* VS Code
* GitHub
* GitHub Desktop
* Pydoc

## GitHub Workflow

GitHub was used to track project progress. I used:

* Issues to plan tasks
* Branches to work on changes separately
* Commits to save progress
* Pull requests to merge changes into the main branch

Examples of work completed through GitHub:

* Fixed image loading lag
* Added collection timer
* Added pydoc documentation
* Updated README documentation

## Testing

The game was tested by checking that:

* The game starts correctly
* The player can move
* The timer counts down
* Items can be collected
* Item images appear
* Learning box appears after each collection
* Quiz questions match the item information
* Score updates correctly
* High score saves correctly
* Restart and quit options work

## Responsible and Inclusive Programming

This project uses Cambodian cultural content, so it is important to be respectful. The game only introduces selected Khmer New Year items and does not claim to represent all Cambodian traditions.

The purpose is to create a small educational example that helps players learn about culture through programming.
