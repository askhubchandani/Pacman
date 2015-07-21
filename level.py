__author__ = 'Ravil'

import pygame


class Level:
    def __init__(self):
        self.level = [
            "-------------------------",
            "-                       -",
            "------    -             -",
            "-         -             -",
            "-         -     ---------",
            "-         -     -       -",
            "-         -------       -",
            "-       --      -       -",
            "-               -   -   -",
            "-      --       -   -   -",
            "-    -          -   -   -",
            "-    -          -   --  -",
            "-       -       -    -  -",
            "-         -------    - --",
            "-               -    -  -",
            "-  -            -    --*-",
            "-               -    ----",
            "-           -----       -",
            "-                       -",
            "-------------------------"]

        state = (2, 3)

        row = state[0]
        column = state[1] + 1

        new_state = (row, column)

        print(self.level[new_state[0]][new_state[1]])

        self.platforms = []

        self.dots = []

        self.platforms_entities = pygame.sprite.Group()

        x = 0
        y = 0

        for row in self.level:
            for item in row:
                if item == "-":
                    pf = Platform(x, y)

                    self.platforms.append(pf)

                    self.platforms_entities.add(pf)

                if item == "*":
                    dot = Dot(x, y)

                    self.dots.append(dot)

                    self.platforms_entities.add(dot)

                x += PLATFORM_WIDTH

            y += PLATFORM_HEIGHT
            x = 0

    def draw(self, screen):
        self.platforms_entities.draw(screen)


PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = (65, 105, 225)

class Platform(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(PLATFORM_COLOR)

        self.rect = pygame.Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

WHITE = (255, 255, 255)
DOT_COLOR = (255, 255, 224)

class Dot(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.ellipse(self.image, DOT_COLOR, [12, 12, 8, 8])

        self.rect = pygame.Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
