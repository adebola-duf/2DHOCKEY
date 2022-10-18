import pygame
pygame.init()


class Ball:
    def __init__(self) -> None:
        self.height = 30
        self.length = 30
        self.x_coord = 30
        self.y_coord = 90
        self.ball = pygame.Rect(self.x_coord, self.y_coord,
                                self.length, self.height)
        self.x_speed = 4
        self.y_speed = 4
        self.gameover = False

    def draw_ball(self, screen):
        pygame.draw.ellipse(screen, (255, 0, 0), self.ball, 7)

    def ball_move(self):
        if self.ball.x >= 750 or self.ball.x <= 20:
            self.x_speed *= -1

        if self.ball.y <= 20 or self.ball.y >= 670:
            self.y_speed *= -1

        self.ball.x += self.x_speed
        self.ball.y += self.y_speed

    def collision(self, p1, p2, b1, b2):
        if self.ball.colliderect(p1) or self.ball.colliderect(p2):
            self.y_speed *= -1

        self.ball.y += self.y_speed
        if self.ball.colliderect(b2) or self.ball.colliderect(b1):
            self.gameover = True

    def gameover_sike(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_TAB]:
            self.gameover = False
