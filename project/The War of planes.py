  
"Игра под названием: Война самолетов"

from superwires import games, color
import random

games.init(screen_width=850, screen_height=1000, fps=60)

games.pygame.display.set_caption("The war of planes")
icon = games.pygame.image.load("icon1.jpg")
games.pygame.display.set_icon(icon)

class PlayerPlane(games.Sprite):
    '''Создание самолета главного героя'''
    image = games.load_image('playerplane1.png')
    counter_heathbar = 1
    start = 0
    g = 0
    diff = 0
    diff2 = 2
    diff3 = 2
    hp_diff = 5
    gameover =  games.load_sound("gameover.mp3")
    
    
    def __init__(self):
        super().__init__(image=PlayerPlane.image,
                         x = games.screen.width/2, 
                         y = games.screen.height/2,
                         )
        
        self.hp = 5
        self.count_shoot = 30
        self.f = 1
        self.t = 1
        self.h = 0
        
        self.heathbar5 = Heathbar(120, 950, 5)
        self.heathbar4 = Heathbar(120, 950, 4)
        self.heathbar3 = Heathbar(120, 950, 3)
        self.heathbar2 = Heathbar(120, 950, 2)
        self.heathbar1 = Heathbar(120, 950, 1)
        self.heathbar0 = Heathbar(120, 950, 0)
        
        self.start_message0 = games.Message(value='Добро пожаловать в The war of planes',
                                        size=60,
                                        color=color.purple,
                                        x=games.screen.width/2,
                                        y=games.screen.height/2 - 400,
                                        lifetime=-1,
                                        is_collideable=False)
        
        self.start_message1 = games.Message(value='Легкий уровень | нажмите 1',
                                        size=45,
                                        color=color.green,
                                        x=games.screen.width/2,
                                        y=games.screen.height/2 - 100,
                                        lifetime=-1,
                                        is_collideable=False)
        self.start_message2 = games.Message(value='Нормальный уровень | нажмите 2',
                                        size=45,
                                        color=color.yellow,
                                        x=games.screen.width/2,
                                        y=games.screen.height/2,
                                        lifetime=-1,
                                        is_collideable=False)
        self.start_message3 = games.Message(value='Сложный уровень | нажмите 3',
                                        size=45,
                                        color=color.red,
                                        x=games.screen.width/2,
                                        y=games.screen.height/2+100,
                                        lifetime=-1,
                                        is_collideable=False)
        self.start_message4 = games.Message(value='Выбирите сложность: ',
                                        size=70,
                                        color=color.purple,
                                        x=games.screen.width/2,
                                        y=games.screen.height/2 - 200,
                                        lifetime=-1,
                                        is_collideable=False)
        self.start_message5 = games.Message(value='Уровень 1',
                                            size=90,
                                            color=color.purple,
                                            x=games.screen.width/2,
                                            y=games.screen.height/2,
                                            lifetime=2*games.screen.fps,
                                            is_collideable=False)
                
    def update(self):
        if PlayerPlane.start == 0:
             
            if self.t == 1:
                
                games.screen.add(self.start_message0)
                games.screen.add(self.start_message1)
                games.screen.add(self.start_message2)
                games.screen.add(self.start_message3)
                games.screen.add(self.start_message4)
                self.t = 2


            elif games.keyboard.is_pressed(games.K_1):
                if self.h == 0:
                    PlayerPlane.g = 1
                    self.h = 1
                    
                    PlayerPlane.diff = 2
                    PlayerPlane.hp_diff = 3
                    PlayerPlane.diff3 = 3

                    
            elif games.keyboard.is_pressed(games.K_2):
                if self.h == 0:
                    PlayerPlane.g = 1
                    self.h = 1
                    PlayerPlane.diff = 3
                    

            elif games.keyboard.is_pressed(games.K_3):
                if self.h == 0:
                    PlayerPlane.g = 1
                    self.h = 1
                    PlayerPlane.diff = 5
                    PlayerPlane.diff2 = 3
                    PlayerPlane.diff3 = 5
                    
                    
                    
        if PlayerPlane.g == 1:       
            x = 250
            for i in range(PlayerPlane.diff):
                    enemy = EnemyPlane(x, y=random.randint(100, 200),hp=3, counter_plane=1)
                    games.screen.add(enemy)
                    x += 100
                    PlayerPlane.g = 2
                    games.screen.add(self.start_message4)

                    self.start_message0.destroy()
                    self.start_message1.destroy()
                    self.start_message2.destroy()
                    self.start_message3.destroy()
                    self.start_message4.destroy()

                    

        if PlayerPlane.counter_heathbar == 1:
            games.screen.add(self.heathbar5)
            PlayerPlane.counter_heathbar += 1
            
        if games.keyboard.is_pressed(games.K_p) and games.keyboard.is_pressed(games.K_o):       #Переход на Финальный уровень
             EnemyPlane.count = 7
             
        if games.keyboard.is_pressed(games.K_i) and games.keyboard.is_pressed(games.K_u):       #Переход на 2 уровень
             EnemyPlane.count = PlayerPlane.diff - 1
             
      
        if PlayerPlane.g == 2: 
            if games.keyboard.is_pressed(games.K_d):
                self.x += 5
            elif games.keyboard.is_pressed(games.K_a):
                self.x -= 5

            if games.keyboard.is_pressed(games.K_s):        # Управление кнопками
                self.y += 5
            elif games.keyboard.is_pressed(games.K_w):
                self.y -= 5

            if self.x < 45:
                self.x += 5
            elif self.x > games.screen.width - 45:
                self.x -= 5
                                                
            if self.y < 450:
                self.y += 5                                     #Проверка границ
            elif self.y > games.screen.height - 35:
                self.y -= 5

            

        if games.keyboard.is_pressed(games.K_SPACE):
            if self.count_shoot == 30:
                self.shoot()
                self.count_shoot = 0
            
            else:
                self.count_shoot += 1
                
        self.check_collide()
            
            
    def shoot(self):
        bullet_player = Bullet(self.x, self.y - 70)          #Создание пули игрока
        games.screen.add(bullet_player)
        
       
        

    def check_collide(self):
            for sprite in self.overlapping_sprites:
                if isinstance(sprite, Bullet) or isinstance(sprite, Fireball):#Проверка на столкновение со спрайтами
                    self.die()
                    sprite.destroy()
                elif isinstance(sprite, Ray) or isinstance(sprite, Boss):
                    self.die()
                elif isinstance(sprite, G):
                    sprite.destroy()
                    sprite.count = 2
                    self.hp += 3
                    self.die()
                    attack = Attack(self.x, self.y)
                    games.screen.add(attack)
                    
                
                    
                    
    def die(self):
        
        self.hp -= 1
        if self.hp >= 5:
            self.hp = 5
            PlayerPlane.counter_heathbar = 1
           
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
            EnemyPlane.stop_bullet = 0
            self.heathbar1.destroy()
            games.screen.add(self.heathbar0)
            PlayerPlane.gameover.play()
            end_message = games.Message(value='Game over',
                                    size=90,
                                    color=color.red,
                                    x=games.screen.width/2,
                                    y=games.screen.height/2-80,
                                    lifetime=5*games.screen.fps,
                                    after_death=games.screen.quit,
                                    is_collideable=False)
            games.screen.add(end_message)
            

            count_message = games.Message(value='Побеждено врагов: '+ str(EnemyPlane.count),
                                    size=90,
                                    color=color.white,
                                    x=games.screen.width/2,
                                    y=games.screen.height/2,
                                    lifetime=5*games.screen.fps,
                                    after_death=games.screen.quit,
                                    is_collideable=False)
            games.screen.add(count_message)

            level_message = games.Message(value='Пройдено уровней: '+ str(EnemyPlane.level) + '/3',
                                    size=90,
                                    color=color.white,
                                    x=games.screen.width/2,
                                    y=games.screen.height/2 + 80,
                                    lifetime=5*games.screen.fps,
                                    after_death=games.screen.quit,
                                    is_collideable=False)
            games.screen.add(level_message)

            death_effect = Explosion(self.x, self.y)         #Создание анимации смерти игрока
            games.screen.add(death_effect)
            self.destroy()

