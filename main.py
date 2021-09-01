import pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards

# from pygame.locals import (
#     K_UP,
#     K_DOWN,
#     K_LEFT,
#     K_RIGHT,
#     K_ESCAPE,
#     KEYDOWN,
#     QUIT
# )


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 750


class field:
    field_left = 20
    field_up = 20
    field_width = SCREEN_WIDTH - field_left * 2 - 100
    field_height = SCREEN_HEIGHT - field_up * 2

    def draw_field(self, screen):
        pygame.draw.rect(screen, (60, 60, 60), (self.field_left, self.field_up, self.field_width, self.field_height), 1)
        pygame.draw.rect(screen, (60, 60, 60), (self.field_left * 2 + self.field_width,
                                                self.field_up, 80, self.field_height), 1)


pygame.init()
# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
screen.fill((220, 220, 220))

field = field()

field.draw_field(screen)

# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Flip the display
    pygame.display.flip()

pygame.quit()
