"""
SNAKE GAME - built with pygame
================================
Teaching sequence (build it in this order with students):
  STAGE 1: Draw a window and a single moving square
  STAGE 2: Control direction with arrow keys
  STAGE 3: Add a food dot; snake grows when it eats food
  STAGE 4: Detect wall collision and self-collision -> Game Over
  STAGE 5: Add a score display

Install pygame first:  pip install pygame --break-system-packages
"""

import pygame
import random
import sys

# ----------------------------
# SETUP (Stage 1)
# ----------------------------
pygame.init()

CELL_SIZE = 20          # size of one grid square (snake segment / food)
GRID_WIDTH = 30          # how many cells wide
GRID_HEIGHT = 20         # how many cells tall
WIDTH = CELL_SIZE * GRID_WIDTH
HEIGHT = CELL_SIZE * GRID_HEIGHT

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 120, 0)
RED = (200, 0, 0)
BLACK = (20, 20, 20)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 24)


def draw_grid_square(pos, color):
    """Draws one square on the grid. pos is (x, y) in grid coordinates, not pixels."""
    rect = pygame.Rect(pos[0] * CELL_SIZE, pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, BLACK, rect, 1)  # thin border so segments are visible


def random_food_position(snake_body):
    """Pick a random grid cell that isn't currently occupied by the snake."""
    while True:
        pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if pos not in snake_body:
            return pos


def show_game_over(score):
    screen.fill(BLACK)
    msg = font.render(f"Game Over! Score: {score}  (Press R to restart, Q to quit)", True, WHITE)
    screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()


def main():
    # ----------------------------
    # STATE (Stage 2 & 3): snake is a LIST of grid positions.
    # snake_body[0] is the head. This list is the core data structure
    # students should understand -- moving = add new head, remove tail.
    # ----------------------------
    snake_body = [(10, 10), (9, 10), (8, 10)]
    direction = (1, 0)   # moving right: (dx, dy)
    next_direction = direction
    food_pos = random_food_position(snake_body)
    score = 0
    game_over = False

    MOVE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(MOVE_EVENT, 120)  # controls snake speed (ms per move)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # Prevent the snake from reversing directly into itself
                if event.key == pygame.K_UP and direction != (0, 1):
                    next_direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction != (0, -1):
                    next_direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction != (1, 0):
                    next_direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                    next_direction = (1, 0)
                elif game_over and event.key == pygame.K_r:
                    return main()  # restart
                elif game_over and event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

            if event.type == MOVE_EVENT and not game_over:
                direction = next_direction
                head_x, head_y = snake_body[0]
                new_head = (head_x + direction[0], head_y + direction[1])

                # ----------------------------
                # STAGE 4: collision detection
                # ----------------------------
                hit_wall = not (0 <= new_head[0] < GRID_WIDTH and 0 <= new_head[1] < GRID_HEIGHT)
                hit_self = new_head in snake_body

                if hit_wall or hit_self:
                    game_over = True
                else:
                    snake_body.insert(0, new_head)  # add new head

                    # ----------------------------
                    # STAGE 3: eating food = grow (skip removing tail)
                    # ----------------------------
                    if new_head == food_pos:
                        score += 1
                        food_pos = random_food_position(snake_body)
                    else:
                        snake_body.pop()  # remove tail so length stays same

        # ----------------------------
        # DRAW EVERYTHING
        # ----------------------------
        if game_over:
            show_game_over(score)
            continue

        screen.fill(BLACK)
        for i, segment in enumerate(snake_body):
            color = DARK_GREEN if i == 0 else GREEN  # head is a darker shade
            draw_grid_square(segment, color)
        draw_grid_square(food_pos, RED)

        # STAGE 5: score display
        score_surface = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_surface, (5, 5))

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
