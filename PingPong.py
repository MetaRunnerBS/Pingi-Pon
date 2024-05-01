from pygame import *
mixer.init()
font.init()
#b_font = font.SysFont('Bahnschrift Light Condensed', 50)
window = display.set_mode((600, 400))
display.set_caption("Pingi Pon")
#BG = transform.scale(image.load("galaxy.jpg"), (700, 800))
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
        if keys[K_d] and self.rect.right < 700:
            self.rect.x += self.speed
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
player = Player("ten2.png", 100, 100, 100, 100, 100)
player.update()
display.update()
clock.tick(60)