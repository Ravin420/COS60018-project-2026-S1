# Design Document

## Project Title

**Choul Chnam Thmey Quest**

## Project Overview

My project is a small educational game made with Python and Pygame. The game is about Khmer New Year, which is called **Choul Chnam Thmey** in Khmer.

In the game, the player moves around the screen and collects cultural items. After collecting an item, the game shows a picture and a short explanation about that item. At the end, the player answers a quiz based on what they learned.

The game is not meant to explain all of Cambodian culture. It only introduces a few simple Khmer New Year items in an easy and respectful way.

## Purpose of the Project

The purpose of this project is to show how programming can be used for cultural learning.

I chose Khmer New Year because I am Cambodian, so this topic is personally meaningful to me. I wanted to make something simple that can help other people learn a little bit about Cambodian culture through a game.

Instead of only reading information, the player can interact with the items, look at images, and answer questions. This makes the learning process more active and interesting.

## Cultural Context

The game is based on Khmer New Year traditions. I included five cultural items:

* Flower
* Water Bowl
* Traditional Food
* Pagoda
* Traditional Game

Each item has a short explanation. For example, flowers are used for decoration and respect, while water can represent blessing and cleansing. Traditional food and games also show family and community connection.

I tried to keep the explanations simple because the game is designed for beginner players.

## Assumptions

For this project, I made a few assumptions:

* The player can use a keyboard.
* The player can understand simple English.
* The game only teaches basic information.
* The game does not represent every Khmer New Year tradition.
* The images are used only to help players understand the items visually.

## Problem and Requirements

The problem I wanted to address is that cultural learning can sometimes feel boring if it is only text-based. A simple game can make learning more interactive.

The main requirements of the game are:

* The player can move around the screen.
* The player can collect items.
* Each item shows an image and explanation.
* The game has a countdown timer.
* The quiz is based on the collected item information.
* The game has a score and high score.
* The program uses file input/output.
* The program uses Pygame.

## Main Features

The main features are:

* Start screen
* Player movement
* Item collection
* Learning screen
* Item images
* Countdown timer
* Final quiz
* Score system
* High score saving
* Game over screen

## Game Flow

The game uses different states:

1. Start
2. Playing
3. Learning
4. Quiz
5. Game over

The player starts from the start screen. After pressing SPACE, the player begins collecting items. When an item is collected, the game changes to the learning screen. After all items are collected, the quiz begins. After the quiz, the game shows the final score.

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

    Check player input

    IF game state is start:
        Show start screen
        IF player presses SPACE:
            Reset game
            Change to playing state

    ELSE IF game state is playing:
        Count down timer
        Move player using keyboard

        IF player touches an item:
            Mark item as collected
            Add points
            Save item for quiz
            Show learning screen

        IF timer reaches zero:
            Change to game over

    ELSE IF game state is learning:
        Show item image
        Show item explanation
        IF player presses SPACE:
            IF all items are collected:
                Change to quiz state
            ELSE:
                Return to playing state

    ELSE IF game state is quiz:
        Show question based on collected item
        Check answer
        Add points if correct

        IF all questions are answered:
            Save high score
            Change to game over

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

```text
Start
  ↓
Start Screen
  ↓
Press SPACE
  ↓
Playing State
  ↓
Move Player and Timer Counts Down
  ↓
Collect Item
  ↓
Learning Screen
  ↓
Show Image and Explanation
  ↓
All Items Collected?
  ↓
If No: Back to Playing
  ↓
If Yes: Final Quiz
  ↓
Answer Questions
  ↓
Game Over
  ↓
Restart or Quit
```

## Code Design

I used functions to keep the code organised. This makes the program easier to read and easier to fix.

Some important functions are:

* `load_highscore()` — loads the saved high score
* `save_highscore()` — saves the high score
* `draw_text()` — draws text on the screen
* `draw_wrapped_text()` — draws longer text in multiple lines
* `load_image()` — loads and resizes images
* `create_items()` — creates the cultural items
* `reset_game()` — resets the game
* `draw_top_bar()` — shows score, timer, and high score
* `draw_detail_box()` — shows item explanation
* `main()` — runs the main game loop

## Data Structures

I used a list of dictionaries to store the cultural items.

Each dictionary stores information like:

* item name
* image path
* position
* points
* explanation
* quiz question
* answer choices
* correct answer

This design is useful because each item’s explanation and quiz question are stored together. This makes sure the quiz is related to what the player learned.

## File Input and Output

The game uses file input/output for the high score system.

The function `load_highscore()` reads the high score from `highscore.txt`.

The function `save_highscore()` writes the new high score to `highscore.txt`.

This means the game can remember the best score even after the program closes.

## Design Decisions

### Using Pygame

I used Pygame because this project is a small game. Pygame is useful for creating a window, drawing images, handling keyboard input, and making a game loop.

### Using a Learning Screen

At first, collecting items was not educational enough. I changed the design so that each item shows its picture and explanation after being collected. This makes the game more connected to cultural learning.

### Quiz Based on Collected Items

The quiz questions are based on the item details shown earlier. This makes the quiz fair because players can learn the answer before being tested.

### Preloading Images

The game was laggy at first because images were loading many times during gameplay. I fixed this by loading images once when the items are created. This made the movement smoother.

### Adding a Timer

I added a timer because the game felt too easy without it. The timer gives the player a simple challenge while collecting items.

## Testing

I tested the game by checking:

* The game opens without errors.
* The player can move.
* The player stays inside the screen.
* Images appear correctly.
* Items can be collected.
* The learning box appears.
* The quiz questions match the item information.
* The timer counts down.
* The score updates.
* The high score saves.
* Restart and quit work.

## GitHub Workflow

I used GitHub and GitHub Desktop during the project.

I uploaded the project to GitHub and used issues, branches, commits, and pull requests.

Some examples of tasks I tracked were:

* fixing image loading lag
* adding a collection timer
* updating README documentation
* adding pydoc documentation
* adding this design document

Using GitHub helped me keep track of my changes and made the project workflow more organised.

## Responsible Programming

Because this project uses cultural content, I tried to keep it respectful. I did not try to represent all Cambodian traditions. I only used a few selected items as examples.

This project helped me understand that programmers need to think carefully when using culture in software. Even a small game should avoid stereotypes and should explain things clearly.

## Limitations

The game has some limitations:

* It only has five items.
* It only has one level.
* The explanations are short.
* The graphics are simple.
* The game is only in English.
* There is no sound or music.

## Future Improvements

In the future, I could improve the game by adding:

* Khmer language text
* background music
* sound effects
* more cultural items
* more quiz questions
* better character design
* more levels

## Conclusion

Overall, this project is a small but complete Pygame game. It combines basic programming skills with cultural learning.

Through this project, I practised using functions, loops, conditionals, lists, dictionaries, file input/output, Pygame, VS Code, and GitHub.

The game also helped me think about how programming can be used responsibly to share cultural knowledge in a simple way.

## References

Python Software Foundation. (2026). *pydoc — Documentation generator and online help system*. https://docs.python.org/3/library/pydoc.html

Pygame developers. (2023). *Pygame documentation*. https://www.pygame.org/docs/

Wikipedia contributors. (2026). *Cambodian New Year*. Wikipedia. https://en.wikipedia.org/wiki/Cambodian_New_Year
