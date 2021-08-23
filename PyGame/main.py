import pygame

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([1080, 720])
pygame_icon = pygame.image.load('Plr_chr.bmp')
pygame.display.set_icon(pygame_icon)
pygame.display.set_caption('A Game')
background_image = pygame.image.load('BKG.bmp')

# velocities
jumpvel = 50
lvel = 0
rvel = 0

# PLR
pljump = False
plleft = False
plright = False
plx = 100
ply = 528
yground = 528.5
hp = 3
level = 1

boxx = 700
boxy = 528

spikex = 480
spikey = 528.5

finx = 940
finy = 432

hp3 = pygame.image.load("hp3.bmp")
hp2 = pygame.image.load("hp2.bmp")
hp1 = pygame.image.load("hp1.bmp")

lose_bkg = pygame.image.load("lose_scr.bmp")
lose = False
win_bkg = pygame.image.load("win_screen.bmp")
win = False

class WoodenBox(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.boximg = pygame.image.load('Wooden_Box.bmp')
        self.boxrect = self.boximg.get_rect()
        self.boxrect.center = (x, y)

    def draw(self):
        screen.blit(self.boximg, self.boxrect)


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.plimg = pygame.image.load('Plr_chr.bmp')
        self.plrect = self.plimg.get_rect()
        self.plrect.center = (x, y)

    def draw(self):
        screen.blit(self.plimg, self.plrect)

    def move(self, x, y):
        self.plrect.center = (x, y)


class Spike(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.spimg = pygame.image.load('Spike.bmp')
        self.sprect = self.spimg.get_rect()
        self.sprect.center = (x, y)

    def draw(self):
        screen.blit(self.spimg, self.sprect)

class Finish(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.finimg = pygame.image.load('finish.bmp')
        self.finrect = self.finimg.get_rect()
        self.finrect.center = (x, y)

    def draw(self):
        screen.blit(self.finimg, self.finrect)

finish = Finish(finx, finy)
box1 = WoodenBox(boxx, boxy)
spike1 = Spike(spikex, spikey)
player = Player(plx, ply)


# Run until the user asks to quit
running = True
while running:

    startposx = plx
    startposy = ply

    # BG IMG
    screen.blit(background_image, [0, 0])

    # player.plrect.center = (player.x, player.y)

    #BOX
    box1.draw()
    #FINISH
    finish.draw()

    if abs(plx - spikex) < 63 and abs(ply - spikey) < 16:
        plx = 120
        ply = 528.5
        pljump = True
        rvel = 0
        lvel = 0
        jumpvel = 0
        hp -= 1

    elif abs(plx - spikex) < 32 and abs(ply - spikey) < 32:
        plx = 120
        ply = 528.5
        rvel = 0
        lvel = 0
        jumpvel = 0
        pljump = True
        hp -= 1

    elif abs(plx - spikex) < 16 and abs(ply - spikey) < 48:
        plx = 120
        ply = 528.5
        rvel = 0
        lvel = 0
        jumpvel = 0
        pljump = True
        hp -= 1

    elif abs(plx - spikex) < 8 and abs(ply - spikey) < 64:
        plx = 120
        ply = 528.5
        rvel = 0
        lvel = 0
        jumpvel = 0
        pljump = True
        hp -= 1

    # GRAVITY and JUMP
    ply += 5
    if ply >= yground and pljump == False:
        ply = yground
    elif pljump == True:
        ply -= jumpvel * 0.3
        jumpvel -= 1
        if ply >= yground:
            pljump = False
            jumpvel = 50

    # MOVEMENT
    if plleft == True:
        plx -= 3
        lvel = 1
    if plleft == False and lvel > (1 - 1):  # 0 wasnt working xD
        lvel -= 0.05
        plx -= 3 * lvel

    if plright == True:
        plx += 3
        rvel = 1
    if plright == False and rvel > (1 - 1):
        rvel -= 0.05
        plx += 3 * rvel

    if plx < 32:
        plx = 32
    elif plx > 1048:
        plx = 1048

            # COLLISION /W A BOX

    if abs(boxx - plx) < 64 and abs(boxy - ply) < 64:
        plx = startposx

    elif abs(boxx - plx) < 64 and abs(boxy - ply) >= 64:
        yground = 528.5 - 65

    else:
        yground = 528.5

        # FINISH

    if plx > finx - 64:
        win = True
        running = False
        print("GG")

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                if pljump == False:
                    pljump = True
            if event.key == pygame.K_LEFT:
                plleft = True
            if event.key == pygame.K_RIGHT:
                plright = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                plleft = False
            if event.key == pygame.K_RIGHT:
                plright = False

    if hp == 3:
        screen.blit(hp3, [10, 20])

    elif hp == 2:
        screen.blit(hp2, [10, 20])

    elif hp == 1:
        screen.blit(hp1, [10, 20])

    else:
        running = False
        lose = True

    player.move(plx, ply)
    player.draw()

    spike1.draw()

    while lose:
        screen.blit(lose_bkg, [0, 0])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lose = False

    while win:
        screen.blit(win_bkg, [0, 0])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                win = False

    pygame.display.update()

# AFTER CLOSING


pygame.quit()
