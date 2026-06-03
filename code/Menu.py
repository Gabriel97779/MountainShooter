import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLLOR_BLUISH_WHITE, COLLOR_BLUE_LIGHT, MENU_OPTION, COLLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Menu.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./asset/song_menu.wav')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(40,"Mountain",COLLOR_BLUISH_WHITE, ((WIN_WIDTH/2), 40))
            self.menu_text(25,"Shooter",COLLOR_BLUE_LIGHT, ((WIN_WIDTH/2), 86))

            for i in range(len(MENU_OPTION)):
                self.menu_text(15, MENU_OPTION[i], COLLOR_WHITE ,((WIN_WIDTH / 2), 200 + (20 * i)))

            pygame.display.flip()
            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # <-- close window
                    quit()  # <-- end pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font("./asset/PressStart2P-Regular.ttf", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
