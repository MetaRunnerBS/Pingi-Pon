from pygame import *
import time

mixer.init()
font.init()

# Окно
window = display.set_mode((800, 500))
display.set_caption("Pingi Pon")
BG = transform.scale(image.load("bg.png"), (800, 500))

# Шрифты, тексты
font1 = font.SysFont('Arial', 50)
start_text = font1.render("Нажмите пробел чтобы начать", True, (255, 255, 255))

# Скорости мяча
speed_x = 5
speed_y = 5

# Классы спрайтов
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_s] and self.rect.bottom < 500:
            self.rect.y += self.speed
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed

class Player2(GameSprite): 
    def update(self): 
        keys = key.get_pressed() 
        if keys[K_UP] and self.rect.y > 0: 
            self.rect.y -= self.speed 
        if keys[K_DOWN] and self.rect.bottom < 500: 
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, ball_image, ball_x, ball_y, w, h, speed_x=5, speed_y=5):
        super().__init__(ball_image, ball_x, ball_y, 0, w, h)
        self.speed_x = speed_x
        self.speed_y = speed_y
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y < 0 or self.rect.y > 500 - self.rect.height:
            self.speed_y *= -1
        if self.rect.colliderect(player.rect):
            self.speed_x *= -1
        if self.rect.colliderect(player2.rect):
            self.speed_x *= -1
        if self.rect.x < 0 or self.rect.x > 800 - self.rect.width:
            global finish
            finish = True

player = Player("ten2.png", 30, 100, 5, 110, 110)
player2 = Player2("ten1.png", 670, 100, 5, 110, 110)
ball = Ball('tennis.png', 400, 250, 40, 40)
clock = time.Clock()

# Состояния игры
run = True
finish = False
game_started = False
countdown = False
countdown_start = 0

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE and not game_started:
                countdown = True
                countdown_start = time.time()

    if not game_started:
        window.blit(BG, (0, 0))
        window.blit(start_text, (150, 220))
        if countdown:
            elapsed = time.time() - countdown_start
            if elapsed >= 3:
                game_started = True
                countdown = False
            else:
                countdown_text = font1.render(str(3 - int(elapsed)), True, (255, 255, 255))
                window.blit(countdown_text, (380, 220))

    else:
        if not finish:
            window.blit(BG, (0, 0))
            player.reset()
            player.update()
            player2.reset()
            player2.update()
            ball.reset()
            ball.update()

    display.update()
    clock.tick(60)
