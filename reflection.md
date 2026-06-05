# Reflection

## Project Overview

I made a small Pygame for this project named Choul Chnam Thmey Quest, based on Khmer New Year. Players collect cultural items, read brief descriptions, and take a quiz at the end.

I picked this theme because Khmer New Year is personal to me – I'm Cambodian. I just wanted to create a basic game to introduce a bit of Cambodian culture to others.

## Development Process

To start, the game was just about gathering items. But after trying it out, I saw it wasn't really teaching anything. So, I added a learning screen. Now, once a player collects an item, the game shows a picture and explains what it is.

I also tacked on a quiz at the end. This quiz uses info from the item descriptions, letting players learn before they answer the questions.

## Time Log

| Task                            | Time      |
| ------------------------------- | --------- |
| Planning the idea               | 0.3 hours |
| Setting up Python and Pygame    |  1  hours |
| Creating player movement        |  1  hours |
| Adding items and images         | 0.3 hours |
| Adding learning screen and quiz |  1  hours |
| Fixing bugs                     |  3  hours |
| Adding timer and high score     |  2  hours |
| Documentation and testing       |  1  hours |

## What Worked Well

Using a list of dictionaries worked well because I could store each item’s name, image, explanation, quiz question, and answer in one place.

The learning screen also worked well because it made the game more educational.

## What Did Not Work Well

One problem was installing Pygame because my computer used the wrong Python version. I fixed it by using Python 3.12 and a virtual environment.

Another problem was that the game was laggy at first. I found out that images were loading again and again during gameplay. I fixed this by loading the images once at the start.

I also had some indentation errors. This helped me understand that Python spacing is very important.

## Tools I Used

I used:

* VS Code to write code
* Terminal to run the program
* Pygame to make the game
* GitHub Desktop to manage GitHub
* GitHub issues, branches, commits, and pull requests
* Pydoc to create documentation

## What I Learned

I learned how to create a small game using Pygame. I also learned how to use functions, loops, if statements, lists, dictionaries, and file input/output.

I also learned how to use GitHub better. Before this project, I was not confident with branches and pull requests, but now I understand the basic workflow.

## Link to Unit Learning Outcomes

This project was great for practicing how to break problems down into smaller tasks. I made separate functions for loading images, drawing text, generating items, and keeping high scores.

Sequence, selection, and iteration were key in building the game. The game had various states, used if statements, and loops to run continuously.

I also added a high score system using file input/output and stored item info in lists and dictionaries.

Thinking about cultural responsibility was important too, since the game features Cambodian culture. I aimed to keep all the descriptions both simple and respectful.

## AI Statement

I used AI to help brainstorm ideas, understand errors, improve the code structure, and prepare for the demo.

I did not use AI during the demo. I also tested the game myself and made sure I understood the code.

This reflection should be edited in my own words before submission.

## Conclusion

Overall, this project helped me improve my Python, Pygame, debugging, and GitHub skills. It also helped me think about how programming can be used to share cultural knowledge in a respectful way.
