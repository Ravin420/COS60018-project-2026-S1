"""
Choul Chnam Thmey Quest

A small Pygame educational game about Khmer New Year.
The player collects cultural items, reads their meaning, and answers
a final quiz based on the information learned.
"""

import pygame
import os

pygame.init()

# -----------------------------
# Game settings
# -----------------------------

WIDTH = 900
HEIGHT = 650
FPS = 60

PLAYER_SIZE = 40
ITEM_SIZE = 50

WHITE = (255, 255, 255)
BLACK = (20, 20, 20)
GOLD = (235, 190, 60)
RED = (190, 50, 50)
BLUE = (70, 130, 220)
GREEN = (70, 170, 90)
PURPLE = (150, 90, 180)
ORANGE = (230, 130, 50)
LIGHT_YELLOW = (255, 245, 210)
LIGHT_BLUE = (220, 235, 255)
GREY = (230, 230, 230)

HIGHSCORE_FILE = "highscore.txt"

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Choul Chnam Thmey Quest")
clock = pygame.time.Clock()


# -----------------------------
# Cultural item data
# -----------------------------

ITEMS = [
    {
        "name": "Flower",
        "image": "images/flower.jpg",
        "color": PURPLE,
        "points": 10,
        "position": (130, 160),
        "detail": "Flowers are used during Khmer New Year to decorate homes and pagodas. They show beauty, respect, and good wishes.",
        "question": "Flowers are used during Khmer New Year to:",
        "choices": [
            "A. Decorate homes and pagodas",
            "B. Repair motorbikes",
            "C. Build roads"
        ],
        "answer": "A"
    },
    {
        "name": "Water Bowl",
        "image": "images/water.png",
        "color": BLUE,
        "points": 15,
        "position": (370, 180),
        "detail": "Water can symbolise blessing, respect, cleansing, and a fresh start during Khmer New Year.",
        "question": "Water can symbolise:",
        "choices": [
            "A. Anger",
            "B. Blessing and cleansing",
            "C. Shopping"
        ],
        "answer": "B"
    },
    {
        "name": "Traditional Food",
        "image": "images/food.jpg",
        "color": ORANGE,
        "points": 20,
        "position": (620, 160),
        "detail": "Families prepare and share food during Khmer New Year. This helps bring family and community together.",
        "question": "Traditional food is important because it:",
        "choices": [
            "A. Is only decoration",
            "B. Brings family and community together",
            "C. Is used for sport"
        ],
        "answer": "B"
    },
    {
        "name": "Pagoda",
        "image": "images/pagoda.jpg",
        "color": GOLD,
        "points": 25,
        "position": (230, 350),
        "detail": "Many Cambodian families visit pagodas to pray, give respect, and remember good values.",
        "question": "Many Cambodian families visit pagodas to:",
        "choices": [
            "A. Watch movies",
            "B. Pray and give respect",
            "C. Play video games"
        ],
        "answer": "B"
    },
    {
        "name": "Traditional Game",
        "image": "images/game.png",
        "color": GREEN,
        "points": 30,
        "position": (560, 370),
        "detail": "Traditional games are played during Khmer New Year to create fun, friendship, and community connection.",
        "question": "Traditional games help create:",
        "choices": [
            "A. Community connection",
            "B. Isolation",
            "C. Traffic problems"
        ],
        "answer": "A"
    }
]


# -----------------------------
# File I/O functions
# -----------------------------

def load_highscore():
    """Load the high score from a text file."""
    if not os.path.exists(HIGHSCORE_FILE):
        return 0

    try:
        with open(HIGHSCORE_FILE, "r") as file:
            return int(file.read())
    except ValueError:
        return 0


def save_highscore(score):
    """Save the high score to a text file."""
    with open(HIGHSCORE_FILE, "w") as file:
        file.write(str(score))


# -----------------------------
# Helper functions
# -----------------------------

def draw_text(text, size, x, y, color=BLACK, center=True):
    """Draw text on the game screen."""
    font = pygame.font.SysFont("arial", size)
    image = font.render(text, True, color)
    rect = image.get_rect()

    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)

    screen.blit(image, rect)


def draw_wrapped_text(text, size, x, y, max_width, color=BLACK):
    """Draw long text across multiple lines."""
    font = pygame.font.SysFont("arial", size)
    words = text.split()
    line = ""

    for word in words:
        test_line = line + word + " "

        if font.size(test_line)[0] <= max_width:
            line = test_line
        else:
            image = font.render(line, True, color)
            screen.blit(image, (x, y))
            y += size + 8
            line = word + " "

    image = font.render(line, True, color)
    screen.blit(image, (x, y))


