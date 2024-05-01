from pygame import * 
mixer.init() 
font.init() 
 
window = display.set_mode((700, 500)) 
display.set_caption('PingPong') 
BG = transform.scale(image.load('bgbgbg.png'), (700, 500)) 
clock = time.Clock() 
restart_txt = font.SysFont('Comic Sans MS', 59).render('Чтобы начать заново,', True, (0, 0, 0))
restart_txt2 = font.SysFont('Comic Sans MS', 59).render('нажмите на пробел', True, (0, 0, 0))
 
class GameSprite(sprite.Sprite): 
    def __init__(self, x, y, w, h, img, speed=0): 
        super().__init__() 
        self.image = transform.scale(image.load(img), (w, h)) 
        self.speed = speed 
        self.rect = self.image.get_rect() 
        self.rect.x = x 
        self.rect.y=y 
    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y)) 
 
class Player1(GameSprite): 
    def update(self): 
        key_pressed = key.get_pressed() 
        if key_pressed[K_w] and self.rect.y > 10: 
            self.rect.y -= self.speed 
        if key_pressed[K_s] and self.rect.y < 410: 
            self.rect.y += self.speed 
 
class Player2(GameSprite): 
    def update(self): 
        key_pressed = key.get_pressed() 
        if key_pressed[K_UP] and self.rect.y > 10: 
            self.rect.y -= self.speed 
        if key_pressed[K_DOWN] and self.rect.y < 410: 
            self.rect.y += self.speed 

class Ball(GameSprite):
    def __init__(self, x, y, size, img, speed_x=5, speed_y=5):
        super().__init__(x, y, size, size, img)
        self.speed_x = speed_x
        self.speed_y = speed_y
    
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y < 0 or self.rect.y > 500 - self.rect.height:
            self.speed_y *= -1
        if self.rect.colliderect(player_one.rect):
            self.speed_x *= -1
        if self.rect.colliderect(player_two.rect):
            self.speed_x *= -1
        if self.rect.x < 0 or self.rect.x > 700 - self.rect.width:
            global finish
            global restart_txt
            finish = True
            window.blit(restart_txt, (50, 100))
            window.blit(restart_txt2, (60, 200))


player_one = Player1(30, 210, 30, 100, 'p1.png', 10) 
player_two = Player2(640, 210, 30, 100, 'p1.png', 10) 
ball = Ball(345, 245, 50, 'balll.png', 5, 5)
run = True 
finish = False 
 
while run: 
    for e in event.get(): 
        if e.type == QUIT: 
            run = False 
    if not finish:  
        window.blit(BG, (0,0)) 
        player_one.update() 
        player_one.reset() 
        player_two.update() 
        player_two.reset()  
        ball.update()
        ball.reset()
    if finish: 
        keys = key.get_pressed() 
        if keys[K_SPACE]: 
            finish = False 
            player_one = Player1(30, 210, 30, 100, 'p1.png', 10) 
            player_two = Player2(640, 210, 30, 100, 'p1.png', 10)
            ball = Ball(345, 245, 20, 'balll.png', 5, 5) 
             
    clock.tick(60) 
    display.update()
