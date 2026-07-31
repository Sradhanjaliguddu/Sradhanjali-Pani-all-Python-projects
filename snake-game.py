import pygame
import random
import sys
from enum import Enum

pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // BLOCK_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // BLOCK_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 180, 0)
GRAY = (40, 40, 40)
YELLOW = (255, 215, 0)
BLUE = (70, 130, 180)

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


def reset_game():
    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    direction = Direction.RIGHT
    next_direction = Direction.RIGHT
    food = spawn_food(snake)
    score = 0
    game_over = False
    paused = False
    return snake, direction, next_direction, food, score, game_over, paused


def spawn_food(snake):
    while True:
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if food not in snake:
            return food


def draw_grid():
    for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (SCREEN_WIDTH, y))


def draw_snake(snake):
    for index, segment in enumerate(snake):
        x, y = segment
        rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
        color = DARK_GREEN if index == 0 else GREEN
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 1)


def draw_food(food):
    x, y = food
    rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
    pygame.draw.rect(screen, RED, rect)
    pygame.draw.rect(screen, BLACK, rect, 1)


def draw_ui(score, game_over, paused):
    font = pygame.font.SysFont("arial", 24, bold=True)
    title_font = pygame.font.SysFont("arial", 36, bold=True)

    title_surface = title_font.render("Snake Game", True, WHITE)
    screen.blit(title_surface, (20, 10))

    score_surface = font.render(f"Score: {score}", True, YELLOW)
    screen.blit(score_surface, (SCREEN_WIDTH - 140, 15))

    hint_font = pygame.font.SysFont("arial", 18)
    hint_surface = hint_font.render("Arrow keys / WASD to move • Space to pause • Enter to restart", True, WHITE)
    screen.blit(hint_surface, (20, SCREEN_HEIGHT - 30))

    if game_over:
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        screen.blit(overlay, (0, 0))

        over_font = pygame.font.SysFont("arial", 48, bold=True)
        over_surface = over_font.render("Game Over", True, RED)
        screen.blit(over_surface, (SCREEN_WIDTH // 2 - over_surface.get_width() // 2, SCREEN_HEIGHT // 2 - 80))

        restart_font = pygame.font.SysFont("arial", 24)
        restart_surface = restart_font.render("Press Enter to play again", True, WHITE)
        screen.blit(restart_surface, (SCREEN_WIDTH // 2 - restart_surface.get_width() // 2, SCREEN_HEIGHT // 2 + 20))

    if paused and not game_over:
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        screen.blit(overlay, (0, 0))

        pause_font = pygame.font.SysFont("arial", 42, bold=True)
        pause_surface = pause_font.render("Paused", True, BLUE)
        screen.blit(pause_surface, (SCREEN_WIDTH // 2 - pause_surface.get_width() // 2, SCREEN_HEIGHT // 2 - 30))


def main():
    snake, direction, next_direction, food, score, game_over, paused = reset_game()
    move_timer = 0
    move_interval = 120

    running = True
    while running:
        clock.tick(30)
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_UP, pygame.K_w) and direction != Direction.DOWN:
                    next_direction = Direction.UP
                elif event.key in (pygame.K_DOWN, pygame.K_s) and direction != Direction.UP:
                    next_direction = Direction.DOWN
                elif event.key in (pygame.K_LEFT, pygame.K_a) and direction != Direction.RIGHT:
                    next_direction = Direction.LEFT
                elif event.key in (pygame.K_RIGHT, pygame.K_d) and direction != Direction.LEFT:
                    next_direction = Direction.RIGHT
                elif event.key == pygame.K_SPACE:
                    if not game_over:
                        paused = not paused
                elif event.key == pygame.K_RETURN and game_over:
                    snake, direction, next_direction, food, score, game_over, paused = reset_game()

        if not game_over and not paused and current_time - move_timer >= move_interval:
            direction = next_direction
            head_x, head_y = snake[0]

            if direction == Direction.UP:
                new_head = (head_x, head_y - 1)
            elif direction == Direction.DOWN:
                new_head = (head_x, head_y + 1)
            elif direction == Direction.LEFT:
                new_head = (head_x - 1, head_y)
            else:
                new_head = (head_x + 1, head_y)

            if (
                new_head[0] < 0
                or new_head[0] >= GRID_WIDTH
                or new_head[1] < 0
                or new_head[1] >= GRID_HEIGHT
                or new_head in snake
            ):
                game_over = True
            else:
                snake.insert(0, new_head)
                if new_head == food:
                    score += 1
                    food = spawn_food(snake)
                    move_interval = max(60, 120 - score * 5)
                else:
                    snake.pop()

            move_timer = current_time

        screen.fill(BLACK)
        draw_grid()
        draw_food(food)
        draw_snake(snake)
        draw_ui(score, game_over, paused)
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