class Bullet(games.Sprite):
    '''Создание пули'''
    image_bullet = games.load_image('bullet.png')
    
    def __init__(self, x, y, dy=-10, dx=0, angle=0):
        super().__init__(image=Bullet.image_bullet,
                         x = x,
                         y = y,
                         dy = dy,
                         dx = dx,
                         angle = angle,
                         )
        
    def update(self):
        self.check_collide()

        if self.y < 0 or self.y > games.screen.height:                     #Проверка границ если True, то уничтожается
            self.destroy()
        
    def check_collide(self):
        for sprite in self.overlapping_sprites:
            if isinstance(sprite, Bullet):
                self.destroy()
                sprite.destroy()
            elif isinstance(sprite, Boss):
                self.destroy()
                
        
    

class Fireball(games.Sprite):
    '''Создание fireball врага'''
    image_fireball = games.load_image('fireball.png')
    
    def __init__(self, x, y, dy=10, dx=0, angle=0):
        super().__init__(image=Fireball.image_fireball,
                         x = x,
                         y = y,
                         dy = dy,
                         dx = dx,
                         angle = angle
                         )
    def update(self):
        if self.y > games.screen.height:
            self.destroy()
        
        self.check_collide()
        
    def check_collide(self):
            for sprite in self.overlapping_sprites:
                if isinstance(sprite, Bullet):              #Проверка на столкновение со спрайтом
                    sprite.destroy()


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

    
class SuperHit(games.Animation):
    images = ['wc111.png',
              'wc2.png',
              'wc3.png',
              'wc4.png',
              'wc5.png',
              'wc6.png',
              'wc7.png'
              ]
    def __init__(self, x, y, angle=90):
        super().__init__(images=SuperHit.images,
                         x=x,
                         y=y,
                         angle=angle,
                         repeat_interval=10,
                         n_repeats=1,
                         is_collideable=False)

        