def load_image(path, size):
    """Load and resize an image. Return None if the image is missing."""
    if os.path.exists(path):
        image = pygame.image.load(path)
        return pygame.transform.scale(image, size)

    return None


def create_items():
    """Create item rectangles and collected status."""
    game_items = []

    for item in ITEMS:
        new_item = item.copy()
        x, y = item["position"]
        new_item["rect"] = pygame.Rect(x, y, ITEM_SIZE, ITEM_SIZE)
        new_item["collected"] = False
        game_items.append(new_item)

    return game_items


def reset_game():
    """Reset the game variables."""
    player = pygame.Rect(WIDTH // 2, HEIGHT // 2, PLAYER_SIZE, PLAYER_SIZE)
    items = create_items()
    learned_items = []
    score = 0
    quiz_index = 0
    current_item = None

    return player, items, learned_items, score, quiz_index, current_item


def draw_top_bar(score, learned_items, highscore):
    """Draw the score bar at the top."""
    pygame.draw.rect(screen, GOLD, (0, 0, WIDTH, 80))
    draw_text(f"Score: {score}", 24, 100, 30)
    draw_text(f"Collected: {len(learned_items)} / {len(ITEMS)}", 24, WIDTH // 2, 30)
    draw_text(f"High Score: {highscore}", 24, WIDTH - 130, 30)


def draw_detail_box(item):
    """Draw the learning box for the collected item."""
    box = pygame.Rect(40, 500, 820, 120)

    pygame.draw.rect(screen, LIGHT_BLUE, box)
    pygame.draw.rect(screen, BLUE, box, 3)

    draw_text(f"Collected: {item['name']}", 24, 60, 515, RED, center=False)
    draw_wrapped_text(item["detail"], 21, 60, 555, 760)
    draw_text("Press SPACE to continue", 20, 650, 600, BLUE, center=False)


# -----------------------------
# Main game loop
# -----------------------------

def main():
    """Run the game."""
    highscore = load_highscore()

    player, items, learned_items, score, quiz_index, current_item = reset_game()

    game_state = "start"
    feedback = ""

    running = True

    while running:
        clock.tick(FPS)
        screen.fill(WHITE)

        # -----------------------------
        # Event handling
        # -----------------------------

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if game_state == "start":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    player, items, learned_items, score, quiz_index, current_item = reset_game()
                    feedback = ""
                    game_state = "playing"

            elif game_state == "learning":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    if len(learned_items) == len(ITEMS):
                        game_state = "quiz"
                    else:
                        game_state = "playing"

            elif game_state == "quiz":
                if event.type == pygame.KEYDOWN:
                    answer = None

                    if event.key == pygame.K_a:
                        answer = "A"
                    elif event.key == pygame.K_b:
                        answer = "B"
                    elif event.key == pygame.K_c:
                        answer = "C"

                    if answer is not None:
                        quiz_item = learned_items[quiz_index]

                        if answer == quiz_item["answer"]:
                            score += 50
                            feedback = "Correct! +50 points"
                        else:
                            feedback = f"Incorrect. Correct answer: {quiz_item['answer']}"

                        quiz_index += 1

                        if quiz_index >= len(learned_items):
                            if score > highscore:
                                highscore = score
                                save_highscore(highscore)

                            game_state = "game_over"

            elif game_state == "game_over":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        player, items, learned_items, score, quiz_index, current_item = reset_game()
                        feedback = ""
                        game_state = "playing"

                    elif event.key == pygame.K_ESCAPE:
                        running = False

        # -----------------------------
        # Start screen
        # -----------------------------

        if game_state == "start":
            screen.fill(LIGHT_YELLOW)

            draw_text("Choul Chnam Thmey Quest", 44, WIDTH // 2, 120, RED)
            draw_text("Khmer New Year Cultural Learning Game", 28, WIDTH // 2, 180)
            draw_text("Collect cultural items, read the information, then answer the final quiz.", 23, WIDTH // 2, 260)
            draw_text("Use WASD or arrow keys to move.", 24, WIDTH // 2, 320)
            draw_text("Press SPACE to start", 30, WIDTH // 2, 420, BLUE)
            draw_text(f"High Score: {highscore}", 24, WIDTH // 2, 500, GREEN)

        # -----------------------------
        # Playing screen
        # -----------------------------

        elif game_state == "playing":
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                player.x -= 5
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                player.x += 5
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                player.y -= 5
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                player.y += 5

            player.x = max(0, min(WIDTH - PLAYER_SIZE, player.x))
            player.y = max(80, min(HEIGHT - PLAYER_SIZE, player.y))

            draw_top_bar(score, learned_items, highscore)
            draw_text("Collect an item to learn about it.", 22, WIDTH // 2, 105, BLUE)

            # Draw items
            for item in items:
                if not item["collected"]:
                    small_image = load_image(item["image"], (60, 60))

                    if small_image:
                        screen.blit(small_image, (item["rect"].x - 5, item["rect"].y - 5))
                    else:
                        pygame.draw.rect(screen, item["color"], item["rect"])

                    draw_text(item["name"], 16, item["rect"].centerx, item["rect"].y - 15)

            # Draw player
            pygame.draw.rect(screen, GREEN, player)
            draw_text("Player", 16, player.centerx, player.y - 15)

            # Default learning box
            box = pygame.Rect(40, 500, 820, 120)
            pygame.draw.rect(screen, GREY, box)
            pygame.draw.rect(screen, BLACK, box, 2)
            draw_text("Learning Box", 24, 60, 515, RED, center=False)
            draw_text("Collect an item. Its cultural meaning will appear here.", 21, 60, 555, BLACK, center=False)

            # Collision check
            for item in items:
                if not item["collected"] and player.colliderect(item["rect"]):
                    item["collected"] = True
                    current_item = item
                    learned_items.append(item)
                    score += item["points"]
                    game_state = "learning"
                    break

        # -----------------------------
        # Learning screen
        # -----------------------------

        elif game_state == "learning":
            screen.fill(WHITE)

            draw_top_bar(score, learned_items, highscore)

            # Draw remaining items
            for item in items:
                if not item["collected"]:
                    small_image = load_image(item["image"], (60, 60))

                    if small_image:
                        screen.blit(small_image, (item["rect"].x - 5, item["rect"].y - 5))
                    else:
                        pygame.draw.rect(screen, item["color"], item["rect"])

                    draw_text(item["name"], 16, item["rect"].centerx, item["rect"].y - 15)

            # Draw player
            pygame.draw.rect(screen, GREEN, player)
            draw_text("Player", 16, player.centerx, player.y - 15)

            # Show selected item title
            draw_text(current_item["name"], 36, WIDTH // 2, 130, RED)

            # Show selected item image
            image = load_image(current_item["image"], (180, 180))

            if image:
                screen.blit(image, (WIDTH // 2 - 90, 170))
            else:
                pygame.draw.rect(screen, current_item["color"], (WIDTH // 2 - 90, 170, 180, 180))
                draw_text("Image missing", 22, WIDTH // 2, 260, WHITE)

            # Show item explanation
            draw_detail_box(current_item)

        # -----------------------------
        # Quiz screen
        # -----------------------------

        elif game_state == "quiz":
            screen.fill(LIGHT_YELLOW)

            quiz_item = learned_items[quiz_index]

            draw_text("Final Pop Quiz", 42, WIDTH // 2, 70, RED)
            draw_text(f"Question {quiz_index + 1} of {len(learned_items)}", 24, WIDTH // 2, 120, BLUE)
            draw_text(f"Based on: {quiz_item['name']}", 24, WIDTH // 2, 165, GREEN)

            draw_wrapped_text(quiz_item["question"], 28, 120, 220, 680)

            y = 330
            for choice in quiz_item["choices"]:
                draw_text(choice, 24, WIDTH // 2, y)
                y += 55

            draw_text("Press A, B, or C to answer.", 26, WIDTH // 2, 560, BLUE)

        # -----------------------------
        # Game over screen
        # -----------------------------

        elif game_state == "game_over":
            screen.fill(LIGHT_YELLOW)

            draw_text("Game Completed!", 46, WIDTH // 2, 110, RED)
            draw_text(f"Final Score: {score}", 32, WIDTH // 2, 200)
            draw_text(f"High Score: {highscore}", 32, WIDTH // 2, 250, GREEN)

            if feedback:
                draw_text(feedback, 22, WIDTH // 2, 315, BLUE)

            draw_text("You collected all cultural items and completed the quiz.", 24, WIDTH // 2, 390)
            draw_text("Press R to restart or ESC to quit.", 28, WIDTH // 2, 500, BLUE)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()