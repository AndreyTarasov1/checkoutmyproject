
"Игра под названием: Война самолетов"

from superwires import games, color
import random

games.init(screen_width=850, screen_height=900, fps=60)

games.pygame.display.set_caption("The war of planes")
icon = games.pygame.image.load("icon1.jpg")
games.pygame.display.set_icon(icon)

class PlayerPlane(games.Sprite):
    '''Создание самолета главного героя'''
    image = games.load_image('playerplane1.png')
    counter_heathbar = 1
    def __init__(self):
        super().__init__(image=PlayerPlane.image,
                         x = games.screen.width/2, 
                         y = games.screen.height/2,
                         )
        
        self.hp = 5
        self.count_shoot = 0
        
        self.heathbar5 = Heathbar(100, 50, 5)
        self.heathbar4 = Heathbar(100, 50, 4)
        self.heathbar3 = Heathbar(100, 50, 3)
        self.heathbar2 = Heathbar(100, 50, 2)
        self.heathbar1 = Heathbar(100, 50, 1)
        self.heathbar0 = Heathbar(100, 50, 0)

    def update(self):
        if PlayerPlane.counter_heathbar == 1:
            games.screen.add(self.heathbar5)
            PlayerPlane.counter_heathbar += 1

        
            
        
        if games.keyboard.is_pressed(games.K_d) > 0:
            self.x += 5
        elif games.keyboard.is_pressed(games.K_a) > 0:
            self.x -= 5

        if games.keyboard.is_pressed(games.K_s) > 0:        # Управление кнопками
            self.y += 5
        elif games.keyboard.is_pressed(games.K_w) > 0:
            self.y -= 5

        if self.x < 0:
            self.x += 5
        elif self.x > games.screen.width:
            self.x -= 5
                                            
        if self.y < 300:
            self.y += 5                                     #Проверка границ
        elif self.y > games.screen.height:
            self.y -= 5
            

        if games.keyboard.is_pressed(games.K_SPACE) > 0:
            if self.count_shoot == 30:
                self.shoot()
                self.count_shoot = 0
            
            else:
                self.count_shoot += 1
                
                
            
            
    def shoot(self):
        bullet_player = Bullet(self.x, self.y - 50)          #Создание пули игрока
        games.screen.add(bullet_player)
        

    def check_collide(self):
            for bullet_enemy in self.overlapping_sprites:    #Проверка на столкновение со спрайтами
                plane.die()
                bullet_enemy.die()
                
    def die(self):
        
        self.hp -= 1
        if self.hp == 4:
            self.heathbar5.destroy()
            games.screen.add(self.heathbar4)
        elif self.hp == 3:
            self.heathbar4.destroy()
            games.screen.add(self.heathbar3)
        elif self.hp == 2:
            self.heathbar3.destroy()
            games.screen.add(self.heathbar2)
        elif self.hp == 1:                                   #Жизни игрока
            self.heathbar2.destroy()
            games.screen.add(self.heathbar1)
        elif self.hp == 0:
            self.heathbar1.destroy()
            games.screen.add(self.heathbar0)            
            EnemyPlane.hop = 0   
            end_message = games.Message(value='Вы проиграли',
                                    size=90,
                                    color=color.white,
                                    x=games.screen.width/2,
                                    y=games.screen.height/2,
                                    lifetime=5*games.screen.fps,
                                    after_death=games.screen.quit,
                                    is_collideable=False)
            games.screen.add(end_message)
            

            count_message = games.Message(value='Побеждено врагов:'+ EnemyPlane.count_str,
                                    size=90,
                                    color=color.white,
                                    x=games.screen.width/2,
                                    y=games.screen.height/2 + 80,
                                    lifetime=5*games.screen.fps,
                                    after_death=games.screen.quit,
                                    is_collideable=False)
            games.screen.add(count_message)
            

            death_effect = Explosion(self.x, self.y)         #Создание анимации смерти
            games.screen.add(death_effect)
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

        if self.y < 0 or self.y > 900:                     #Проверка границ если True, то уничтожается
            self.destroy()
        
    def check_collide(self):
            for sprite in self.overlapping_sprites:         #Проверка столкновения пули со спрайтом
                self.destroy()
                sprite.die()
                
    def die(self):
        self.destroy()

class Heathbar(games.Sprite):
    '''Создание шкалы здоровья'''
    heathbar1 = games.load_image('heathbar1.png')
    heathbar2 = games.load_image('heathbar2.png')               # шкала здоровья врага
    
    heathbar_player5 = games.load_image('heathbar_player5.png')
    heathbar_player4 = games.load_image('heathbar_player4.png')
    heathbar_player3 = games.load_image('heathbar_player3.png') # шкала здоровья героя
    heathbar_player2 = games.load_image('heathbar_player2.png')
    heathbar_player1 = games.load_image('heathbar_player1.png')
    heathbar_player0 = games.load_image('heathbar_player0.png')
    def __init__(self, x, y, a):
        if a == 10:
            super().__init__(image=Heathbar.heathbar1,
                             x = x,
                             y = y - 60
                             )
        elif a == 20:
            super().__init__(image=Heathbar.heathbar2,
                             x = x,
                             y = y - 60
                             )
        elif a == 5:
            super().__init__(image=Heathbar.heathbar_player5,
                             x = x,
                             y = y
                             )
        elif a == 4:
            super().__init__(image=Heathbar.heathbar_player4,
                             x = x,
                             y = y
                             )
        elif a == 3:
            super().__init__(image=Heathbar.heathbar_player3,
                             x = x,
                             y = y
                             )
        elif a == 2:
            super().__init__(image=Heathbar.heathbar_player2,
                             x = x,
                             y = y
                             )
        elif a == 1:
            super().__init__(image=Heathbar.heathbar_player1,
                             x = x,
                             y = y
                             )
        else:
            super().__init__(image=Heathbar.heathbar_player0,
                             x = x,
                             y = y
                             )
    def die(self):
        pass


    