class Ray(games.Sprite):
    image = games.load_image('ray.png')
    def __init__(self, x, y, angle=0):
        super().__init__(image=Ray.image,
                       x=x,
                       y=y,
                       angle=angle)
        self.time_count = 0
        
    def update(self):
        if self.time_count == 5:
            self.destroy()
        else:
            self.time_count += 1

            
class Attack(games.Sprite):
    image = games.load_image('attack.png')
    def __init__(self, x, y):
            super().__init__(image=Attack.image,
                             x=x,
                             y=y,
                             dy= -5,
                             angle=270)
        
        
            
class Boss(games.Sprite):
    image = games.load_image('boss.png')
    diamond = games.load_image('diamond.png')
    
    count = 1
    count2 = 1
    def __init__(self, count):
        if count == 1111:
            super().__init__(image=Boss.diamond,
                             x = games.screen.width/2,
                             y = 150)
            
            self.count = count
            
        else:
            super().__init__(image=Boss.image,
                             x = games.screen.width/2,
                             y = 150)
            self.hp = 3
            self.count_shoot = 0
            self.count_shoot2 = 0
            self.count_shoot3 = 0
            self.count2 = 0
            self.count4 = 0
            self.count5 = 1
            self.x1 = 0
            self.x2 = 230
            self.f = 0
            self.phase = 1
            self.f1 = 0
            self.f2 = 0
            self.v = 0
            self.count50 = 0
            self.count = 0
            self.r = 0
            self.star = Star(games.screen.width/2, games.screen.height/2 + 100)
            self.h = G(games.screen.width/2, games.screen.height/2 + 100)
            

            
    def update(self):
      if EnemyPlane.stop_bullet != 0:
        if self.count != 1111:
            if self.count_shoot2 != 11:
                if self.count_shoot > 20: 
                    self.count_shoot = 0
                    fireball = Fireball(self.x1, self.y + 100, angle=180)       #1 атака босса
                    games.screen.add(fireball)
                    self.x1 += 100
                    self.count_shoot2 += 1

                    self.phase = 1
                    Boss.count2 = 1
                else:
                    self.count_shoot += 1
                    
                    
            elif self.phase == 1:                                   
                if self.f == 60:
                    if self.count_shoot3 != 5:
                                fireball = Fireball(self.x2, 400, angle=180)    #2 атака босса
                                games.screen.add(fireball)
                                self.x2 += 100
                                self.count_shoot3 += 1
                                if self.count4 != 4:
                                    self.count4 += 1
                                else:
                                    self.phase = 2
                else:
                      self.f += 1
                      
            elif self.phase == 2:
                if self.f1 == 0:
                    if self.v == 60:
                        hit = SuperHit(self.x+10, self.y)
                        games.screen.add(hit)
                        self.f1 = 1
                    else:
                        self.v += 1
                elif self.f2 == 40:
                    ray = games.load_sound('ray.mp3')
                    ray.play()
                    ray = Ray(self.x, self.y+500)
                    games.screen.add(ray)
                    if self.f1 == 60:
                        self.phase = 3
                    else:
                        self.f1 += 1
                    
                else:
                    self.f2 += 1
                    
                    
                
                
            else:
                if self.count5 == 1:
                    if PlayerPlane.diff > 2:
                        enemy1 = EnemyPlane(self.x+200, 5, 2, 150, 330)
                        games.screen.add(enemy1)
                        enemy1 = EnemyPlane(self.x-200, 5, 2, 150, 330)
                        games.screen.add(enemy1)
                        
                    if PlayerPlane.diff != 3:    
                        enemy2 = EnemyPlane(self.x-100, 3, 1, y=400)
                        games.screen.add(enemy2)
                        enemy2 = EnemyPlane(self.x, 3, 1, y=400)
                        games.screen.add(enemy2)
                        enemy2 = EnemyPlane(self.x+100, 3, 1, y=400)
                        games.screen.add(enemy2)
                        
                    EnemyPlane.count2 = 0
                    self.count5 += 1

            
                elif EnemyPlane.count2 == PlayerPlane.diff3:
                    
                    if self.count50 == 0:  
                        games.screen.add(self.star)
                        games.screen.add(self.h)
                        self.count50 = 2
                        
                    if self.h.count == 2:
                            self.r = 0
                            superhit = games.load_sound('superhit.mp3')
                            superhit.play()
                            self.star.destroy()
                            self.h.destroy()
                            self.h.count = 0
                            EnemyPlane.count2 = 0
                            self.count5 = 1
                            self.phase = 0
                            self.f1 = 0
                            self.f2 = 0
                            self.count_shoot = 0
                            self.count_shoot2 = 0
                            self.count4 = 0
                            self.count_shoot3 = 0
                            self.x1 = 0
                            self.x2 = 230
                            self.f = 0
                            self.v = 0 
                            self.count50 = 0
                            
                    elif self.r == 240:
                            self.r = 0
                            superhit = games.load_sound('superhit.mp3')
                            superhit.play()
                            self.star.destroy()
                            self.h.destroy()
                            self.h.count = 0
                            EnemyPlane.count2 = 0
                            self.count5 = 1
                            self.phase = 0
                            self.f1 = 0
                            self.f2 = 0
                            self.count_shoot = 0
                            self.count_shoot2 = 0
                            self.count4 = 0
                            self.count_shoot3 = 0
                            self.x1 = 0
                            self.x2 = 230
                            self.f = 0
                            self.v = 0 
                            self.count50 = 0
                    else:
                        self.r += 1
                        

                            
            self.check_collide()
                    
    def check_collide(self):
            for sprite in self.overlapping_sprites:
                if isinstance(sprite, Attack):              #Проверка на столкновение со спрайтом
                    sprite.destroy()
                    self.die()

    def die(self):
            self.hp -= 1
            if self.hp == 2:
                pass
            elif self.hp == 1:
                pass
            elif self.hp == 0:
                self.win()

    def win(self):
            ex = Explosion(self.x, self.y)
            games.screen.add(ex)
            ex = Explosion(self.x-150, self.y-150)
            games.screen.add(ex)
            ex = Explosion(self.x-150, self.y+150)
            games.screen.add(ex)
            ex = Explosion(self.x+150, self.y+150)
            games.screen.add(ex)
            ex = Explosion(self.x+150, self.y-150)
            games.screen.add(ex)
            self.destroy()
            diamond = Boss(1111)
            games.screen.add(diamond)
            win = games.load_sound('win.mp3')
            win.play()
            count_message = games.Message(value='Победа',
                                    size=120,
                                    color=color.white,
                                    x=games.screen.width/2,
                                    y=games.screen.height/2,
                                    lifetime=5*games.screen.fps,
                                    after_death=games.screen.quit,
                                    is_collideable=False)
            games.screen.add(count_message)
            
            count_message = games.Message(value='Побеждено врагов: '+ str(EnemyPlane.count)+ '/23',
                                    size=90,
                                    color=color.white,
                                    x=games.screen.width/2,
                                    y=games.screen.height/2+100,
                                    lifetime=5*games.screen.fps,
                                    after_death=games.screen.quit,
                                    is_collideable=False)
            games.screen.add(count_message)


                
            
        


                    
