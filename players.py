import pygame
pygame.init()


class Players:
    start = False

    def __init__(self, x, y) -> None:
        self.X_coordinate = x
        self.Y_coordinate = y
        self.height = 30
        self.length = 180
        self.width = 5
        self.color = (255, 0, 90)
        self.p = pygame.Rect(self.X_coordinate, self.Y_coordinate,
                             self.length, self.height)

    def draw_players(self, screen):
        pygame.draw.rect(screen, self.color, self.p, self.width)

    def players_move(self, left_key, right_key):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[left_key] and self.p.x > 25:
            self.p.x -= 9
        if key_pressed[right_key] and self.p.x < 800 - (self.length + 25):
            self.p.x += 9

    @classmethod
    def other_keys(cls):
        key_pressed2 = pygame.key.get_pressed()
        if key_pressed2[pygame.K_SPACE]:
            cls.start = True