class EnemyPlane(games.Sprite):
    '''Создание вражеского самолета'''
    image1 = games.load_image('playerplane1.png')
    image2 = games.load_image('enemy_plane2.png')
    count = 0
    count_str = str(count)
    g = 1
    r = 1
    hop = 1
    level = 1
    
    def __init__(self, x, p):
        if p == 1:
            super().__init__(image=EnemyPlane.image1,
                                 angle = 180,
                                 x = x,
                                 y = random.randint(50, 180)),

        else:
            super().__init__(image=EnemyPlane.image2,
                                 angle = 180,
                                 x = x,
                                 y = 150),
        self.hp = 3      
        self.heathbar1 = Heathbar(self.x, self.y, 10)
        self.heathbar2 = Heathbar(self.x, self.y, 20)
        self.count_shoot = 0
        self.count_heathbar1 = 0
        self.count_heathbar2 = 0
        self.x1 = 0
        
            
            
        
    def update(self):
        EnemyPlane.count_str = str(EnemyPlane.count)
        if games.keyboard.is_pressed(games.K_p) > 0:
            self.level_2()
        
                
        if EnemyPlane.hop != 0:
            if self.count_shoot > random.randint(60, 130): #Задержка выстрела и сам выстрел
                self.shoot()
                self.count_shoot = 0
            else:
                self.count_shoot += 1
                

        if self.hp == 2:
            if self.count_heathbar1 == 60:              #Уничтожение heathbar1 
                self.heathbar1.destroy()
            else:
                self.count_heathbar1 += 1
                
                
        if self.hp == 1:
            
            if self.count_heathbar2 == 60:              
                self.heathbar2.destroy()                #Уничтожение heathbar2
            else:
                self.count_heathbar2 += 1
        
        self.check_collide()
        
        

            
    def check_collide(self):
         
            for sprite in self.overlapping_sprites:
                if isinstance(sprite, Bullet): #Проверка на столкновение со спрайтом
                    sprite.die()
                    self.die()
                

                    
    def shoot(self):
            bullet_enemy = Bullet(self.x, self.y + 80, 10, 180)     #Создание вражеской пули
            games.screen.add(bullet_enemy)
            
            
    def die(self):
        self.hp -= 1
        if self.hp == 2:
            games.screen.add(self.heathbar1)

            
       
        elif self.hp == 1:
            self.counter_heathbar2 = 0
            self.heathbar1.destroy()
            games.screen.add(self.heathbar2)
            
            
                   
        elif self.hp == 0:
            EnemyPlane.count += 1
            EnemyPlane.count_str = str(EnemyPlane.count)

            self.heathbar2.destroy()

            if EnemyPlane.count == 5:
                EnemyPlane.level += 1
                end_message = games.Message(value='Уровень 2',
                                    size=90,
                                    color=color.white,
                                    x=games.screen.width/2,
                                    y=games.screen.height/2,
                                    lifetime=5*games.screen.fps,
##                                    after_death=games.screen.quit,
                                    is_collideable=False)
                games.screen.add(end_message)
##                games.screen.background
                
                
            death_effect = Explosion(self.x, self.y)
            games.screen.add(death_effect)
            self.destroy()
            
    def level_2(self): 
        self.hp = 0
        for i in range(1):
                    enemy = EnemyPlane(200, 2)
                    self.hp = 3
                    self.x1 += 200
                    games.screen.add(enemy)
        
        

class Text(games.Message):
    count = 1
    def __init__(self, count_str, a):
        super().__init__(value='Побеждено врагов:'+ count_str + '/5',
                                    size=50,
                                    color=color.white,
                                    x=650,
                                    y=30,
                                    lifetime=-1,
                                    is_collideable=False)

        self.a = a
    def update(self):
        if Text.count < EnemyPlane.count:
            self.destroy()
            Text.count += 1
            text = Text(EnemyPlane.count_str, 1)
            games.screen.add(text)
        
            
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
    
        sky_image = games.load_image('sky.jpg')
        games.screen.background = sky_image

        # создание корабля, которым будет управлять игрок
        plane = PlayerPlane()
        games.screen.add(plane)

    
##      games.music.load("musicgame.mid") #сделать чтобы при выходе выключалась и жизнь игрока и полоска жизни у врага
##      games.music.play(-1)
        
        x = 250
        for i in range(5):
            enemy = EnemyPlane(x, 1)
            games.screen.add(enemy)
            x += 100
            
        games.screen.mainloop()

# поехали!
if __name__ == "__main__":
    main()

##    games.music.load("musicgame.mid") #сделать чтобы при выходе выключалась и жизнь игрока и полоска жизни у врага
##    games.music.play(-1)


##plane = PlayerPlane()
##games.screen.add(plane)






#Сделать уровни сложности
