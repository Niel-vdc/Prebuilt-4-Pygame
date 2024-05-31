import pygame, sys
import math


class CheckBox:
    def __init__(self, x, y, width, colour, mark_width, mark_colour, font, font_colour, margin, text=""):
        self.x = x
        self.y = y - width/2
        self.orig_pos = (self.x, self.y)
        self.orig_width = width
        self.width = width
        self.colour = colour

        self.mark_width = mark_width
        self.mark_colour = mark_colour

        self.clicked = 0
        self.checked = False

        self.font = font
        self.font_colour = font_colour
        self.margin = margin
        self.text = text
        self.text_surface = font.render(text, True, font_colour)
        
    def _draw_cross(self, screen):
        pygame.draw.line(screen, self.mark_colour, (self.x, self.y), (self.x + self.width, self.y + self.width), self.mark_width)
        pygame.draw.line(screen, self.mark_colour, (self.x + self.width, self.y), (self.x, self.y + self.width), self.mark_width)

    def mouse_is_over(self):
        mouse = pygame.mouse.get_pos()

        if mouse[0] >= self.orig_pos[0] and mouse[0] <= self.orig_pos[0] + self.orig_width + self.margin + self.text_surface.get_width() and mouse[1] >= self.orig_pos[1] and mouse[1] <= self.orig_pos[1] + self.orig_width:
            return True
        return False
    
    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONUP and self.mouse_is_over():
            self.clicked += 1

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.width))
        
        screen.blit(self.text_surface, (self.x + self.width + self.margin, self.y + self.width/2 - self.text_surface.get_height()/2))

    def update(self):
        if self.mouse_is_over() and pygame.mouse.get_pressed()[0]:
            self.width = self.orig_width * 0.8
            self.x = self.orig_pos[0] + self.orig_width * 0.1
            self.y = self.orig_pos[1] + self.orig_width * 0.1
        else:
            self.width = self.orig_width
            self.x = self.orig_pos[0]
            self.y = self.orig_pos[1]
        
        if self.clicked % 2 == 0:
            self.checked = False
        elif self.clicked % 2 != 0:
            self.checked = True
        
        if self.checked:
            self._draw_cross(screen)


if __name__ == "__main__":
    pygame.init()
    screen_width, screen_height = 800, 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    font = pygame.font.Font("/Volumes/Macintosh HD 2/Users/nielvandercolff/Documents/Niel Code/Python/prebuilt4pygame/Quicksand-Regular.ttf", 38)

    checkbox = CheckBox(30, screen_height/2, 50, (255, 255, 255), 5, (0, 0, 0), font, (255, 255, 255), 10, "Check me out ;)")
    checkbox2 = CheckBox(30, screen_height/2 + 100, 50, (255, 255, 255), 5, (0, 0, 0), font, (255, 255, 255), 10, "Check me out too hehe")

    while True:
        screen.fill((0, 0, 0))
        checkbox.draw(screen)
        checkbox2.draw(screen)
        for event in pygame.event.get():
            checkbox.handle_events(event)
            checkbox2.handle_events(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        checkbox.update()
        checkbox2.update()
        pygame.display.update()
        clock.tick(60)