from pygame import *
import json
from random import randint

width, height = 800, 600
window = display.set_mode((width, height))
display.set_caption('P-L-A-T-F-O-R-M')
clock = time.Clock()

FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Player():
    def __init__(self, w, h,):
        self.w = 50
        self.h = 50
        self.x = w//2 - self.w//2
        self.y = h - self.h
        self.speed = 5
        self.jump = False
        self.jump_count = 0
    def draw(self):
        draw.rect(window, BLUE, (self.x, self.y, self.w, self.h))
    def move(self, keys):
        if keys[K_d]:
            self.x += self.speed
        elif keys[K_a]:
            self.x -= self.speed
        elif keys[K_SPACE] and not self.jump:
            self.jump_count = 20
            self.jump = True
    def update(self):
        if self.jump_count > 0:
            self.y -= 15
            self.jump_count -= 1
        for platform in platforms:
            if self.y + self.h >= platform.y and self.y + self.h < platform.y + 10 \
                and self.x + self.w >= platform.x and self.x + self.h < platform.x + width:
                self.y = platform.y - self.h
                self.jump = False
        self.y += 10*(self.y / (height - self.h))
        if self.y > height - self.h:
            self.y = height - self.h
            self.jump = False

class Platform():
    def __init__(self, x, y, w, h):
        self.y = y
        self.x = x
        self.h = h
        self.w = w
    def draw(self):
        draw.rect(window, BLACK, (self.x, self.y, self.w, self.h))

class Goal():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.h = 50
        self.w = 50
    def draw(self):
        draw.rect(window, GREEN, (self.x, self.y, self.w, self.h))
    def update(self):
        global lvls, platforms
        if player.x + player.w >= self.x and player.x <= self.x + self.w \
            and player.y + player.h >= self.y and player.y <= self.y + self.h:
            print("LEVEL COMPLETE")
            platforms.clear()
            for d in lvls[1]['platforms']:
                platform = Platform(d['x'], d['y'], d['w'], d['h'])
                platforms.append(platform)
            goal = Goal(lvls[1]['goal']['x'], lvls[1]['goal']['y'])
            player.x = width // 2 - self.w // 2
            player.y = height - self.h

with open('levels.json') as f:
    lvls = json.load(f)
platforms = []
for d in lvls[0]["platforms"]:
    platform = Platform(d['x'], d['y'], d['w'], d['h'])
    platforms.append(platform)
goal = Goal(lvls[0]['goal']['x'], lvls[0]['goal']['y'])
player = Player(width, height)
clock = time.Clock()
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.fill(WHITE)
    player.draw()
    player.move(key.get_pressed())
    player.update()
    for platform in platforms:
        platform.draw()
    goal.draw()
    goal.update()
    display.update()
    clock.tick(FPS)