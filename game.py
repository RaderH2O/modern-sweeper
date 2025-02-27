from grid import Grid
import pygame

from minesweeper_types import MS


class Game:

    def __init__(self, surf: pygame.Surface, fps: int, mines=10, grid_rows=10, grid_columns=10):
        self.mines      = mines

        self.surf       = surf
        self.fps        = fps
        self.running    = True
        self.won        = False
        self.lost       = False
        self.clock      = pygame.time.Clock()

        pygame.transform.set_smoothscale_backend("GENERIC")

        # Loading resources
        self.mine_img   = pygame.image.load("res/img/mine.png")
        self.flag_img   = pygame.image.load("res/img/flag.png")

        self.font       = pygame.font.Font("res/fonts/SansSerifFLF.otf", 30)
        
        self.width, self.height = surf.get_size()

        self.mine_img   = pygame.transform.smoothscale(
                                                        self.mine_img,
                                                        (
                                                            self.width / grid_columns - 6,
                                                            self.height / grid_rows - 6
                                                        )
                                                      )

        self.flag_img   = pygame.transform.smoothscale(
                                                        self.flag_img,
                                                        (
                                                            self.width / grid_columns - 6,
                                                            self.height / grid_rows - 6
                                                        )
                                                      )

        self.grid = Grid(columns=grid_columns, rows=grid_rows, mines=mines)

    def handle_events(self, events: list[pygame.event.Event], rel_mouse_pos: tuple[int, int] = (0, 0)):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = rel_mouse_pos
                if event.button == pygame.BUTTON_RIGHT:
                    self.grid.flag    (
                                        int((x / self.width) * self.grid.columns),
                                        int((y / self.height) * self.grid.rows)
                                      )

                if event.button == pygame.BUTTON_LEFT:
                    gx = int((x / self.width) * self.grid.columns)
                    gy = int((y / self.height) * self.grid.rows)
                    self.grid.uncover (
                                        int((x / self.width) * self.grid.columns),
                                        int((y / self.height) * self.grid.rows)
                                      )

                    if self.grid.grid[gy][gx] == MS.Mine:
                        self.lost = True


    def _has_won(self):
        for x in range(self.grid.columns):
            for y in range(self.grid.rows):
                if self.grid.grid[y][x] == MS.Mine and not self.grid.flags[y][x]:
                    return False

        return True

    def update(self):
        if self.grid.flag_count == self.mines:
            if self._has_won():
                self.won = True

    def draw(self):

        grid        = self.grid.grid

        g_width     = self.width / self.grid.columns
        g_height    = self.height / self.grid.rows

        for x in range(self.grid.columns):
            for y in range(self.grid.rows):

                pos = (x * g_width + 2, y * g_height + 2, g_width - 4, g_height - 4)

                # Hiding the "hidden" tiles
                if self.grid.hidden[y][x]:
                    pygame.draw.rect(self.surf, (230, 230, 230), pos, border_radius=10)

                    # Show the flag over the hidden tile
                    if self.grid.flags[y][x]: self.surf.blit(self.flag_img, (x * g_width, y * g_height))
                    continue

                if grid[y][x] == MS.Mine:
                    pygame.draw.rect(self.surf, "gray", pos, border_radius=10)
                    self.surf.blit(self.mine_img, (x * g_width + 3, y * g_height + 3))
                else:

                    text = self.font.render(str(grid[y][x].value), True, (0, 0, 0))

                    val = 245 - 10 * grid[y][x].value
                    color = pygame.Color(val, val, val)
                    pygame.draw.rect(self.surf, color, pos, border_radius=10)
                    if grid[y][x] != MS.Empty:
                        self.surf.blit(text, (pos[0] + 15, pos[1] + 8))

### By Radin ###
