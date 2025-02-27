import pygame
from game import Game
from game_handler import GameHandler
from ui import UI


pygame.init()

WIDTH = 500
HEIGHT = 600

FPS = 60

if __name__ == "__main__":

    pygame.display.set_caption("M I N E S W E E P E R - The Modern one")
    surf        = pygame.display.set_mode((WIDTH, HEIGHT))  # The surface (window) we want to draw on
    game_surf   = pygame.Surface((500, 500))                # The game surface (where the actual game is)
    ui_surf     = pygame.Surface((500, 100))                # The UI surface (where the amount of mines is shown)

    game    = Game(surf=game_surf, fps=FPS, mines=14,       # The game object
                   grid_rows=10, grid_columns=10)
    ui      = UI(surf=surf)                                 # The UI object

    handler = GameHandler(surf, game, ui)                   # The handler object (combining the classes using composition)

    handler.run()                                           # Run the game

pygame.quit() # Quits the game when the game stops running (or the player loses)

### By Radin ###
