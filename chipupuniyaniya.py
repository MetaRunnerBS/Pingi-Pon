from pygame import *
font.init()

window = display.set_mode((800, 600))
display.set_caption("Menu")
clock = time.Clock()
font_txt = font.SysFont('Arial', 36)

menu_options = ['Start', 'Option', 'Exit']
selected_option = 0
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class Button():
    def __init__(self, text, x, y, w, h, color, hover_color):
        self.text = text
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.hover_color = hover_color
    def draw(self):
        x, y = mouse.get_pos()
        if (self.x < x < self.x + self.w) and (self.y < y < self.y + self.h):
            draw.rect(window, self.hover_color, (self.x, self.y, self.w, self.h))
        else:
            draw.rect(window, self.color, (self.x, self.y, self.w, self.h))
        text = font_txt.render(self.text, True, WHITE)
        text_rect = text.get_rect(center=(self.x + self.w / 2, self.y + self.h / 2))
        window.blit(text, text_rect)

buttons = []
for i, option in enumerate(menu_options):
    button = Button(option, 400 - 100, 200 + i * 50, 200, 50, BLACK, RED)
    buttons.append(button)

run = True
game_state = "menu"
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if game_state == "menu":
                if e.key == K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif e.key == K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif e.key == K_RETURN:
                    if selected_option == 0:
                        game_state = "game"
                    elif selected_option == 1:
                        game_state = "option"
                    elif selected_option == 2:
                        game_state = "exit"
            if e.key == K_ESPACE:
                game_state = "menu"
    window.fill(BLACK)
    if game_state == "menu":
        for i, button in enumerate(buttons):
            if i == selected_option:
                button.color = GREEN
            else:
                button.color = BLACK
            button.draw()
    elif game_state == "option":
        window.fill(WHITE)
        text = font_txt.render('OPTION', True, BLACK)
        window.blit(text, (320, 20))
    display.update()
    clock.tick(30)