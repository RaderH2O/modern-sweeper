import pygame


class UI:

    def __init__(self, surf: pygame.Surface):

        self.surf = surf
        self.font = pygame.font.Font("res/fonts/SansSerifFLF.otf", 30)

        self.width, self.height = self.surf.get_size()

    def draw(self, mines):
        title = self.font.render("M I N E S W E E P E R", True, (0, 0, 0))
        m_text = f"{mines} M I N E S" if mines > 1 else f"{mines} M I N E"
        mines_text = self.font.render(m_text, True, (0, 0, 0))

        self.surf.fill("white")

        self.surf.blit(title, (20, 20))
        self.surf.blit(mines_text, (20, 60))

### By Radin ###
