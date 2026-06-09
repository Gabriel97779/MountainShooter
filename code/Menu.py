import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_BLUISH_WHITE, COLOR_BLUE_LIGHT, MENU_OPTION, COLOR_WHITE, COLOR_FRENCH_BLUE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Menu.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./asset/song_menu.wav')
        pygame.mixer_music.play(-1)
        # DRAW IMAGES
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(45, "PEAK", COLOR_BLUISH_WHITE, ((WIN_WIDTH / 2), 40))
            self.menu_text(25, "Extreme", COLOR_BLUE_LIGHT, ((WIN_WIDTH / 2), 86))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(15, MENU_OPTION[i], COLOR_FRENCH_BLUE, ((WIN_WIDTH / 2), 200 + (20 * i)))

                else:
                    self.menu_text(15, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + (20 * i)))

            pygame.display.flip()


            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # <-- close window
                    quit()  # <-- end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:#DOWN
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option +=1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:#UP
                        if menu_option > 0:
                            menu_option -=1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]



    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font("./asset/PressStart2P-Regular.ttf", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
