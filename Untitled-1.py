from pygame import *
font.init()
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
sprite1 = Player('Без имени.png', 30,30,30,200,5)
sprite2 = Player('Без имени.png', 600,400,30,200,5)
ball = Player("myachik.png",400,200,30,30,3)


game = True
finish = False
clock = time.Clock()
FPS = 60
speed_x = 3
speed_y = 3
font1 = font.Font(None, 35)
lose1 = font1.render('Player 1 lose!',True,(180,0,0))
font2 = font.Font(None, 35)
lose2 = font1.render('Player 2 lose!',True,(180,0,0))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if sprite.collide_rect(sprite1,ball) or sprite.collide_rect(sprite2,ball):
        speed_x *= -1
    if ball.rect.y >  500 - 50 or ball.rect.y < 0:
        speed_y *= -1
    if ball.rect.x < 0:
        finish = True
        main_win.blit(lose1,(200,200))
    if ball.rect.x > 700:
        finish = True
        main_win.blit(lose2,(200,200))


        

            


    if finish != True:          
        main_win.blit(background,(0,0))
        sprite1.update_l()
        sprite2.update_r()
        ball.update()
        ball.reset()
        sprite1.reset()
        sprite2.reset()

    clock.tick(FPS)
    display.update()


        
        