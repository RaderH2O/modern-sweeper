import pygame

from game import Game
from ui import UI


class GameHandler:

    def __init__(self, display: pygame.Surface, game: Game, ui: UI):

        self.display    = display
        self.game       = game
        self.ui         = ui


    def run(self):
        while self.game.running:
            mouse_pos = pygame.mouse.get_pos()
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.game.running = False
            if not self.game.lost and not self.game.won:
                self.game.handle_events(events, (mouse_pos[0], mouse_pos[1] - 100))

            self.display.fill((230, 230, 230))
            self.game.surf.fill("white")

            ### UPDATE  ###
            self.game.update()

            ### DRAWING ###
            self.ui.draw(self.game.mines)
            self.game.draw()

            self.display.blit(self.ui.surf, (0, 0))
            self.display.blit(self.game.surf, (0, 100))

            if self.game.won:
                pygame.draw.rect(self.display, "white", (20, 200, 460, 250), border_radius=30)
                won_text = self.ui.font.render("Y O U   W O N !", True, (0, 0, 0))
                self.display.blit(won_text, (150, 310))

            if self.game.lost:
                pygame.draw.rect(self.display, "black", (20, 200, 460, 250), border_radius=30)
                lost_text = self.ui.font.render("Y O U   L O S T !", True, (255, 255, 255))
                self.display.blit(lost_text, (150, 310))

            pygame.display.flip()
            self.game.clock.tick(self.game.fps)