class Star(games.Animation):
    images = ['star1.png',
              'star2.png',
              'star3.png',
              'star4.png',
              'star5.png',
              'star6.png',
              'star7.png']
    def __init__(self, x, y):
        super().__init__(images=Star.images,
                         x=x,
                         y=y,
                         repeat_interval=5,
                         n_repeats=-1,
                         is_collideable=False)
        
    
    

class G(games.Sprite):
    image = games.load_image('1232.png')
    def __init__(self,x,y):
        super().__init__(image=G.image,
                         x=x,
                         y=y)
        self.count = 1
                            
        
class EnemyPlane(games.Sprite):
    '''Создание вражеского самолета'''
    image1 = games.load_image('playerplane1.png')
    image2 = games.load_image('enemy_plane2.png')
    
    
    count = 0
    count2 = count
    g = 1
    stop_bullet = 1
    level = 0
    boss_count = 1
    message_count = 1
    
    def __init__(self, x, hp, counter_plane, sp=100, y=0):
        if counter_plane == 1:
            super().__init__(image=EnemyPlane.image1,
                                 angle = 180,
                                 x = x,
                                 y = y),
            self.hp = hp     
            self.heathbar1 = Heathbar(self.x, self.y, 10)
            self.heathbar2 = Heathbar(self.x, self.y, 20)
            self.count_shoot = 0
            self.count_heathbar1 = 0
            self.count_heathbar2 = 0
            self.sp = sp
            self.xx = 250
                            
        elif counter_plane == 2:
            super().__init__(image=EnemyPlane.image2,
                                 angle = 180,
                                 x = x,
                                 y = y),
            self.hp = hp     
            self.heathbar1 = Heathbar(self.x, self.y, 10)
            self.heathbar2 = Heathbar(self.x, self.y, 20)
            self.count_shoot = 0
            self.count_heathbar1 = 0
            self.count_heathbar2 = 0
            self.sp = sp
        else:
            super().__init__(image=EnemyPlane.image3,
                                 angle = 180,
                                 x = x,
                                 y = y),

            
            
        
    def update(self):
                
        if EnemyPlane.stop_bullet != 0:
                if self.count_shoot > random.randint(100, 180): #Задержка выстрела и сам выстрел
                    self.shoot()
                    self.count_shoot = 0
                else:
                    self.count_shoot += 1
            

        if self.hp == 2:
            if self.count_heathbar1 == 30:              #Уничтожение heathbar1 
                self.heathbar1.destroy()
            else:
                self.count_heathbar1 += 1
                
                
                
        if self.hp == 1:
            
            if self.count_heathbar2 == 30:              
                self.heathbar2.destroy()                #Уничтожение heathbar2
            else:
                self.count_heathbar2 += 1
        
        self.check_collide()
        
        

            
    def check_collide(self):
            for sprite in self.overlapping_sprites:
                if isinstance(sprite, Bullet):              #Проверка на столкновение со спрайтом
                    sprite.destroy()
                    self.die()
                    
                

                    
    def shoot(self):
        if self.sp == 150:
                bullet_enemy = Fireball(self.x-60 , self.y + self.sp, dy=10, dx=random.randint(-5,-1), angle=190)
                games.screen.add(bullet_enemy)
                bullet_enemy = Fireball(self.x, self.y + self.sp, dy=10, angle=180)
                games.screen.add(bullet_enemy)
                bullet_enemy = Fireball(self.x+60, self.y + self.sp, dy=10, dx=random.randint(1, 5),angle=170,)
                games.screen.add(bullet_enemy)
        else:
            bullet_enemy = Bullet(self.x, self.y + self.sp, 10, angle=180)
            games.screen.add(bullet_enemy)
            
    def die(self):
        self.hp -= 1
        if self.hp == 2:
            games.screen.add(self.heathbar1)

            
       
        elif self.hp == 1:
            self.heathbar1.destroy()
            games.screen.add(self.heathbar2)
            
            
                   
        elif self.hp == 0:
            EnemyPlane.count += 1
            EnemyPlane.count2 += 1

            self.heathbar2.destroy()
            death_effect = Explosion(self.x, self.y)
            games.screen.add(death_effect)
            

            if EnemyPlane.count == PlayerPlane.diff:
                EnemyPlane.level = 1
                level = games.load_sound('level.mp3')
                level.play()#Переход на второй уровень
  
                level_message = games.Message(value='Уровень 2',
                                    size=90,
                                    color=color.yellow,
                                    x=games.screen.width/2,
                                    y=games.screen.height/2,
                                    lifetime=games.screen.fps,
                                    is_collideable=False)
                games.screen.add(level_message)

                
                if EnemyPlane.g == 1:
                    for i in range(PlayerPlane.diff2):
                        space_image = games.load_image('space1.jpg')
                        games.screen.background = space_image
                        
                        enemy = EnemyPlane(self.xx, PlayerPlane.hp_diff, 2, 150, 150)
                        games.screen.add(enemy)
                        self.xx += 200
                        
                        EnemyPlane.g += 1
                        
            elif (PlayerPlane.diff == 5 and EnemyPlane.count > 7) or (PlayerPlane.diff == 3 and EnemyPlane.count > 4 ) or(PlayerPlane.diff == 2 and EnemyPlane.count > 3 ):
                EnemyPlane.level = 2
                if EnemyPlane.message_count == 1:
                    level = games.load_sound('level.mp3')
                    level.play()
                    level_message = games.Message(value='Финальный Уровень',
                                        size=90,
                                        color=color.yellow,
                                        x=games.screen.width/2,
                                        y=games.screen.height/2,
                                        lifetime=games.screen.fps,
                                        is_collideable=False)
                    games.screen.add(level_message)
                    EnemyPlane.message_count = 2
                    
                if EnemyPlane.boss_count == 1:
                    boss = Boss(123)
                    games.screen.add(boss)
                    EnemyPlane.boss_count += 1             
                    
                        
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

                sky_image = games.load_image('sky.jpg')
                games.screen.background = sky_image

                
                plane = PlayerPlane()
                games.screen.add(plane)
                
            
                games.music.load("musicgame.mid") #сделать чтобы при выходе выключалась и жизнь игрока и полоска жизни у врага
                games.music.play(-1)
                

                games.screen.mainloop()

if __name__ == '__main__':
    main()

#Заметки: меню паузы  сферы для босса сюжет 

