import pygame, sys


class TextBox:
    def __init__(self, x, y, width, height, padding, colour, active, curser_width, curser_colour, font, font_colour, base_font=None, base_font_colour=None, base_text="", outline_width=None, outline_colour=None):
        self.x = x - width/2
        self.y = y - height/2
        self.orig_width = width
        self.width = width
        self.height = height
        self.padding = padding
        self.colour = colour

        self.active = active

        self.font = font
        self.font_colour = font_colour
        self.user_text = ""
        self.text_surface = font.render(self.user_text, True, font_colour)

        self.base_font = base_font
        self.base_font_colour = base_font_colour
        self.base_text = base_text
        self.base_text_surface = base_font.render(self.base_text, True, base_font_colour)

        self.curser_width = curser_width
        self.curser_height = self.text_surface.get_height()
        self.curser_colour = curser_colour

        self.outline_width = outline_width
        self.outline_colour = outline_colour
        
    def mouse_is_over(self):
        mouse = pygame.mouse.get_pos()

        if mouse[0] >= self.x and mouse[0] <= self.x + self.width and mouse[1] >= self.y and mouse[1] <= self.y + self.height:
            return True
        return False
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.mouse_is_over():
            self.active = True
        if event.type == pygame.MOUSEBUTTONDOWN and not self.mouse_is_over():
            self.active = False
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                self.active = False
            if event.key == pygame.K_BACKSPACE:
                self.user_text = self.user_text[:-1]
            self.user_text += event.unicode
            self.text_surface = self.font.render(self.user_text, True, self.font_colour)

    def draw(self, screen):
        if self.outline_width:
            pygame.draw.rect(screen, self.outline_colour, (self.x - self.outline_width, self.y - self.outline_width, self.width + self.outline_width*2, self.height + self.outline_width*2))
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))

        if self.user_text == "":
            screen.blit(self.base_text_surface, (self.x + self.padding, self.y + self.padding))
        else:
            screen.blit(self.text_surface, (self.x + self.padding, self.y + self.padding))
        
        if self.active:
            pygame.draw.rect(screen, self.curser_colour, (self.x + self.text_surface.get_width() + self.padding, self.y + self.padding, self.curser_width, self.curser_height))

    def update(self):
        self.width = max(self.orig_width, self.text_surface.get_width() + self.curser_width + self.padding * 2)
        

            
if __name__ == "__main__":
    pygame.init()
    screen_width, screen_height = 800, 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    font = pygame.font.Font("/Volumes/Macintosh HD 2/Users/nielvandercolff/Documents/Niel Code/Python/prebuilt4pygame/Quicksand-Regular.ttf", 28)
    font_italic = pygame.font.Font("/Volumes/Macintosh HD 2/Users/nielvandercolff/Documents/Niel Code/Python/prebuilt4pygame/Raleway-Italic.ttf", 28)

    text_box = TextBox(screen_width/2, screen_height/2, 250, 80, 20, (255, 255, 255), False, 3, (100, 100, 100), font, (0, 0, 0), font_italic, (150, 150, 150), "Text", 4, (30, 80, 200))

    while True:
        screen.fill((0, 0, 0))
        text_box.draw(screen)
        for event in pygame.event.get():
            text_box.handle_event(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        text_box.update()
        pygame.display.update()
        clock.tick(60)