__author__ = 'Ravil'

from agent import *
from pacman import *
from level import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 640
DISPLAY = (WINDOW_WIDTH, WINDOW_HEIGHT)
WINDOW_BACKGROUND_COLOR = (0, 0, 0)

class PacmanGame:

    def __init__(self):
        self.level = Level()

        self.pacman = Pacman(32, 32)

        self.agent = ProblemSolvingAgent(self.pacman, self.level, self.level.dots)

    def main(self):
        pygame.init()
        pygame.display.set_caption("Pacman")

        screen = pygame.display.set_mode(DISPLAY)

        clock = pygame.time.Clock()

        done = False

        while not done:
            # Handling events
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    done = True
            #
            #     if event.type == KEYDOWN and event.key == K_RIGHT:
            #         action = PACMAN_GO_RIGHT_ACTION
            #
            #     if event.type == KEYUP and event.key == K_RIGHT:
            #         action = PACMAN_STAY_ACTION
            #
            #     if event.type == KEYDOWN and event.key == K_LEFT:
            #         action = PACMAN_GO_LEFT_ACTION
            #
            #     if event.type == KEYUP and event.key == K_LEFT:
            #         action = PACMAN_STAY_ACTION
            #
            #     if event.type == KEYDOWN and event.key == K_UP:
            #         action = PACMAN_GO_UP_ACTION
            #
            #     if event.type == KEYUP and event.key == K_UP:
            #         action = PACMAN_STAY_ACTION
            #
            #     if event.type == KEYDOWN and event.key == K_DOWN:
            #         action = PACMAN_GO_DOWN_ACTION
            #
            #     if event.type == KEYUP and event.key == K_DOWN:
            #         action = PACMAN_STAY_ACTION

            # Game logic
            # PACMAN.update(action, LEVEL.platforms, LEVEL.dots)

            self.agent.execute_next_action()

            # Drawing elements
            screen.fill(WINDOW_BACKGROUND_COLOR)

            self.level.draw(screen)

            self.pacman.draw(screen)

            # Update screen
            pygame.display.update()

            # 60 fps
            clock.tick(30)

if __name__ == '__main__':
    PacmanGame().main()


