import pygame_menu
import pygame
from pygame_menu import themes
class Menu(pygame_menu.Menu):
    def __init__(self, root, theme=themes.THEME_DARK):
        super().__init__("", root.get_width(), root.get_height(), theme=theme)
        self.root = root
        self.arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size=(10, 15))

    def flip2(self, event):
        if self.is_enabled():
            self.update(event)
        if self.is_enabled():
            self.draw(self.root)