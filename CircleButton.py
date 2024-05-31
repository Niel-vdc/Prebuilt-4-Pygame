import pygame
import math


class CircleButton:
    def __init__(self, x, y, radius, colour, hover_colour, clicked_colour, func, font, font_colour, text="", outline_width=None, outline_colour=None):
        self.x = x
        self.y = y
        self.radius = radius

        self.current_colour = colour
        self.colour = colour
        self.hover_colour = hover_colour
        self.clicked_colour = clicked_colour

        self.func = func

        self.font = font
        self.font_colour = font_colour
        self.text = text
        self.text_surface = font.render(text, True, font_colour)

        self.outline_width = outline_width
        self.outline_colour = outline_colour
        
    def mouse_is_over(self):
        mouse = pygame.mouse.get_pos()

        line = math.sqrt((self.x - mouse[0])**2 + (self.y - mouse[1])**2)

        if line < self.radius:
            return True
        return False

    def clicked(self):
        if self.mouse_is_over() and pygame.mouse.get_pressed()[0]:
            self.func()
            return True
        return False
        
    def draw(self, screen):
        if self.outline_width:
            pygame.draw.circle(screen, self.outline_colour, (self.x, self.y), self.radius + self.outline_width * 2)
        pygame.draw.circle(screen, self.current_colour, (self.x, self.y), self.radius)

        if self.text != "":
            screen.blit(self.text_surface, self.text_surface.get_rect(center = (self.x, self.y)))
        
    def update(self):
        if self.clicked():
            self.current_colour = self.clicked_colour
        elif self.mouse_is_over():
            self.current_colour = self.hover_colour
        else:
            self.current_colour = self.colour


if __name__ == "__main__":
    import sys

    def func1():
        print("HELLO!!")

    pygame.init()
    screen = pygame.display.set_mode((800, 800))

    font = pygame.font.Font("/Volumes/Macintosh HD 2/Users/nielvandercolff/Documents/Niel Code/Python/prebuilt4pygame/Quicksand-Regular.ttf", 38)

    button = CircleButton(screen.get_width()/2, screen.get_height()/2, 100, (200, 30, 50), (255, 80, 100), (130, 0, 0), func1, font, (255, 255, 255), "Press me", 2, (255, 255, 255))

    while True:
        button.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        button.update()
        pygame.display.update()