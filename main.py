# make a single and multi-player mode


import pygame
from players import Players
from hockey_table import HockeyTable
from ball import Ball
from Text import Texts

pygame.init()

clock = pygame.time.Clock()

screen_size = screen_length, screen_height = 800, 720
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("2D Hockey OOP")

player1 = Players(30, 25)
player2 = Players(100, 665)
ht = HockeyTable()
ball = Ball()
text = Texts()


run_game = True
while run_game:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run_game = False

    screen.fill((0, 0, 0))
    clock.tick(60)
    ht.draw_table(screen)

    if not Players.start and not ball.gameover:
        text.start_text(screen)
        Players.other_keys()
    elif Players.start and not ball.gameover:
        ball.draw_ball(screen=screen)
        player2.draw_players(screen)
        player1.draw_players(screen)
        player1.players_move(pygame.K_a, pygame.K_d)
        player2.players_move(pygame.K_LEFT, pygame.K_RIGHT)
        ball.ball_move()
        ball.collision(p1=player1.p, p2=player2.p, b1=ht.b1, b2=ht.b2)
    elif Players.start and ball.gameover:
        text.game_over(screen)
        ball.gameover_sike()
        text.replay(screen)

    pygame.display.update()
# how are y'all doing today, hope things are going really well with you
# hi there
