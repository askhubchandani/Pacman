__author__ = 'Ravil'

from pygame import *
import pygame

WHITE = (255, 255, 255)

PACMAN_MOVE_SPEED = 8

PACMAN_GO_RIGHT_ACTION = 0
PACMAN_GO_LEFT_ACTION = 1
PACMAN_GO_UP_ACTION = 2
PACMAN_GO_DOWN_ACTION = 3
PACMAN_STAY_ACTION = 4

UP_ANGLE = 90
RIGHT_ANGLE = 360
LEFT_ANGLE = 180
DOWN_ANGLE = -90


class Pacman(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = image.load("resources/pacman.png")
        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.action = PACMAN_STAY_ACTION

        self.current_angle = 360

    def update(self, action, platforms, dots):
        if action == PACMAN_GO_RIGHT_ACTION:
            self.go_right()
        elif action == PACMAN_GO_DOWN_ACTION:
            self.go_down()
        elif action == PACMAN_GO_LEFT_ACTION:
            self.go_left()
        elif action == PACMAN_GO_UP_ACTION:
            self.go_up()

        self.action = action

        self.collide(platforms)

        self.dots_collide(dots)

    def go_right(self):
        self.rect.x += PACMAN_MOVE_SPEED

        self.rotate(RIGHT_ANGLE)

    def go_up(self):
        self.rect.y -= PACMAN_MOVE_SPEED

        self.rotate(UP_ANGLE)

    def go_down(self):
        self.rect.y += PACMAN_MOVE_SPEED

        self.rotate(DOWN_ANGLE)

    def go_left(self):
        self.rect.x -= PACMAN_MOVE_SPEED

        self.rotate(LEFT_ANGLE)

    def rotate(self, angle):
        rotate_angle = angle - self.current_angle

        self.current_angle += rotate_angle

        self.image = transform.rotate(self.image, rotate_angle)

    def collide(self, platforms):
        for platform in platforms:
            if sprite.collide_rect(self, platform):

                if self.action == PACMAN_GO_RIGHT_ACTION:
                    self.rect.right = platform.rect.left
                elif self.action == PACMAN_GO_LEFT_ACTION:
                    self.rect.left = platform.rect.right
                elif self.action == PACMAN_GO_DOWN_ACTION:
                    self.rect.bottom = platform.rect.top
                elif self.action == PACMAN_GO_UP_ACTION:
                    self.rect.top = platform.rect.bottom

    def dots_collide(self, dots):
        for dot in dots:
            if sprite.collide_rect(self, dot):
                dot.kill()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
