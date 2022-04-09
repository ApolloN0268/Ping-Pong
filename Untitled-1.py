from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,w,h,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(w,h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        main_win.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500 - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500 - 80:
            self.rect.y += self.speed
        


main_win = display.set_mode((700,500))
display.set_caption("Шутер")
background = transform.scale(image.load("Dekoratsii-starogo-goroda-na-kinostudii-Mosfilm-700x500.jpg"),(700,500))
sprite1 = Player('Без имени.png', 30,30,65,120,5)
sprite2 = Player('Без имени.png', 500,400,65,120,5)


game = True
finish = False
clock = time.Clock()
FPS = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
            


    if finish != True:          
        main_win.blit(background,(0,0))
        sprite1.update_l()
        sprite2.update_r()
        sprite1.reset()
        sprite2.reset()

    clock.tick(FPS)
    display.update()


        
        