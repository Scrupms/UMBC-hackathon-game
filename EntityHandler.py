# Example file showing a basic pygame "game loop"
import pygame
import Main
import math
tps=Main.tps
gForce=-5
id=0
def NextID(this):
        id+=1
        Main.id=id
class Entity:

    
    
    def __init__(this,x=0,y=0,type="NA",sprite="NA"): # Variables that likely need to be added: Health, Velocity, possibly an invincible tag?
        global id
        this.id=id
        NextID()
        this.x=x
        this.y=y
        this.type=type
        this.sprite=sprite
        this.id = id

    def updatePosition(this,xChange=0,yChange=0):
        this.x+=xChange
        this.y+=yChange

        
        

    

    def __str__(this):
        return f"id={this.id}, x={this.x}, y={this.y}, type={this.type}"

    def step(this):
        pass

class LivingEntity(Entity):
    def __init__(this, x=0, y=0, type="NA", sprite="NA", health=-1):
        super().__init__(x, y, type, sprite)
        this.health=health

class Projectile(Entity):
    #Angle 0=> to the right
    def __init__(this, x=0, y=0, type="NA", sprite="NA",velocityX="0",velocityY="0",angle=0): 
        super().__init__(x, y, type, sprite)

    def ProjectileStep(this):
        this.x+=this.velocityX
        this.y+=this.velocityY
        this.angle=math.tan(this.velocityY,this.velocityX)

class GravityProjectile(Projectile):
    def ProjectileStep(this):
        this.velocityY+=gForce/tps^2
        return super().ProjectileStep()
        

        

class Dog(LivingEntity): #this is a test class, it is not to be used outside of testing.
    def __init__(this, x=0, y=0):
        super().__init__(x, y, "DOG","DOG",67)
        

    def __str__(this):
        return f"{super().__str__()}, sprite={this.sprite} "
        

e1= Entity()
e2=Entity(1,2,"DOG")

j3 = Dog()

print("printing ids")
print(e1.id)
print(e2.id)
print("printing objects")
print(e1)
print(e2)
print(j3)


"""
Entity variables]
- x
- y
-type (the type of enemy that it is), actually maybe gonna use a subclass instead

"""