import pygame
from ButtonHandler import Button

#import EntityHandler
id=0 
SCREENX=960
SCREENY=640
 #constant for the screen
entityArray=[]
screen=pygame.display.set_mode((SCREENX,SCREENY))
#tick setup
clock = pygame.time.Clock()
running =True
ticks = 0
tps=60 
currentState='Menu'


pygame.font.init()
pygame.init()
testFont=pygame.font.SysFont('comicsansms',50)
text=testFont.render('skibidi john pork',True,(255,255,255),(0,0,0))
textRect=text.get_rect()
textRect.center =(SCREENX//2,SCREENY//2)
musicPlaying = False

        
def PlayMusic(): #music player
    global musicPlaying
    pygame.mixer.music.unload()

    if currentState == 'Menu':
        pygame.mixer.music.load('Assets/Music/titlemenu.wav')
        pygame.mixer.music.play()
        musicPlaying = True
            
    if currentState == 'GamePlay':
        pygame.mixer.music.load('Assets/Music/maintheme.wav')
        pygame.mixer.music.play()
        musicPlaying = True




def QuitFunc():
    global running
    print('quit func called')
    quit()
    running=False
    pygame.quit()



def FireProjectile():
   # entityArray[id]= new Projecrtile # fix later
    #figure out how to make a bunch of objects without defining them as individual variables
    pass
class Game:
    global currentState
    def __init__(self):
        self.clock=pygame.time.Clock()
        self.display=pygame.display
        screen=self.display.set_mode((SCREENX,SCREENY))
        self.menu=Menu(screen, currentState)
        self.shop=Shop(screen, currentState)
        self.gamePlay=GamePlay(screen, currentState)
        self.states={'Menu':self.menu, 'Shop':self.shop, 'GamePlay':self.gamePlay}
        print('display up')
    

    def run():
        global ticks
        global currentState
        def GameEvent():
            global currentState
            global musicPlaying
            #print(f'Game Event called, tick={ticks}')
            for event in pygame.event.get():
                
                if event.type == pygame.MOUSEBUTTONDOWN:  
                    pygame.mixer.music.load('Assets/Music/powerupsound.wav')
                    pygame.mixer.music.play()                              
                    if startButton.checkForInput(pygame.mouse.get_pos()):
                        print('Start Button Pressed')
                        currentState='GamePlay'
                        musicPlaying=False
                        pygame.mixer.music.load('Assets/Music/powerupsound.wav')
                        pygame.mixer.music.play()
                if event.type == pygame.QUIT:
                    QuitFunc()
        #main game loop (?)
        if running:
            print('running')
        while running:
            GameEvent()



            global musicPlaying

            match currentState:
                case 'Menu':
                    print('Menu called')
                    screen.blit(pygame.image.load('Assets/Photos/screens/titlescreen.png'))
                    startButton = Button(pygame.image.load('Assets/Photos/screens/playbutton.png'), pygame.image.load('Assets/Photos/screens/playbutton.png'), 760, 510)
                    screen.blit(startButton.getSurface(), startButton.getRect())
                    if not musicPlaying:
                        PlayMusic()
                case 'GamePlay':
                    
                    print('Gameplay called')

                    screen.blit(pygame.image.load('Assets/Photos/screens/gamescreen.png'))
                    player = pygame.image.load('Assets/Photos/king/kingmiddle.png')
                    waveWorm=pygame.image.load('Assets/Photos/ui/waveworm.png')
                    screen.blit(waveWorm)
                    playerRect=player.get_rect(center=(SCREENX/2, SCREENY/2))
                    screen.blit(player,playerRect)
                    
                    kingSprite=pygame.surface
                    if not musicPlaying:
                        PlayMusic()
                    

                

                
            ticks += 1
            text=testFont.render(f'tick={ticks}',True,(255,255,255),(0,0,0))
            
            

            
                    
            pygame.display.update()
            
            clock.tick(60)





#start screen
class Menu:
    def __init__(self, display, gameStateManager):
        self.display=display
        currentState=gameStateManager
    #run()

        
#shop screen
class Shop:
    def __init__(self, display, gameStateManager):
        self.display=display
        currentState=gameStateManager
    #def run(self):
        
        self.display.fill('cyan')
#screen for main gameplay
class GamePlay:
    def __init__(self, display, gameStateManager):
        self.display=display
        currentState=gameStateManager
    def run(self):
        self.display.fill('purple')




#runs the game
if True:
    Game.run()
