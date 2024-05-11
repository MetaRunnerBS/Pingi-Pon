from pygame import *
mixer.init()
font.init()
#font1 = font.SysFont('Arial', 50)
window = display.set_mode((800, 500))
display.set_caption("Pingi Pon")
BG = transform.scale(image.load("bg.png"), (800, 500))
#win1_txt = font.SysFont("Arial", 60,).render("Победил Первый Игрок!", True, (0, 255, 70))
#win2_txt = font.SysFont("Arial", 60,).render("Победил Второй Игрок!", True, (220, 40, 20))
speed_x = 5
speed_y = 5
#ball.rect.x += speed_x
#ball.rect.y += speed_y
#if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2), ball):
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
        super().__init__(ball_image, ball_x, ball_y, w, h)
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
run = True
finish = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.colliderect(player) or ball.colliderect(player2):
            speed_y *= -1
        if ball.rect.x <= 0 or ball.rect.x >= 450:
            speed_x *= -1
        if ball.rect.y <= 0:
            speed_y *= -1
        window.blit(BG, (0, 0))
        player.reset()
        player.update()
        player2.reset()
        player2.update()
        ball.reset()
        ball.update()
        #if sprite.collide_rect(player, final):
        #    window.blit(win_txt, (250, 250))
        #    win_sound.play()
        #    finish = True
        #    mixer.music.stop()
    display.update()
    clock.tick(60)