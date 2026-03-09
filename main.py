from pygame import *
font.init()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_w, player_h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_w, player_h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_w, player_h):
        super().__init__(player_image, player_x, player_y, player_speed, player_w, player_h)
        self.start_x = player_x
        self.start_y = player_y
        self.is_jumping = False
        self.jump_progress = 0
        self.jump_height = 190
    def update(self):
        keys = key.get_pressed()
        if keys[K_SPACE] and not self.is_jumping and self.rect.y >= self.start_y:
            self.is_jumping = True
            self.jump_progress = 0
        if self.is_jumping:
            if self.jump_progress < self.jump_height:
                self.rect.y -= self.speed
                self.jump_progress += self.speed
                if self.rect.y < (self.start_y - self.jump_height):
                    self.rect.x += 250
            else:
                self.rect.y += self.speed
            if self.rect.y >= self.start_y:
                self.rect.y = self.start_y
                self.is_jumping = False
                self.jump_progress = False
        if self.rect.y == self.start_y and self.rect.x > self.start_x:
                self.rect.x -= 20
        if self.rect.x > win_w:
            self.rect.x = self.start_x
score = 0
class Rock(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_w, player_h):
        super().__init__(player_image, player_x, player_y, player_speed, player_w, player_h)
    def update(self):
        global score
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.rect.x = win_w
            score += 1
win_w = 1000
win_h = 600
mw = display.set_mode((win_w, win_h))
background = transform.scale(image.load('bg.png'), (win_w, win_h))
player = Player('lizard.png', 0, 450, 60, 150, 170)
rock = Rock('crystal.png', 900, 470, 20, 100, 100)
font_text = font.Font(None, 40)
text_lose = font_text.render('Поражение!', True, (255, 255, 255))
game = True
finish = False
while game:
    mw.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        player.reset()
        player.update()
        rock.reset()
        rock.update()
        score_text = font_text.render('Счет:'+str(score), True, (255, 255, 255))
        mw.blit(score_text, (0, 0))
    if player.rect.colliderect(rock.rect):
        finish = True
        mw.blit(text_lose, (450, 300))
        score_text = font_text.render('Счет:'+str(score), True, (255, 255, 255))
        mw.blit(score_text, (0, 0))
    time.Clock().tick(60)
    display.update()