import pygame
pygame.init()

class Button:
    """custom button class used for menus"""
    def __init__(self, rect, color, clicked, border_radius, selection_color, button_type="default"):
        self.rect = rect
        self.clicked = clicked
        self.color = color
        self.border_radius = border_radius
        self.selection_color = selection_color
        self.button_type = button_type

    def draw_button(self, screen):
        if not self.clicked:
            pygame.draw.rect(screen, self.color, self.rect, border_radius=self.border_radius)
        else:
            pygame.draw.rect(screen, self.selection_color, self.rect, border_radius=self.border_radius)