import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1280, 720
FPS = 60
WHITE = (255, 255, 255)
PLAYER_SPEED = 8

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Endless Runner")

# Load images
player_img = pygame.Surface((50, 50))
player_img.fill((0, 128, 255))
player_rect = player_img.get_rect(midbottom=(WIDTH // 2, HEIGHT - 50))

obstacle_img = pygame.Surface((50, 50))
obstacle_img.fill((255, 0, 0))
obstacles = []

clock = pygame.time.Clock()

def draw_text(text, size, color, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def run_game():
    global obstacles  # Declare obstacles as global
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        player_rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * PLAYER_SPEED

        # Spawn new obstacles
        if random.randint(1, 100) <= 5:
            obstacle_rect = obstacle_img.get_rect(midtop=(random.randint(0, WIDTH - 50), 0))
            obstacles.append(obstacle_rect)

        # Move and draw obstacles
        for obstacle in obstacles:
            obstacle.y += 5
            screen.blit(obstacle_img, obstacle)
            if obstacle.colliderect(player_rect):
                draw_text("Game Over", 64, WHITE, WIDTH // 2, HEIGHT // 2)
                pygame.display.flip()
                pygame.time.wait(2000)
                obstacles = []  # Reset obstacles
                return  # End the game

        # Remove off-screen obstacles
        obstacles = [obstacle for obstacle in obstacles if obstacle.y < HEIGHT]

        # Draw player
        screen.fill((0, 0, 0))
        screen.blit(player_img, player_rect)

        # Draw score
        score += 1
        draw_text(f"Score: {score}", 36, WHITE, WIDTH // 2, 50)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    while True:
        run_game()
