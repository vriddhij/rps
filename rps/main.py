import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock, Paper, Scissors")

# Load images
rock_img = pygame.image.load(os.path.join("images", "rock.png"))
paper_img = pygame.image.load(os.path.join("images", "paper.png"))
scissors_img = pygame.image.load(os.path.join("images", "sci.png"))

# Load sounds
win_sound = pygame.mixer.Sound(os.path.join("sounds", "win.mp3"))
lose_sound = pygame.mixer.Sound(os.path.join("sounds", "lose.mp3"))
tie_sound = pygame.mixer.Sound(os.path.join("sounds", "tie.mp3"))

# Map images to choices
choices = {
    "rock": rock_img,
    "paper": paper_img,
    "scissors": scissors_img
}

# Function to display choices
def display_choices(player_choice, computer_choice):
    win.blit(choices[player_choice], (150, 200))
    win.blit(choices[computer_choice], (450, 200))

# Function to display text
def display_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    win.blit(text_surface, (x, y))

# Main game loop
def main():
    clock = pygame.time.Clock()
    FPS = 1
    font = pygame.font.Font(None, 36)
    running = True

    while running:
        win.fill((255, 255, 255))

        display_text("Choose: Rock, Paper, or Scissors", font, (0, 0, 0), 200, 50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                if event.key in [pygame.K_r, pygame.K_p, pygame.K_s]:
                    player_choice = ""
                    if event.key == pygame.K_r:
                        player_choice = "rock"
                    elif event.key == pygame.K_p:
                        player_choice = "paper"
                    elif event.key == pygame.K_s:
                        player_choice = "scissors"

                    computer_choices = ["rock", "paper", "scissors"]
                    computer_choice = random.choice(computer_choices)

                    display_choices(player_choice, computer_choice)

                    if player_choice == computer_choice:
                        display_text("It's a tie!", font, (0, 0, 0), 350, 400)
                        tie_sound.play()
                    elif (
                        (player_choice == "rock" and computer_choice == "scissors")
                        or (player_choice == "paper" and computer_choice == "rock")
                        or (player_choice == "scissors" and computer_choice == "paper")
                    ):
                        display_text("You win!", font, (0, 255, 0), 350, 400)
                        win_sound.play()
                    else:
                        display_text("You lose!", font, (255, 0, 0), 350, 400)
                        lose_sound.play()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
