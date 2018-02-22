#Author: Fatima Abukar
#Pygame Simplified, API version II
import pygame,math,random,collections
import sys
pygame.init()


#Actor class where all the actors behaviours are determined 
class Actor(pygame.sprite.Sprite):
    
    #Initialise global variables in constructor
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #create an actors sprite group
        self.actors = pygame.sprite.Group()
        self.current_image = pygame.Surface([0, 0])
        self.image = self.current_image
        self.width = self.current_image.get_width()
        self.height= self.current_image.get_height()
        self.widthx = 700
        self.heightx =  400
        self.rect = self.image.get_rect()
        self.direction = 0
        self.imagex= self.current_image.get_width()
        self.x=0
        self.y=0
        self.dx=0
        self.dy=0
        self.speed=1
        self.rotation=0
        self.rect.x =self.x
        self.rect.y = self.y
        self.oldCenter = (100, 100)
        sys.setrecursionlimit(10000)
        
    #rotation for an actor is determined, called in update method    
    def __rotation(self):
        oldCenter = self.rect.center
        self.oldCenter = oldCenter
        self.image = pygame.transform.rotate(self.current_image, self.rotation)
        self.rect = self.image.get_rect()
        self.rect.center = oldCenter
        
    #gets the sprites position by adding dx, dy      
    def __Position(self):
        self.x += self.dx 
        self.y += self.dy
        
    #update the dx and dy     
    def __update_dx_dy(self):
        dy =self.dy
        dx =self.dx
        radians = math.atan2(dy,dx)
        
    #updates position, rotation and dx, dy
    def update(self):
        self.oldCenter = self.rect.center
        self.__rotation()
        self.__Position()
        self.__update_dx_dy()
        self.rect.center = (self.x, self.y)
        pygame.display.update()
        
    #set the location of the actor   
    def set_location(self, x,y):
        self.x= x
        self.y= y
        
    #set the image of the actor    
    def set_image(self, image):
        self.current_image = pygame.image.load(image)
        
    #actors rotation is set    
    def set_rotation(self, rotation):
        if rotation >= 360:
            rotation = rotation % 360
        elif rotation <0:
                rotation +(rotation % 360)
        if self.rotation != rotation:
            self.rotation = rotation
            
    ##checks if this object intecects with another object       
    def intersects(self, Actor):
        collision = False
        if self.rect.colliderect(Actor.rect):
            collision = True
        return collision
   
    #turns actor by amount    
    def turn(self, turn_by):
        rotation = self.rotation+turn_by
        self.set_rotation(rotation)
        
    #turns actor to face x, y position    
    def turn_towards(self, x,y):
        ##math.atan2 returns x and y on plane in radians
        ## get angle of x and y in radian        
        radians = math.atan2(y-self.y, x -self.x)
        #converting from radiants to degrees:
        degrees = radians * 180/math.pi
        self.set_rotation(degrees)
        
    #moves an actor by a distance      
    def move(self,distance):
        radians = (math.pi/180)
        self.dx = distance * math.cos(radians)
        self.dy = distance * math.sin(radians)
        
    #moves actor by x and y position
    def move_by(self, x,y):
        #distance of x        
        self.x= self.x+x*self.speed
        #distance of y
        self.y = self.y+y*self.speed

    #set the speed of an actor    
    def set_speed(self, speed):
        self.speed = speed

    #checks if mouse collides with an actor 
    def collide_point(self, pos):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return True
        return False
    
    #checks if a actor collides with a group of actors.    
    def collides_with(self, actor):
        collision= pygame.sprite.spritecollide(self,actor, False)
        if collision:
            return True
        return False

    
    #--------------------------------------------------------------------------------#
                #Multiple actors, and collisions for muliple actors    
    #--------------------------------------------------------------------------------#

    #iterator so the actors in the actors group can be looped through 
    def __iter__(self):
        return iter(self.actors)
    
    #make an actors group with a specified amount, set random location to world   
    def generate_rand_actors(self, number, image, World):
        for i in range(number):
            self.actor=Actor()
            self.add_actor(self.actor)
            for actor in self.actors:
                self.actor.x = random.randrange(World.width)
                self.actor.y = random.randrange(World.height-50)
                self.actor.set_image(image)
           
    #create actor group
    def make_actor_group(self):
        self.actors = pygame.sprite.Group()
        
    #remove an actor from the generate rand actors groups     
    def remove_actor_from_group(self):
        if self.actor_group_length()==0:
            raise Exception("You cant remove from an empty actors list.")
        else:
            for actors in self.actors:
                for k in range(1):
                    self.actors.remove(actors)
                break
    
    #draw actor group  
    def draw_actors(self,World):
        self.actors.draw(World)
        
    #add actor to actor group  
    def add_actor(self, *actor):
        self.actors.add(actor)

    #remove actor from actor group    
    def remove_actor(self, *actor):
        if self.actor_group_length()==0:
            raise Exception("You cant remove from an empty actors list.")
        else:
            self.actors.remove(actor)
            
    #get the length of the sprite group    
    def actor_group_length(self):
        return len(self.actors)
    
    #update the actors group   
    def update_actors(self):
        self.actors.update()
    
    #if actor collides with actor group, remove actor     
    def collide_group(self, actor):
         collision = pygame.sprite.spritecollide(actor, self.actors, True)
         if collision:
             return True
         return False
        
    
