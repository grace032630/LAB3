import pygame
import math
import os
from settings import PATH

pygame.init()
ENEMY_IMAGE = pygame.image.load(os.path.join("images", "enemy.png"))


class Enemy:
    def __init__(self):
        self.width = 40
        self.height = 50
        self.image = pygame.transform.scale(ENEMY_IMAGE, (self.width, self.height))
        self.health = 5
        self.max_health = 10
        self.path = PATH
        self.path_index = 0
        self.move_count = 0
        self.stride = 1
        self.x, self.y = self.path[0]
        
    def draw(self, win):
        # draw enemy
        win.blit(self.image, (self.x - self.width // 2, self.y - self.height // 2))
        # draw enemy health bar
        self.draw_health_bar(win)

    def draw_health_bar(self, win):
        """
        Draw health bar on an enemy
        :param win: window
        :return: None
        """
        h=5
        pygame.draw.rect(win,(250,0,0),[int(self.x),int(self.y-25),int(self.max_health),h])#紅色
        pygame.draw.rect(win,(0,250,0),[int(self.x),int(self.y-25),int(self.health),h])#綠色
        # ...(to be done)
        pass

    def move(self):
        """
        Enemy move toward path points every frame
        :return: None
        """
       
        PATH = [(22, 308), (52, 283), (84, 283), (110, 305), (116, 341), (115, 375), (112, 405), (116, 433),
          (135, 455), (159, 475), (188, 480), (217, 481), (243, 474), (267, 463), (291, 454), (315, 441),
          (334, 423), (343, 398), (339, 368), (328, 345), (305, 331), (282, 322), (264, 303), (255, 283),
          (259, 259), (274, 239), (294, 225), (318, 214), (347, 212), (373, 217), (394, 230), (410, 250),
          (429, 266), (446, 282), (465, 295), (483, 310), (502, 321), (523, 309), (535, 282), (535, 254),
          (533, 230), (532, 190)]
        p_A=self.path[self.path_index]
        p_B=self.path[self.path_index+1]
        ax, ay = p_A  # x, y position of point A
        bx, by = p_B  # x, y position of point B
        distance_A_B = math.sqrt((ax - bx)**2 + (ay - by)**2)
        max_count = int(distance_A_B / self.stride)  # total footsteps that needed from A to B
        unit_vector_x = (bx - ax) / distance_A_B
        unit_vector_y = (by - ay) / distance_A_B
        delta_x = unit_vector_x * self.stride
        delta_y = unit_vector_y * self.stride
        if self.move_count < max_count:            
            self.x += delta_x
            self.y += delta_y
            self.move_count += 1 
        else:
            self.path_index+=1
            self.move_count=0
            
        # ...(to be done)
        

class EnemyGroup:
    def __init__(self):
        self.gen_count = 0
        self.gen_period = 120   # (unit: frame)
        self.reserved_members = []
        self.expedition = []  # don't change this line until you do the EX.3 
        
    def campaign(self):#第三題
        """
        Send an enemy to go on an expedition once 120 frame
        :return: None
        """
    #按下n鍵出現3個敵人
        
        if self.gen_count==self.gen_period and len(self.reserved_members)>0:
            self.expedition.append(self.reserved_members.pop())
            self.gen_count=0
        elif self.gen_count<self.gen_period:
            self.gen_count+=1
        
        # Hint: self.expedition.append(self.reserved_members.pop())
        # ...(to be done)

        pass

    def generate(self, num):#第三題
        """
        Generate the enemies in this wave
        :param num: enemy number
        :return: None
        """
        #if event.key == pygame.K_按下n鍵:
        while len(self.reserved_members)<num:
            self.reserved_members.append(Enemy())   
            
                                    
        # ...(to be done)
        
        pass
    def get(self):
        """
        Get the enemy list
        """
        return self.expedition

    def is_empty(self):
        """
        Return whether the enemy is empty (so that we can move on to next wave)
        """
        return False if self.reserved_members else True

    def retreat(self, enemy):
        """
        Remove the enemy from the expedition
        :param enemy: class Enemy()
        :return: None
        """
        self.expedition.remove(enemy)