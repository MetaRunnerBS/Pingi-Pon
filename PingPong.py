from pygame import *
mixer.init()
font.init()
#b_font = font.SysFont('Bahnschrift Light Condensed', 50)
window = display.set_mode((800, 500))
display.set_caption("Pingi Pon")
BG = transform.scale(image.load("bg.png"), (800, 500))
#win_txt = font.SysFont("Bahnschrift Light Condensed", 60,).render("YOU WIN!", True, (0, 255, 70))
#lose_txt = font.SysFont("Bahnschrift Light Condensed", 60,).render("YOU LOSE!", True, (220, 40, 20))
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
player = Player("ten2.png", 30, 100, 5, 110, 110)
player2 = Player("ten1.png", 670, 100, 5, 110, 110)
clock = time.Clock()
run = True
finish = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.blit(BG, (0, 0))
        player.reset()
        player.update()
        player2.reset()
        player2.update()
        #if sprite.collide_rect(player, final):
        #    window.blit(win_txt, (250, 250))
        #    win_sound.play()
        #    finish = True
        #    mixer.music.stop()
    display.update()
    clock.tick(60)