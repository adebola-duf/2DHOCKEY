import pygame
pygame.init()


class Texts:
    def __init__(self) -> None:
        self.font1 = pygame.font.Font("Angels Cookie.ttf", 50)
        self.font2 = pygame.font.Font("Sunday morning.otf", 55)

    def start_text(self, screen):
        startX_coordinate, startY_coordinate = 80, 310
        start_text = self.font1.render(
            '* press space bar to start', True, (255, 255, 255))
        screen.blit(start_text, (startX_coordinate,
                    startY_coordinate))

    def game_over(self, screen):
        goX_coordinate, goY_coordinate = 210, 150
        go_text = self.font2.render(
            'Game Over', True, (255, 255, 255))
        screen.blit(go_text, (goX_coordinate,
                    goY_coordinate))

    def replay(self, screen):
        replayX_coordinate, replayY_coordinate = 120, 500
        replay_text = self.font1.render(
            '* press Tab to replay', True, (255, 255, 255))
        screen.blit(replay_text, (replayX_coordinate,
                    replayY_coordinate))
