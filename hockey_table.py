from turtle import Screen
import pygame
pygame.init()


class HockeyTable:
    def __init__(self) -> None:
        self.b1 = pygame.Rect(0, 0, 800, 20)
        self.b2 = pygame.Rect(0, 700, 800, 20)

    def draw_table(self, screen):
        BordersX_coord = [0, 0, 0, 0, 780]
        BordersY_coord = [0, 350, 700, 0, 0]
        Borders_length = [800, 800, 800, 20, 20]
        Borders_height = [20, 20, 20, 720, 720]
        borders_color = [(63, 72, 204), (63, 72, 204),
                         (63, 72, 204), (0, 255, 4), (0, 255, 4)]
        pygame.draw.rect(screen, (63, 72, 204), self.b1)
        pygame.draw.rect(screen, (63, 72, 204), self.b2)
        for i in range(5):
            pygame.draw.rect(
                screen, borders_color[i], (BordersX_coord[i], BordersY_coord[i], Borders_length[i], Borders_height[i]))
