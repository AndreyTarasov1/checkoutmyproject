from superwires import games, color
import random, time




games.init(screen_width=850, screen_height=900, fps=60)

class PlayerPlane(games.Sprite):
    '''Создание самолета главного героя'''
    image = games.load_image('playerplane1.png')
    
    def __init__(self):
        super().__init__(image=PlayerPlane.image,
                         x = games.screen.width/2, 
                         y = games.screen.height/2,
                         )
        self.last_shot = 0  
        self.hp = 5

    def update(self):

        
        if games.keyboard.is_pressed(games.K_d) > 0:
            self.x += 5
        elif games.keyboard.is_pressed(games.K_a) > 0:
            self.x -= 5

        if games.keyboard.is_pressed(games.K_s) > 0:    # Управление кнопками
            self.y += 5
        elif games.keyboard.is_pressed(games.K_w) > 0:
            self.y -= 5

        if self.x < 0:
            self.x += 5
        elif self.x > games.screen.width:
            self.x -= 5
                                            #Проверка границ
        if self.y < 300:
            self.y += 5
        elif self.y > games.screen.height:
            self.y -= 5
            
        if games.keyboard.is_pressed(games.K_SPACE) > 0:
            current_time = time.time()
            if current_time - self.last_shot >= 0.5:     #Атака на пробел с задержкой 0.5 сек
                self.shoot()
                self.last_shot = current_time  
            
            
    def shoot(self):
        bullet_player = Bullet(self.x, self.y - 50)     #Создание пули игрока
        games.screen.add(bullet_player)

    def check_collide(self):
            for bullet_enemy in self.overlapping_sprites:   #Проверка на столкновение со спрайтами
                plane.die()
                bullet_enemy.die()
                
    def die(self):
        
        self.hp -= 1
        if self.hp == 2:
            pass
        elif self.hp == 1:      #Жизни игрока
            pass
        elif self.hp == 0:

            ep = Explosion(self.x, self.y)  #Создание анимации смерти
            games.screen.add(ep)
            self.destroy()

class Bullet(games.Sprite):
    '''Создание пули'''
    image_bullet = games.load_image('bullet.png')
    
    def __init__(self, x, y, dy=-10, angle=0):
        super().__init__(image=Bullet.image_bullet,
                         x = x,
                         y = y,
                         dy = dy,
                         angle = angle,
                        )
        
    def update(self):
        self.check_collide()

        if self.y < 0 or self.y > 900: #Проверка границ если True, то уничтожается
            self.destroy()
        
    def check_collide(self):
            for sprite in self.overlapping_sprites: #Проверка столкновения пули со спрайтом
                self.destroy()
                sprite.die()
                
    def die(self):
        self.destroy()

class Heathbar(games.Sprite):
    '''Создание шкалы здоровья'''
    heathbar1 = games.load_image('heathbar1.png')
    heathbar2 = games.load_image('heathbar2.png')
    count = 0
    def __init__(self, x, y, a):
        if a == 1:
            super().__init__(image=Heathbar.heathbar1,
                             x = x,
                             y = y - 60
                             )
        elif a == 2:
            super().__init__(image=Heathbar.heathbar2,
                             x = x,
                             y = y - 60
                             )
        
        
    def update(self):
        if Heathbar.count % 2 == 0 and Heathbar.count != 0: #Попытка сделать уничтожение hethbar_1(неудачно)
            self.destroy()
            Heathbar.count += 1
            
    def die(self):
        self.destroy()

            
            


class EnemyPlane(games.Sprite):
    '''Создание вражеского самолета'''
    image = games.load_image('playerplane1.png')
    count = 0
    def __init__(self, x):
        super().__init__(image=EnemyPlane.image,
                         angle = 180,
                         x = x,
                         y = random.randint(50, 180),
                         )

        self.hp = 3      
        self.last_shot = 0
        
        
    def update(self):
            current_time = time.time()
            if current_time - self.last_shot >= random.randint(2, 4):       #Выстрел врага
                self.shoot()
                self.last_shot = current_time
   
            self.check_collide()           

            
    def check_collide(self):
        
         if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:     #Проверка на столкновение со спрайтом
                sprite.die()
                self.die()

                    
    def shoot(self):
            bullet_enemy = Bullet(self.x, self.y + 80, 10, 180)     #Создание вражеской пули
            games.screen.add(bullet_enemy)
            
    def die(self):
        self.hp -= 1
        if self.hp == 2:
            heathbar_1 = Heathbar(self.x, self.y, 1)
            games.screen.add(heathbar_1)
            print(Heathbar.count)
            
            
        elif self.hp == 1:
            Heathbar.count += 1
            heathbar_1 = Heathbar(self.x, self.y, 2)                #Жизни противника
            games.screen.add(heathbar_1)
            print(Heathbar.count)
           
        elif self.hp == 0:
            EnemyPlane.count += 1
            Heathbar.count += 1
            print(Heathbar.count)
            if EnemyPlane.count == 5:
                end_message = games.Message(value="Конец игры",
                                    size=90,
                                    color=color.white,
                                    x=games.screen.width/2,
                                    y=games.screen.height/2,
                                    lifetime=5*games.screen.fps,
                                    after_death=games.screen.quit,
                                    is_collideable=False)
                games.screen.add(end_message)
            ep = Explosion(self.x, self.y)
            games.screen.add(ep)
            self.destroy()        

            
class Explosion(games.Animation):
    """ Анимированный взрыв """
    sound = games.load_sound("explosion.wav")
    images = ["explosion1.bmp",
              "explosion2.bmp",
              "explosion3.bmp",
              "explosion4.bmp",
              "explosion5.bmp",
              "explosion6.bmp",
              "explosion7.bmp",
              "explosion8.bmp",
              "explosion9.bmp"]

    def __init__(self, pos_x, pos_y):
        super().__init__(images=Explosion.images,
                         x=pos_x, y=pos_y,
                         repeat_interval=5, n_repeats=1,
                         is_collideable=False)
        Explosion.sound.play()



def main():
        

##    games.music.load("musicgame.mid") #сделать чтобы при выходе выключалась и жизнь игрока и полоска жизни у врага
##    games.music.play(-1)

    plane = PlayerPlane()
    games.screen.add(plane)

    sky_image = games.load_image('sky.jpg')
    games.screen.background = sky_image

    x = 250
    for i in range(5):
            enemy = EnemyPlane(x)
            games.screen.add(enemy)
            x += 100


       
       

            
    games.screen.mainloop()
if __name__ == "__main__":
    main()
