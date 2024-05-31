import pygame, sys


class CheckBox:
    def __init__(self, x, y, width, colour, font, font_colour, margin, text="", image=None):
        self.x = x
        self.y = y - width/2
        self.orig_pos = (self.x, self.y)
        self.width = width
        self.orig_width = width
        self.colour = colour

        self.image = pygame.transform.scale(image, (self.orig_width, self.orig_width))
        self.orig_image = self.image

        self.clicked = 0
        self.checked = False

        self.font = font
        self.font_colour = font_colour
        self.margin = margin
        self.text = text
        self.text_surface = font.render(text, True, font_colour)
        
    def _draw_image(self, screen):
        screen.blit(self.image, (self.x, self.y))

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
            self.image = pygame.transform.scale(self.image, (int(self.width), int(self.width)))
            self.x = self.orig_pos[0] + self.orig_width * 0.1
            self.y = self.orig_pos[1] + self.orig_width * 0.1
        else:
            self.width = self.orig_width
            self.image = self.orig_image
            self.x = self.orig_pos[0]
            self.y = self.orig_pos[1]
        
        if self.clicked % 2 == 0:
            self.checked = False
        elif self.clicked % 2 != 0:
            self.checked = True
        
        if self.checked:
            self._draw_image(screen)


if __name__ == "__main__":
    pygame.init()
    screen_width, screen_height = 800, 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    tick_image = pygame.image.load("/Volumes/Macintosh HD 2/Users/nielvandercolff/Documents/Niel Code/Python/prebuilt4pygame/Tick.png").convert_alpha()
    font = pygame.font.Font("/Volumes/Macintosh HD 2/Users/nielvandercolff/Documents/Niel Code/Python/prebuilt4pygame/Quicksand-Regular.ttf", 38)

    checkbox1 = CheckBox(30, screen_height/2, 50, (255, 255, 255), font, (255, 255, 255), 10, "Check me out ;)", tick_image)
    checkbox2 = CheckBox(30, screen_height/2 + 100, 50, (255, 255, 255), font, (255, 255, 255), 10, "Check me out too :D", tick_image)

    while True:
        screen.fill((0, 0, 0))
        checkbox1.draw(screen)
        checkbox2.draw(screen)
        for event in pygame.event.get():
            checkbox1.handle_events(event)
            checkbox2.handle_events(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        checkbox1.update()
        checkbox2.update()
        pygame.display.update()
        clock.tick(60)