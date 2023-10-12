import chess
import pygame
while True:
    chess.play()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        break
