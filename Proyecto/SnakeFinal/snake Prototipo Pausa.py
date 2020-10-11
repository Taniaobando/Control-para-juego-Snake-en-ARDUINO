import pygame
from pygame import *
import time
import random
import sys


init()

display_width = 800
display_height = 600

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
blue = (0,0,128)
pink = (255,0,220)
yellow = (255,251,0)

gameDisplay = display.set_mode((display_width,display_height))
display.set_caption('Cybersnake')


gameExit = False
clock =pygame.time.Clock()

block_size = 10
pantallaintro = pygame.image.load("worldpixel.png")
perdiste = pygame.image.load("perdiste.png")
instru = pygame.image.load("instru.png")
rules = pygame.image.load("rules.jpg")
rules1 = pygame.image.load("rules1.png")
win = pygame.image.load("iwinx2.jpg")
lvl1 = pygame.image.load("lvl1.png")
lvl2 = pygame.image.load("lvl2.png")
Serp=pygame.image.load("snakeicon.png").convert_alpha()
blackScreen=pygame.image.load("blackScreen.jpg")



smallfont= pygame.font.SysFont("timesnewroman",30)
medfont= pygame.font.SysFont("timesnewroman",40)
largefont= pygame.font.SysFont("algerian",60)


font =font.SysFont(None,25)
def game_intro():
    intro= True
    Serp_pos_y=280
    gameDisplay.blit(Serp,(210,Serp_pos_y))
    pygame.display.update()
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and Serp_pos_y <= 380:
                    Serp_pos_y=Serp_pos_y+50
                if event.key == pygame.K_UP and Serp_pos_y >280:
                    Serp_pos_y=Serp_pos_y-50
                if event.key == pygame.K_SPACE:
                    if Serp_pos_y == 280:
                        intro=False
                        x=250
                        gameLoop()
                    if Serp_pos_y == 330:
                        pygame.quit()
                        sys.exit()
                        quit()
                    if Serp_pos_y == 380:
                        how_to_play1()
                        intro=False
                    if Serp_pos_y == 430:
                        how_to_play()
                        intro=False()
        gameDisplay.blit(pantallaintro,(0,0))
        message_to_screen("Bienvenido a Cybersnake", green,x_displace=0,y_displace=-200,size="large")
        message_to_screen("Atrapa las manzanas", red,x_displace=0,y_displace=-100,size="medium")
        message_to_screen("Jugar", white,x_displace=0, y_displace=0,size="small")
        message_to_screen("Salir", white,x_displace=0, y_displace=50,size="small")
        message_to_screen("Reglas", white,x_displace=0, y_displace=100,size="small")
        message_to_screen("Instrucciones", white,x_displace=0, y_displace=150,size="small")
        gameDisplay.blit(Serp,(210,Serp_pos_y))
        pygame.display.update()
        
    
def how_to_play():
    how=True
    while how:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    how = False
                    game_intro()
                    
        gameDisplay.blit(instru,(0,0))
        message_to_screen("COMO JUGAR", red,x_displace=0,y_displace=-200,size="large")
        message_to_screen("Controles:", red,x_displace=-200,y_displace=-100,size="medium")
        message_to_screen("Arriba: Joystick hacia arriba", white,x_displace=0,y_displace=-50,size="medium")
        message_to_screen("Abajo: Joystick hacia abajo", white,x_displace=0,y_displace=0,size="medium")
        message_to_screen("Izquierda: Joystick hacia la izquierda", white,x_displace=0,y_displace=50,size="medium")
        message_to_screen("Derecha: Joystick hacia la derecha", white,x_displace=0,y_displace=100,size="medium")
        message_to_screen("Presiona ENTER para volver al menú", white,x_displace=0, y_displace=200,size="medium")
        pygame.display.update()
        

def how_to_play1():
    how1=True
    while how1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    how1= False
                    how_to_play2()
                    
        gameDisplay.blit(rules,(0,0))
        message_to_screen("REGLAS", red,x_displace=0,y_displace=-250,size="large")
        message_to_screen("-Cuando atrapas una manzana ganas: 100 puntos", white,x_displace=0,y_displace=-180,size="small")
        message_to_screen("-Cuando pierdes una vida, se reinicia el nivel", white,x_displace=0,y_displace=-130,size="small")
        message_to_screen("-Si te tocas a ti mismo, pierdes una vida", white,x_displace=0,y_displace=-80,size="small")
        message_to_screen("-Si te chocas con un obstaculo, pierdes una vida", white,x_displace=0,y_displace=-30,size="small")
        message_to_screen("-Si te quedas sin vidas, PIERDES!", white,x_displace=0,y_displace=20,size="small")
        message_to_screen("-Si el tiempo termina, pierdes una vida!", white,x_displace=0,y_displace=70,size="small")
        message_to_screen("-Si consigues 4500 puntos, ganas una vida", white,x_displace=0,y_displace=120,size="small")
        message_to_screen("Presiona ENTER para seguir", white,x_displace=0,y_displace=250,size="small")
        pygame.display.update()

def how_to_play2():
    how2=True
    while how2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    how2= False
                    game_intro()
     
        gameDisplay.blit(rules1,(0,0))
        message_to_screen("REGLAS", red,x_displace=0,y_displace=-250,size="large")
        message_to_screen("-Al conseguir 3000 puntos aparecerá el portal azul ", white,x_displace=0,y_displace=-180,size="small")
        message_to_screen(" para pasar al siguiente nivel ",white,x_displace=0,y_displace=-130,size="small")
        message_to_screen("-Si atrapas la ayuda amarilla tus puntos irán x2", white,x_displace=0,y_displace=-80,size="small")
        message_to_screen("-Si atrapas el cuadrado verde", white,x_displace=0,y_displace=-30,size="small")
        message_to_screen("reduciras a la mitad tu tamaño y tus puntos", white,x_displace=0,y_displace=20,size="small")
        message_to_screen("-Si consigues 2000 puntos en el nivel 2, Ganas!", white,x_displace=0,y_displace=70,size="small")
        message_to_screen("-Si tocas las paredes en el nivel 2, pierdes una vida", white,x_displace=0,y_displace=120,size="small")
        message_to_screen("-Si atrapas el cuadrado rosa, aumenta tu velocidad", white,x_displace=0,y_displace=170,size="small")
        message_to_screen("Presiona ENTER para volver al menú", white,x_displace=0,y_displace=250,size="small")  
        pygame.display.update()
        
    
def snake(block_size, snakeList):
    for XnY in snakeList:  
        draw.rect(gameDisplay, black, [XnY[0],XnY[1],block_size,block_size])

def text_objects(text,color,size):
    if size== "small":
        textSurface=smallfont.render(text,True,color)
    elif size== "medium":
        textSurface=medfont.render(text,True,color)
    elif size== "large":
        textSurface=largefont.render(text,True,color)

    return textSurface, textSurface.get_rect()

def message_to_screen(msg,color,x_displace=0,y_displace=0,size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (display_width/ 2)+x_displace,(display_height/ 2)+y_displace
    gameDisplay.blit(textSurf, textRect)

def pause (nivel):
    pausa = True
    Serp_pos_y=280
    while pausa:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and Serp_pos_y < 350:
                    Serp_pos_y=Serp_pos_y+70
                if event.key == pygame.K_UP and Serp_pos_y > 280:
                    Serp_pos_y=Serp_pos_y-70
                if event.key == pygame.K_SPACE and Serp_pos_y<350:
                    game_intro()
                if event.key == pygame.K_SPACE and Serp_pos_y>280:
                    if nivel == 1:
                        gameDisplay.blit(lvl1,(0,0))
                        pausa=False
                    elif nivel == 2:
                        gameDisplay.blit(lvl2,(0,0))
                        pausa=False
                    
        gameDisplay.blit(blackScreen,(0,0))      
        message_to_screen("Juego en pausa", white,x_displace=0, y_displace=-110,size="large")
        message_to_screen("Volver al menú", white,x_displace=0, y_displace=0,size="small")
        message_to_screen("Reanudar partida", white,x_displace=0, y_displace=70,size="small")
        gameDisplay.blit(Serp,(230,Serp_pos_y))
        display.update() 
                    
def gameLoop():
    FPS=20
    t1=pygame.time.get_ticks()//1000
    puntaje=0
    nivel=1
    vida=3
    gameExit = False
    gameOver = False
    multiplicador=350
    cortador=0
    x=250
    contador_de_vida=4

    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 0
    lead_y_change = 0

    snakeList= []
    snakeLength = 1
    
    randAppleX= round (random.randrange(0, display_width - block_size)/10.0)*10
    randAppleY= round (random.randrange(0, display_height - block_size)/10.0)*10

    randPortalX= round (random.randrange(0, display_width - block_size)/10.0)*10
    randPortalY= round (random.randrange(0, display_height - block_size)/10.0)*10

    randHalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
    randHalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

    rand1HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
    rand1HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

    rand2HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
    rand2HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

    rand3HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
    rand3HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

    rand4HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
    rand4HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10
    
    randSpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
    randSpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10

    rand1SpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
    rand1SpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10 

    rand2SpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
    rand2SpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10 

    rand3SpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
    rand3SpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10 

    rand4SpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
    rand4SpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10 


    randMultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
    randMultiY= round (random.randrange(0, display_height - block_size)/10.0)*10

    rand1MultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
    rand1MultiY= round (random.randrange(0, display_height - block_size)/10.0)*10

    rand2MultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
    rand2MultiY= round (random.randrange(0, display_height - block_size)/10.0)*10

    rand3MultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
    rand3MultiY= round (random.randrange(0, display_height - block_size)/10.0)*10

    rand4MultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
    rand4MultiY= round (random.randrange(0, display_height - block_size)/10.0)*10
    
    if (randAppleX == randPortalX and randAppleY == randPortalY) or (randAppleX == randHalfX and randAppleY == randHalfY) or (randAppleX == rand1HalfX and randAppleY == rand1HalfY) or (randAppleX == rand2HalfX and randAppleY == rand2HalfY) or (randAppleX == rand3HalfX and randAppleY == rand3HalfY)or(randAppleX==rand4HalfX and randAppleY==rand4HalfY) or (randAppleX == randSpeedX and randAppleY == randSpeedY)or (randAppleX == rand1SpeedX and randAppleY == rand1SpeedY) or (randAppleX == rand2SpeedX and randAppleY == rand2SpeedY) or (randAppleX == rand3SpeedX and randAppleY == rand3SpeedY)or (randAppleX == rand4SpeedX and randAppleY == rand4SpeedY) or (randAppleX == randMultiX and randAppleY == randMultiY) or (randAppleX == rand1MultiX and randAppleY == rand1MultiY) or (randAppleX == rand2MultiX and randAppleY == rand2MultiY) or (randAppleX == rand3MultiX and randAppleY == rand3MultiY)or(randAppleX == rand4MultiX and randAppleY == rand4MultiY):
        randAppleX= round (random.randrange(0, display_width - block_size)/10.0)*10
        randAppleY= round (random.randrange(0, display_height - block_size)/10.0)*10

    if (randPortalX == randHalfX and randPortalY == randHalfY) or (randPortalX == rand1HalfX and randPortalY == rand1HalfY) or (randPortalX == rand2HalfX and randPortalY == rand2HalfY) or (randPortalX == rand3HalfX and randPortalY == rand3HalfY) or (randPortalX==rand4HalfX and randPortalY==rand4HalfY) or (randPortalX == randSpeedX and randPortalY == randSpeedY)or(randPortalX == rand1SpeedX and randPortalY == rand1SpeedY)or(randPortalX == rand2SpeedX and randPortalY == rand2SpeedY)or(randPortalX == rand3SpeedX and randPortalY == rand3SpeedY)or (randPortalX == rand4SpeedX and randPortalY == rand4SpeedY)or(randPortalX == randMultiX and randPortalY == randMultiY)or(randPortalX == rand1MultiX and randPortalY == rand1MultiY) or (randPortalX == rand2MultiX and randPortalY == rand2MultiY)or(randPortalX == rand3MultiX and randPortalY == rand3MultiY)or(randPortalX == rand4MultiX and randPortalY == rand4MultiY):
        randPortalX= round (random.randrange(0, display_width - block_size)/10.0)*10
        randPortalY= round (random.randrange(0, display_height - block_size)/10.0)*10

    if (randHalfX==rand1HalfX and randHalfY==rand1HalfY)or(randHalfX==rand2HalfX and randHalfY==rand2HalfY)or(randHalfX==rand3HalfX and randHalfY==rand3HalfY)or (randHalfX==rand4HalfX and randHalfY==rand4HalfY)or(randHalfX==randSpeedX and randHalfY==randSpeedY)or(randHalfX==rand1SpeedX and randHalfY==rand1SpeedY)or(randHalfX==rand2SpeedX and randHalfY==rand2SpeedY)or(randHalfX==rand3SpeedX and randHalfY==rand3SpeedY)or (randHalfX==rand4SpeedX and randHalfY==rand4SpeedY)or(randHalfX==randMultiX and randHalfY==randMultiY)or(randHalfX==rand1MultiX and randHalfY==rand1MultiY)or(randHalfX==rand2MultiX and randHalfY==rand2MultiY)or(randHalfX==rand3MultiX and randHalfY==rand3MultiY)or (randHalfX==rand4MultiX and randHalfY==rand4MultiY):
        randHalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
        randHalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

    if (rand1HalfX==rand2HalfX and rand1HalfY==rand2HalfY)or (rand1HalfX==rand3HalfX and rand1HalfY==rand3HalfY)or(rand1HalfX==rand4HalfX and rand1HalfY==rand4HalfY)or(rand1HalfX==randSpeedX and rand1HalfY==randSpeedY)or(rand1HalfX==rand1SpeedX and rand1HalfY==rand1SpeedY)or(rand1HalfX==rand2SpeedX and rand1HalfY==rand2SpeedY)or(rand1HalfX==rand3SpeedX and rand1HalfY==rand3SpeedY)or (rand1HalfX==rand4SpeedX and rand1HalfY==rand4SpeedY)or(rand1HalfX==randMultiX and rand1HalfY==randMultiY)or(rand1HalfX==rand1MultiX and rand1HalfY==rand1MultiY) or(rand1HalfX==rand2MultiX and rand1HalfY==rand2MultiY)or(rand1HalfX==rand3MultiX and rand1HalfY==rand3MultiY)or(rand1HalfX==rand4MultiX and rand1HalfY==rand4MultiY):
        rand1HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
        rand1HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

    if (rand2HalfX==rand3HalfX and rand2HalfY==rand3HalfY)or (rand2HalfX==rand4HalfX and rand2HalfY==rand4HalfY)or(rand2HalfX==randSpeedX and rand2HalfY==randSpeedY)or(rand2HalfX==rand1SpeedX and rand2HalfY==rand1SpeedY)or(rand2HalfX==rand2SpeedX and rand2HalfY==rand2SpeedY)or(rand2HalfX==rand3SpeedX and rand2HalfY==rand3SpeedY)or (rand2HalfX==rand4SpeedX and rand2HalfY==rand4SpeedY)or(rand2HalfX==randMultiX and rand2HalfY==randMultiY)or(rand2HalfX==rand1MultiX and rand2HalfY==rand1MultiY) or(rand2HalfX==rand2MultiX and rand2HalfY==rand2MultiY)or(rand2HalfX==rand3MultiX and rand2HalfY==rand3MultiY)or(rand2HalfX==rand4MultiX and rand2HalfY==rand4MultiY):
        rand2HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
        rand2HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10
    
    if(rand3HalfX==rand4HalfX and rand3HalfY==rand4HalfY)or(rand3HalfX==randSpeedX and rand3HalfY==randSpeedY)or(rand3HalfX==rand1SpeedX and rand3HalfY==rand1SpeedY)or(rand3HalfX==rand2SpeedX and rand3HalfY==rand2SpeedY)or(rand3HalfX==rand3SpeedX and rand3HalfY==rand3SpeedY)or (rand3HalfX==rand4SpeedX and rand3HalfY==rand4SpeedY)or(rand3HalfX==randMultiX and rand3HalfY==randMultiY)or(rand3HalfX==rand1MultiX and rand3HalfY==rand1MultiY) or(rand3HalfX==rand2MultiX and rand3HalfY==rand2MultiY)or(rand3HalfX==rand3MultiX and rand3HalfY==rand3MultiY)or(rand3HalfX==rand4MultiX and rand3HalfY==rand4MultiY):
        rand3HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
        rand3HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

    if(rand4HalfX==randSpeedX and rand4HalfY==randSpeedY)or(rand4HalfX==rand1SpeedX and rand4HalfY==rand1SpeedY)or(rand4HalfX==rand2SpeedX and rand4HalfY==rand2SpeedY)or(rand4HalfX==rand3SpeedX and rand4HalfY==rand3SpeedY)or (rand4HalfX==rand4SpeedX and rand4HalfY==rand4SpeedY)or(rand4HalfX==randMultiX and rand4HalfY==randMultiY)or(rand4HalfX==rand1MultiX and rand4HalfY==rand1MultiY) or(rand4HalfX==rand2MultiX and rand4HalfY==rand2MultiY)or(rand4HalfX==rand3MultiX and rand4HalfY==rand3MultiY)or(rand4HalfX==rand4MultiX and rand4HalfY==rand4MultiY):
        rand4HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
        rand4HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

    if (randSpeedX==rand1SpeedX and randSpeedY==rand1SpeedY)or(randSpeedX==rand2SpeedX and randSpeedY==rand2SpeedY)or(randSpeedX==rand3SpeedX and randSpeedY==rand3SpeedY)or (randSpeedX==rand4SpeedX and randSpeedY==rand4SpeedY)or(randSpeedX==randMultiX and randSpeedY==randMultiY)or(randSpeedX==rand1MultiX and randSpeedY==rand1MultiY) or(randSpeedX==rand2MultiX and randSpeedY==rand2MultiY)or(randSpeedX==rand3MultiX and randSpeedY==rand3MultiY)or(randSpeedX==rand4MultiX and randSpeedY==rand4MultiY):
        randSpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
        randSpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10

    if(rand1SpeedX==rand2SpeedX and rand1SpeedY==rand2SpeedY)or(rand1SpeedX==rand3SpeedX and rand1SpeedY==rand3SpeedY)or (rand1SpeedX==rand4SpeedX and rand1SpeedY==rand4SpeedY)or(rand1SpeedX==randMultiX and rand1SpeedY==randMultiY)or(rand1SpeedX==rand1MultiX and rand1SpeedY==rand1MultiY) or(rand1SpeedX==rand2MultiX and rand1SpeedY==rand2MultiY)or(rand1SpeedX==rand3MultiX and rand1SpeedY==rand3MultiY)or(rand1SpeedX==rand4MultiX and rand1SpeedY==rand4MultiY):
        rand1SpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
        rand1SpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10 

    if(rand2SpeedX==rand3SpeedX and rand2SpeedY==rand3SpeedY)or (rand2SpeedX==rand4SpeedX and rand2SpeedY==rand4SpeedY)or(rand2SpeedX==randMultiX and rand2SpeedY==randMultiY)or(rand2SpeedX==rand1MultiX and rand2SpeedY==rand1MultiY) or(rand2SpeedX==rand2MultiX and rand2SpeedY==rand2MultiY)or(rand2SpeedX==rand3MultiX and rand2SpeedY==rand3MultiY)or(rand2SpeedX==rand4MultiX and rand2SpeedY==rand4MultiY):
        rand2SpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
        rand2SpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10 

    if(rand3SpeedX==rand4SpeedX and rand3SpeedY==rand4SpeedY)or(rand3SpeedX==randMultiX and rand3SpeedY==randMultiY)or(rand3SpeedX==rand1MultiX and rand3SpeedY==rand1MultiY) or(rand3SpeedX==rand2MultiX and rand3SpeedY==rand2MultiY)or(rand3SpeedX==rand3MultiX and rand3SpeedY==rand3MultiY)or(rand3SpeedX==rand4MultiX and rand3SpeedY==rand4MultiY):
        rand3SpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
        rand3SpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10 

    if(rand4SpeedX==randMultiX and rand4SpeedY==randMultiY)or(rand4SpeedX==rand1MultiX and rand4SpeedY==rand1MultiY) or(rand4SpeedX==rand2MultiX and rand4SpeedY==rand2MultiY)or(rand4SpeedX==rand3MultiX and rand4SpeedY==rand3MultiY)or(rand4SpeedX==rand4MultiX and rand4SpeedY==rand4MultiY):
        rand4SpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
        rand4SpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10 

    if(randMultiX==rand1MultiX and randMultiY==rand1MultiY) or(randMultiX==rand2MultiX and randMultiY==rand2MultiY)or(randMultiX==rand3MultiX and randMultiY==rand3MultiY)or(randMultiX==rand4MultiX and randMultiY==rand4MultiY):
        randMultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
        randMultiY= round (random.randrange(0, display_height - block_size)/10.0)*10

    if(rand1MultiX==rand2MultiX and rand1MultiY==rand2MultiY)or(rand1MultiX==rand3MultiX and rand1MultiY==rand3MultiY)or(rand1MultiX==rand4MultiX and rand1MultiY==rand4MultiY):
        rand1MultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
        rand1MultiY= round (random.randrange(0, display_height - block_size)/10.0)*10

    if(rand2MultiX==rand3MultiX and rand2MultiY==rand3MultiY)or(rand2MultiX==rand4MultiX and rand2MultiY==rand4MultiY):
        rand2MultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
        rand2MultiY= round (random.randrange(0, display_height - block_size)/10.0)*10

    if rand3MultiX==rand4MultiX and rand3MultiY==rand4MultiY:
        rand4MultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
        rand4MultiY= round (random.randrange(0, display_height - block_size)/10.0)*10
    tmp=0
    desface=0
    cte=0
    while not gameExit:
        while  gameOver == True:
            gameDisplay.blit(perdiste,(0,0))
            message_to_screen("PERDISTE!", red,x_displace=0, y_displace=-200,size="large")
            message_to_screen("Presione ENTER si quiere jugar de nuevo o M para ir al menú", black,x_displace=0, y_displace=-50,size="small")
            display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:


                    if event.key == K_m:
                        game_intro()

                    if event.key == K_SPACE:
                        x = 250
                        gameExit = False
                        gameOver = False

                        lead_x = display_width/2
                        lead_y = display_height/2

                        lead_x_change = 0
                        lead_y_change = 0

                        snakeList= []
                        snakeLength = 1
                        
                        randAppleX= round (random.randrange(0, display_width - block_size)/10.0)*10
                        randAppleY= round (random.randrange(0, display_height - block_size)/10.0)*10
                        t1 = pygame.time.get_ticks()//1000

                        nivel=1
                        vida=3
                        contador_de_vida=4
                        multiplicador=350
                        tmp=0
                        desface=0
                        cte=0
                        FPS=20
        tiempo= pygame.time.get_ticks()//1000
        if (tmp==0):
            desface=tiempo
                
        for event in pygame.event.get():
            if event.type == QUIT:
                gameExit = True 
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    Serp_pos_x=200
                    escp = True
                    while escp == True:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                                quit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == K_RIGHT and Serp_pos_x < 390:
                                    Serp_pos_x=Serp_pos_x + 190
                                if event.key == K_LEFT and Serp_pos_x > 200:
                                    Serp_pos_x=Serp_pos_x - 190
                                if event.key == K_SPACE:
                                    if Serp_pos_x == 390:
                                        if nivel == 1:
                                            gameDisplay.blit(lvl1,(0,0))
                                            escp=False
                                        elif nivel == 2:
                                            gameDisplay.blit(lvl2,(0,0))
                                            escp=False
                                        desface=tiempo
                                        tmp=1
                                    if Serp_pos_x == 200:
                                        gameExit=True
                                        game_intro()
                        gameDisplay.blit(blackScreen,(0,0))
                        message_to_screen("¿Está seguro que desea regresar al menú?",white,x_displace=0,y_displace=-140,size="medium")
                        message_to_screen("Aceptar",white,x_displace=-100,y_displace=0,size="small")
                        message_to_screen("Cancelar",white,x_displace=100,y_displace=0,size="small")
                        message_to_screen ("Recuerde: su partida se reiniciará si vuelve al menú",red,x_displace=0,y_displace=200,size="small")
                        gameDisplay.blit(Serp,(Serp_pos_x,280))
                        display.update()
                if event.key == K_p:
                    tmp=1
                    pause(nivel)
                    desface=tiempo
                        
                if lead_x_change == 0:
                    if event.key == K_LEFT:
                        lead_x_change = -block_size
                        lead_y_change = 0
                    if event.key == K_RIGHT:
                        lead_x_change = block_size
                        lead_y_change = 0
                if lead_y_change == 0:
                    if event.key == K_UP:
                        lead_y_change = -block_size
                        lead_x_change = 0
                    elif event.key == K_DOWN:
                        lead_y_change = block_size
                        lead_x_change = 0

                if lead_x_change == 0:
                    if event.key == K_a:
                        lead_x_change = -block_size
                        lead_y_change = 0
                    elif event.key == K_d:
                        lead_x_change = block_size
                        lead_y_change = 0
                if lead_y_change == 0:
                    if event.key == K_w:
                        lead_y_change = -block_size
                        lead_x_change = 0
                    elif event.key == K_s:
                        lead_y_change = block_size
                        lead_x_change = 0
        
        if tmp == 0:
            cte=tiempo-desface+cte
        elif tmp==1:
            tiempo= pygame.time.get_ticks()//1000
            cte=tiempo-desface+cte
            tmp=2
        seg= x - tiempo + t1 + cte
        texto= str(seg)
        timeDisplayed= font.render(texto, 1, black)
        
        
        if lead_x>=display_width:
            lead_x=0
        if lead_x<0:
            lead_x=display_width
        if lead_y>=display_height:
            lead_y=0
        if lead_y<0:
            lead_y=display_height

        lead_x += lead_x_change
        lead_y += lead_y_change
        if nivel == 1:
            gameDisplay.blit(lvl1,(0,0))
        elif nivel == 2:
            gameDisplay.blit(lvl2,(0,0))
        gameDisplay.blit(timeDisplayed,(650,30))

        draw.rect(gameDisplay, red, [randAppleX, randAppleY,block_size,block_size])
       
        
        
        snakeHead= []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList [0]

        for eachSegment in snakeList [:-1]:
            if eachSegment == snakeHead:
                
                lead_x = display_width/2
                lead_y = display_height/2
                
                lead_x_change = 0
                lead_y_change = 0

                snakeList= []
                snakeLength = 1
                
                vida-=1
                contador_de_vida-=1
                puntaje-=puntaje
                        
                randAppleX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randAppleY= round (random.randrange(0, display_height - block_size)/10.0)*10
                t1 = pygame.time.get_ticks()//1000
                multiplicador=350
                FPS=20

                
                        
        snake(block_size, snakeList)

        
            
        if vida==0:
            gameOver=True
        
        if (seg==0):

            lead_x = display_width/2
            lead_y = display_height/2

            lead_x_change = 0
            lead_y_change = 0

            snakeList= []
            snakeLength = 1
                
            vida-=1
            contador_de_vida-=1
            puntaje-=puntaje
                        
            randAppleX= round (random.randrange(0, display_width - block_size)/10.0)*10
            randAppleY= round (random.randrange(0, display_height - block_size)/10.0)*10
            t1 = pygame.time.get_ticks()//1000
            multiplicador=350
            FPS=20
           

        

        if puntaje >= 2000:

            draw.rect(gameDisplay, blue, [randPortalX, randPortalY,block_size,block_size])

            if (puntaje == 4500 or puntaje == 6000) and vida<contador_de_vida:
                vida+=1
            if puntaje == 4600 or puntaje == 6100:
                contador_de_vida+=1
                
            if lead_x == randPortalX and lead_y == randPortalY:

                lead_x = display_width/2
                lead_y = display_height/2
    
                lead_x_change = 0
                lead_y_change = 0
    
                snakeList= []
                snakeLength = 1

                randAppleX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randAppleY= round (random.randrange(0, display_height - block_size)/10.0)*10

                t1 = pygame.time.get_ticks()//1000

                puntaje-=puntaje
                multiplicador=350
                FPS=20
                x=350
                nivel+=1
                if nivel == 3:
                    ganaste= True
                    while ganaste == True:
                        display.update()
                        gameDisplay.blit(win,(0,0))
                        message_to_screen("HAS GANADOO!", red,x_displace=0,y_displace=-250,size="large")
                        message_to_screen("Presiona Q para salir, M para ir al menu o C para volver a jugar", white,x_displace=0,y_displace=200,size="small")

                        for event in pygame.event.get():

                            if event.type == pygame.QUIT:
                                gameExit = True
                                gameOver = False

                            if event.type == pygame.KEYDOWN:

                                if event.key == K_q:
                                    pygame.quit()
                                    sys.exit()
                                    quit()
                                if event.key == K_m:
                                    game_intro()
                                
                                if event.key == K_c:
                                    x=250
                                    gameLoop()
                
                
                
        if nivel == 2:
            a=draw.rect(gameDisplay, black, [100, 100,600,20])
            b=draw.rect(gameDisplay, black, [50, 250,200,20])
            c=draw.rect(gameDisplay, black, [300, 250,200,20])
            d=draw.rect(gameDisplay, black, [550, 250,200,20])
            e=draw.rect(gameDisplay, black, [100, 400,200,20])
            f=draw.rect(gameDisplay, black, [500, 400,200,20])
            g=draw.rect(gameDisplay, black, [150, 550,500,20])

            if lead_x>=display_width:
                lead_x = display_width/2
                lead_y = display_height/2

                lead_x_change = 0
                lead_y_change = 0

                snakeList= []
                snakeLength = 1
                
                vida-=1
                contador_de_vida-=1
                puntaje-=puntaje
                        
                randAppleX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randAppleY= round (random.randrange(0, display_height - block_size)/10.0)*10
                t1 = pygame.time.get_ticks()//1000
                multiplicador=350
                FPS=20

            if lead_x<0:
                lead_x = display_width/2
                lead_y = display_height/2

                lead_x_change = 0
                lead_y_change = 0

                snakeList= []
                snakeLength = 1
                
                vida-=1
                contador_de_vida-=1
                puntaje-=puntaje
                        
                randAppleX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randAppleY= round (random.randrange(0, display_height - block_size)/10.0)*10
                t1 = pygame.time.get_ticks()//1000
                multiplicador=350
                FPS=20

            if lead_y>=display_height:

                lead_x = display_width/2
                lead_y = display_height/2

                lead_x_change = 0
                lead_y_change = 0

                snakeList= []
                snakeLength = 1
                
                vida-=1
                contador_de_vida-=1
                puntaje-=puntaje
                        
                randAppleX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randAppleY= round (random.randrange(0, display_height - block_size)/10.0)*10
                t1 = pygame.time.get_ticks()//1000
                multiplicador=350
                FPS=20

            if lead_y<0:
                lead_x = display_width/2
                lead_y = display_height/2

                lead_x_change = 0
                lead_y_change = 0

                snakeList= []
                snakeLength = 1
                
                vida-=1
                contador_de_vida-=1
                puntaje-=puntaje
                        
                randAppleX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randAppleY= round (random.randrange(0, display_height - block_size)/10.0)*10
                t1 = pygame.time.get_ticks()//1000
                multiplicador=350
                FPS=20

            if snakeLength>1:
                draw.rect(gameDisplay, green, [randHalfX, randHalfY,block_size,block_size])
                draw.rect(gameDisplay, green, [rand1HalfX, rand1HalfY,block_size,block_size])
                draw.rect(gameDisplay, green, [rand2HalfX, rand2HalfY,block_size,block_size])
                draw.rect(gameDisplay, green, [rand3HalfX, rand3HalfY,block_size,block_size])
                draw.rect(gameDisplay, green, [rand4HalfX, rand4HalfY,block_size,block_size])

                if lead_x == randHalfX and lead_y == randHalfY:
                    
                    randHalfX= round (random.randrange(0, display_width-block_size)/10.0)*10
                    randHalfY= round (random.randrange(0, display_height-block_size)/10.0)*10

                    if snakeLength % 2!=0:
                        snakeLength+=1
                        snakeLength //=2

                    elif snakeLength % 2==0:
                        snakeLength//=2

                    cortador=0

                    while cortador<=snakeLength:
                        snakeList.remove(snakeList[len(snakeList)-1])
                        cortador+=1


                    if puntaje % 200 != 0:
                        puntaje-=100
                        puntaje //=2
                    elif puntaje % 200 ==0:
                        puntaje //=2

                    draw.rect(gameDisplay, green, [randHalfX, randHalfY,block_size,block_size])

                if lead_x == rand1HalfX and lead_y == rand1HalfY:
                    
                    rand1HalfX= round (random.randrange(0, display_width-block_size)/10.0)*10
                    rand1HalfY= round (random.randrange(0, display_height-block_size)/10.0)*10

                    if snakeLength % 2!=0:
                        snakeLength+=1
                        snakeLength //=2

                    elif snakeLength % 2==0:
                        snakeLength//=2

                    cortador=0

                    while cortador<=snakeLength:
                        snakeList.remove(snakeList[len(snakeList)-1])
                        cortador+=1


                    if puntaje % 200 != 0:
                        puntaje-=100
                        puntaje //=2
                    elif puntaje % 200 ==0:
                        puntaje //=2

                    draw.rect(gameDisplay, green, [randHalfX, randHalfY,block_size,block_size])

                if lead_x == rand2HalfX and lead_y == rand2HalfY:
                    
                    rand2HalfX= round (random.randrange(0, display_width-block_size)/10.0)*10
                    rand2HalfY= round (random.randrange(0, display_height-block_size)/10.0)*10

                    if snakeLength % 2!=0:
                        snakeLength+=1
                        snakeLength //=2

                    elif snakeLength % 2==0:
                        snakeLength//=2

                    cortador=0

                    while cortador<=snakeLength:
                        snakeList.remove(snakeList[len(snakeList)-1])
                        cortador+=1


                    if puntaje % 200 != 0:
                        puntaje-=100
                        puntaje //=2
                    elif puntaje % 200 ==0:
                        puntaje //=2

                if lead_x == rand3HalfX and lead_y == rand3HalfY:
                    
                    rand3HalfX= round (random.randrange(0, display_width-block_size)/10.0)*10
                    rand3HalfY= round (random.randrange(0, display_height-block_size)/10.0)*10

                    if snakeLength % 2!=0:
                        snakeLength+=1
                        snakeLength //=2

                    elif snakeLength % 2==0:
                        snakeLength//=2

                    cortador=0

                    while cortador<=snakeLength:
                        snakeList.remove(snakeList[len(snakeList)-1])
                        cortador+=1


                    if puntaje % 200 != 0:
                        puntaje-=100
                        puntaje //=2
                    elif puntaje % 200 ==0:
                        puntaje //=2
                        
                if lead_x == rand4HalfX and lead_y == rand4HalfY:
                    
                    rand4HalfX= round (random.randrange(0, display_width-block_size)/10.0)*10
                    rand4HalfY= round (random.randrange(0, display_height-block_size)/10.0)*10

                    if snakeLength % 2!=0:
                        snakeLength+=1
                        snakeLength //=2

                    elif snakeLength % 2==0:
                        snakeLength//=2

                    cortador=0

                    while cortador<=snakeLength:
                        snakeList.remove(snakeList[len(snakeList)-1])
                        cortador+=1


                    if puntaje % 200 != 0:
                        puntaje-=100
                        puntaje //=2
                    elif puntaje % 200 ==0:
                        puntaje //=2
                        
            draw.rect(gameDisplay, pink, [randSpeedX, randSpeedY,block_size,block_size])
            draw.rect(gameDisplay, pink, [rand1SpeedX, rand1SpeedY,block_size,block_size])
            draw.rect(gameDisplay, pink, [rand2SpeedX, rand2SpeedY,block_size,block_size])
            draw.rect(gameDisplay, pink, [rand3SpeedX, rand3SpeedY,block_size,block_size])
            draw.rect(gameDisplay, pink, [rand4SpeedX, rand4SpeedY,block_size,block_size])

            if lead_x == randSpeedX and lead_y == randSpeedY:
                randSpeedX= round (random.randrange(0, display_width-block_size)/10.0)*10
                randSpeedY= round (random.randrange(0, display_height-block_size)/10.0)*10
                FPS=FPS*2

            if lead_x == rand1SpeedX and lead_y == rand1SpeedY:
                rand1SpeedX= round (random.randrange(0, display_width-block_size)/10.0)*10
                rand1SpeedY= round (random.randrange(0, display_height-block_size)/10.0)*10
                FPS=FPS*2

            if lead_x == rand2SpeedX and lead_y == rand2SpeedY:
                rand2SpeedX= round (random.randrange(0, display_width-block_size)/10.0)*10
                rand2SpeedY= round (random.randrange(0, display_height-block_size)/10.0)*10
                FPS=FPS*2

            if lead_x == rand3SpeedX and lead_y == rand3SpeedY:
                rand3SpeedX= round (random.randrange(0, display_width-block_size)/10.0)*10
                rand3SpeedY= round (random.randrange(0, display_height-block_size)/10.0)*10
                FPS=FPS*2

            if lead_x == rand4SpeedX and lead_y == rand4SpeedY:
                rand4SpeedX= round (random.randrange(0, display_width-block_size)/10.0)*10
                rand4SpeedY= round (random.randrange(0, display_height-block_size)/10.0)*10
                FPS=FPS*2


            draw.rect(gameDisplay, yellow, [randMultiX, randMultiY,block_size,block_size])
            draw.rect(gameDisplay, yellow, [rand1MultiX, rand1MultiY,block_size,block_size])
            draw.rect(gameDisplay, yellow, [rand2MultiX, rand2MultiY,block_size,block_size])
            draw.rect(gameDisplay, yellow, [rand3MultiX, rand3MultiY,block_size,block_size])
            draw.rect(gameDisplay, yellow, [rand4MultiX, rand4MultiY,block_size,block_size])
                    
            if lead_x == randMultiX and lead_y == randMultiY:
                randMultiX= round (random.randrange(0, display_width-block_size)/10.0)*10
                randMultiY= round (random.randrange(0, display_height-block_size)/10.0)*10
                multiplicador=seg-10

            if lead_x == rand1MultiX and lead_y == rand1MultiY:
                rand1MultiX= round (random.randrange(0, display_width-block_size)/10.0)*10
                rand1MultiY= round (random.randrange(0, display_height-block_size)/10.0)*10
                multiplicador=seg-10

            if lead_x == rand2MultiX and lead_y == rand2MultiY:
                rand2MultiX= round (random.randrange(0, display_width-block_size)/10.0)*10
                rand2MultiY= round (random.randrange(0, display_height-block_size)/10.0)*10
                multiplicador=seg-10

            if lead_x == rand3MultiX and lead_y == rand3MultiY:
                rand3MultiX= round (random.randrange(0, display_width-block_size)/10.0)*10
                rand3MultiY= round (random.randrange(0, display_height-block_size)/10.0)*10
                multiplicador=seg-10

            if lead_x == rand4MultiX and lead_y == rand4MultiY:
                rand4MultiX= round (random.randrange(0, display_width-block_size)/10.0)*10
                rand4MultiY= round (random.randrange(0, display_height-block_size)/10.0)*10
                multiplicador=seg-10

            if multiplicador < seg :
                aviso_multi="Puntaje x2"
                puntajeDisplayed=font.render(aviso_multi, 1, black)
                gameDisplay.blit(puntajeDisplayed,(350,400))
                if lead_x == randAppleX and lead_y == randAppleY:
                    puntaje+=100
                    snakeLength+=1

            if (randAppleX >= 100 and randAppleX <= 690) and (randAppleY >= 100 and randAppleY <=110):

                randAppleX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randAppleY= round (random.randrange(0, display_height - block_size)/10.0)*10
                
            if (randPortalX >= 100 and randPortalX <= 690) and (randPortalY >= 100 and randPortalY <=110):

                randPortalX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randPortalY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (randHalfX >= 100 and randHalfX <= 690) and (randHalfY >= 100 and randHalfY <=110):

                randHalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randHalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand1HalfX >= 100 and rand1HalfX <= 690) and (rand1HalfY >= 100 and rand1HalfY <=110):

                rand1HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand1HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand2HalfX >= 100 and rand2HalfX <= 690) and (rand2HalfY >= 100 and rand2HalfY <=110):

                rand2HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand2HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand3HalfX >= 100 and rand3HalfX <= 690) and (rand3HalfY >= 100 and rand3HalfY <=110):

                rand3HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand3HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand4HalfX >= 100 and rand4HalfX <= 690) and (rand4HalfY >= 100 and rand4HalfY <=110):

                rand4HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand4HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (randSpeedX >= 100 and randSpeedX <= 690) and (randSpeedY >= 100 and randSpeedY <=110):

                randSpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randSpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand1SpeedX >= 100 and rand1SpeedX <= 690) and (rand1SpeedY >= 100 and rand1SpeedY <=110):

                rand1SpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand1SpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand2SpeedX >= 100 and rand2SpeedX <= 690) and (rand2SpeedY >= 100 and rand2SpeedY <=110):

                rand2SpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand2SpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand3SpeedX >= 100 and rand3SpeedX <= 690) and (rand3SpeedY >= 100 and rand3SpeedY <=110):

                rand3SpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand3SpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand4SpeedX >= 100 and rand4SpeedX <= 690) and (rand4SpeedY >= 100 and rand4SpeedY <=110):

                rand4SpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand4SpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (randMultiX >= 100 and randMultiX <= 690) and (randMultiY >= 100 and randMultiY <=110):

                randMultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randMultiY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand1MultiX >= 100 and rand1MultiX <= 690) and (rand1MultiY >= 100 and rand1MultiY <=110):

                rand1MultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand1MultiY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand2MultiX >= 100 and rand2MultiX <= 690) and (rand2MultiY >= 100 and rand2MultiY <=110):

                rand2MultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand2MultiY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand3MultiX >= 100 and rand3MultiX <= 690) and (rand3MultiY >= 100 and rand3MultiY <=110):

                rand3MultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand3MultiY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand4MultiX >= 100 and rand4MultiX <= 690) and (rand4MultiY >= 100 and rand4MultiY <=110):

                rand4MultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand4MultiY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (lead_x >= 100 and lead_x <= 690) and (lead_y >=100 and lead_y<=110):

                lead_x = display_width/2
                lead_y = display_height/2

                lead_x_change = 0
                lead_y_change = 0

                snakeList= []
                snakeLength = 1
                
                vida-=1
                contador_de_vida-=1
                puntaje-=puntaje
                        
                randAppleX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randAppleY= round (random.randrange(0, display_height - block_size)/10.0)*10
                t1 = pygame.time.get_ticks()//1000
                multiplicador=350
                FPS=20

            if (randAppleX >= 50 and randAppleX <= 240) and (randAppleY >= 250 and randAppleY <=260):

                randAppleX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randAppleY= round (random.randrange(0, display_height - block_size)/10.0)*10
                
            if (randPortalX >= 50 and randPortalX <= 240) and (randPortalY >= 250 and randPortalY <=260):

                randPortalX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randPortalY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (randHalfX >= 50 and randHalfX <= 240) and (randHalfY >= 250 and randHalfY <=260):

                randHalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randHalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand1HalfX >= 50 and rand1HalfX <= 240) and (rand1HalfY >= 250 and rand1HalfY <=260):

                rand1HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand1HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand2HalfX >= 50 and rand2HalfX <= 240) and (rand2HalfY >= 250 and rand2HalfY <=260):

                rand2HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand2HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand3HalfX >= 50 and rand3HalfX <= 240) and (rand3HalfY >= 250 and rand3HalfY <=260):

                rand3HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand3HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand4HalfX >= 50 and rand4HalfX <= 240) and (rand4HalfY >= 250 and rand4HalfY <=260):

                rand4HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand4HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (randSpeedX >= 50 and randSpeedX <= 240) and (randSpeedY >= 250 and randSpeedY <=260):

                randSpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randSpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand1SpeedX >= 50 and rand1SpeedX <= 240) and (rand1SpeedY >= 250 and rand1SpeedY <=260):

                rand1SpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand1SpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand2SpeedX >= 50 and rand2SpeedX <= 240) and (rand2SpeedY >= 250 and rand2SpeedY <=260):

                rand2SpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand2SpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10
                
            if (rand3SpeedX >= 50 and rand3SpeedX <= 240) and (rand3SpeedY >= 250 and rand3SpeedY <=260):

                rand3SpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand3SpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand4SpeedX >= 50 and rand4SpeedX <= 240) and (rand4SpeedY >= 250 and rand4SpeedY <=260):

                rand4SpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand4SpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (randMultiX >= 50 and randMultiX <= 240) and (randMultiY >= 250 and randMultiY <=260):

                randMultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randMultiY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand1MultiX >= 50 and rand1MultiX <= 240) and (rand1MultiY >= 250 and rand1MultiY <=260):

                rand1MultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand1MultiY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand2MultiX >= 50 and rand2MultiX <= 240) and (rand2MultiY >= 250 and rand2MultiY <=260):

                rand2MultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand2MultiY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand3MultiX >= 50 and rand3MultiX <= 240) and (rand3MultiY >= 250 and rand3MultiY <=260):

                rand3MultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand3MultiY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand4MultiX >= 50 and rand4MultiX <= 240) and (rand4MultiY >= 250 and rand4MultiY <=260):

                rand4MultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand4MultiY= round (random.randrange(0, display_height - block_size)/10.0)*10



            if (lead_x >= 50 and lead_x <= 240) and (lead_y >=250 and lead_y<=260):

                lead_x = display_width/2
                lead_y = display_height/2

                lead_x_change = 0
                lead_y_change = 0

                snakeList= []
                snakeLength = 1
            
                vida-=1
                contador_de_vida-=1
                puntaje-=puntaje
                        
                randAppleX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randAppleY= round (random.randrange(0, display_height - block_size)/10.0)*10
                t1 = pygame.time.get_ticks()//1000
                multiplicador=350
                FPS=20

            
            if (randAppleX >= 300 and randAppleX <= 490) and (randAppleY >= 250 and randAppleY <=260):

                randAppleX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randAppleY= round (random.randrange(0, display_height - block_size)/10.0)*10
                
            if (randPortalX >= 300 and randPortalX <= 490) and (randPortalY >= 250 and randPortalY <=260):

                randPortalX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randPortalY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (randHalfX >= 300 and randHalfX <= 490) and (randHalfY >= 250 and randHalfY <=260):

                randHalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randHalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand1HalfX >= 300 and rand1HalfX <= 490) and (rand1HalfY >= 250 and rand1HalfY <=260):

                rand1HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand1HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand2HalfX >= 300 and rand2HalfX <= 490) and (rand2HalfY >= 250 and rand2HalfY <=260):

                rand2HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand2HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand3HalfX >= 300 and rand3HalfX <= 490) and (rand3HalfY >= 250 and rand3HalfY <=260):

                rand3HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand3HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand4HalfX >= 300 and rand4HalfX <= 490) and (rand4HalfY >= 250 and rand4HalfY <=260):

                rand4HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand4HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (randSpeedX >= 300 and randSpeedX <= 490) and (randSpeedY >= 250 and randSpeedY <=260):

                randSpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randSpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand1SpeedX >= 300 and rand1SpeedX <= 490) and (rand1SpeedY >= 250 and rand1SpeedY <=260):

                rand1SpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand1SpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand2SpeedX >= 300 and rand2SpeedX <= 490) and (rand2SpeedY >= 250 and rand2SpeedY <=260):

                rand2SpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand2SpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand3SpeedX >= 300 and rand3SpeedX <= 490) and (rand3SpeedY >= 250 and rand3SpeedY <=260):

                rand3SpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand3SpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand4SpeedX >= 300 and rand4SpeedX <= 490) and (rand4SpeedY >= 250 and rand4SpeedY <=260):

                rand4SpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand4SpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (randMultiX >= 300 and randMultiX <= 490) and (randMultiY >= 250 and randMultiY <=260):

                randMultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randMultiY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand1MultiX >= 300 and rand1MultiX <= 490) and (rand1MultiY >= 250 and rand1MultiY <=260):

                randMultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randMultiY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand2MultiX >= 300 and rand2MultiX <= 490) and (rand2MultiY >= 250 and rand2MultiY <=260):

                randMultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randMultiY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand3MultiX >= 300 and rand3MultiX <= 490) and (rand3MultiY >= 250 and rand3MultiY <=260):

                rand3MultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand3MultiY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand4MultiX >= 300 and rand4MultiX <= 490) and (rand4MultiY >= 250 and rand4MultiY <=260):

                rand4MultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand4MultiY= round (random.randrange(0, display_height - block_size)/10.0)*10


            if (lead_x >= 300 and lead_x <= 490) and (lead_y >=250 and lead_y<=260):

                lead_x = display_width/2
                lead_y = display_height/2

                lead_x_change = 0
                lead_y_change = 0

                snakeList= []
                snakeLength = 1
                
                vida-=1
                contador_de_vida-=1
                puntaje-=puntaje

                randAppleX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randAppleY= round (random.randrange(0, display_height - block_size)/10.0)*10
                t1 = pygame.time.get_ticks()//1000
                multiplicador=350
                FPS=20


            if (randAppleX >= 550 and randAppleX <= 740) and (randAppleY >= 250 and randAppleY <=260):

                randAppleX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randAppleY= round (random.randrange(0, display_height - block_size)/10.0)*10
                
            if (randPortalX >= 550 and randPortalX <= 740) and (randPortalY >= 250 and randPortalY <=260):

                randPortalX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randPortalY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (randHalfX >= 550 and randHalfX <= 740) and (randHalfY >= 250 and randHalfY <=260):

                randHalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randHalfY= round (random.randrange(0, display_height - block_size)/10.0)*107

            if (rand1HalfX >= 550 and rand1HalfX <= 740) and (rand1HalfY >= 250 and rand1HalfY <=260):

                rand1HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand1HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand2HalfX >= 550 and rand2HalfX <= 740) and (rand2HalfY >= 250 and rand2HalfY <=260):

                rand2HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand2HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand3HalfX >= 550 and rand3HalfX <= 740) and (rand3HalfY >= 250 and rand3HalfY <=260):

                rand3HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand3HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand4HalfX >= 550 and rand4HalfX <= 740) and (rand4HalfY >= 250 and rand4HalfY <=260):

                rand4HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand4HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

            
            if (randSpeedX >= 550 and randSpeedX <= 740) and (randSpeedY >= 250 and randSpeedY <=260):

                randSpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randSpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand1SpeedX >= 550 and rand1SpeedX <= 740) and (rand1SpeedY >= 250 and rand1SpeedY <=260):

                rand1SpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand1SpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand2SpeedX >= 550 and rand2SpeedX <= 740) and (rand2SpeedY >= 250 and rand2SpeedY <=260):

                rand2SpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand2SpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand3SpeedX >= 550 and rand3SpeedX <= 740) and (rand3SpeedY >= 250 and rand3SpeedY <=260):

                rand3SpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand3SpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand4SpeedX >= 550 and rand4SpeedX <= 740) and (rand4SpeedY >= 250 and rand4SpeedY <=260):

                rand4SpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand4SpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (randMultiX >= 550 and randMultiX <= 740) and (randMultiY >= 250 and randMultiY <=260):

                randMultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randMultiY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand1MultiX >= 550 and rand1MultiX <= 740) and (rand1MultiY >= 250 and rand1MultiY <=260):

                rand1MultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand1MultiY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand2MultiX >= 550 and rand2MultiX <= 740) and (rand2MultiY >= 250 and rand2MultiY <=260):

                rand2MultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand2MultiY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand3MultiX >= 550 and rand3MultiX <= 740) and (rand3MultiY >= 250 and rand3MultiY <=260):

                rand3MultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand3MultiY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand4MultiX >= 550 and rand4MultiX <= 740) and (rand4MultiY >= 250 and rand4MultiY <=260):

                rand4MultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand4MultiY= round (random.randrange(0, display_height - block_size)/10.0)*10

                
            if (lead_x >= 550 and lead_x <= 740) and (lead_y >=250 and lead_y<=260):

                lead_x = display_width/2
                lead_y = display_height/2

                lead_x_change = 0
                lead_y_change = 0

                snakeList= []
                snakeLength = 1
                
                vida-=1
                contador_de_vida-=1
                puntaje-=puntaje
                        
                randAppleX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randAppleY= round (random.randrange(0, display_height - block_size)/10.0)*10
                t1 = pygame.time.get_ticks()//1000
                multiplicador=350
                FPS=20


            if (randAppleX >= 100 and randAppleX <= 290) and (randAppleY >= 400 and randAppleY <=410):

                randAppleX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randAppleY= round (random.randrange(0, display_height - block_size)/10.0)*10
                
            if (randPortalX >= 100 and randPortalX <= 290) and (randPortalY >= 400 and randPortalY <=410):

                randPortalX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randPortalY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (randHalfX >= 100 and randHalfX <= 290) and (randHalfY >= 400 and randHalfY <=410):

                randHalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randHalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand1HalfX >= 100 and rand1HalfX <= 290) and (rand1HalfY >= 400 and rand1HalfY <=410):

                rand1HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand1HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand2HalfX >= 100 and rand2HalfX <= 290) and (rand2HalfY >= 400 and rand2HalfY <=410):

                rand2HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand2HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand3HalfX >= 100 and rand3HalfX <= 290) and (rand3HalfY >= 400 and rand3HalfY <=410):

                rand3HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand3HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10


            if (rand4HalfX >= 100 and rand4HalfX <= 290) and (rand4HalfY >= 400 and rand4HalfY <=410):

                rand4HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand4HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10
                

            if (randSpeedX >= 100 and randSpeedX <= 290) and (randSpeedY >= 400 and randSpeedY <=410):

                randSpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randSpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand1SpeedX >= 100 and rand1SpeedX <= 290) and (rand1SpeedY >= 400 and rand1SpeedY <=410):

                rand1SpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand1SpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand2SpeedX >= 100 and rand2SpeedX <= 290) and (rand2SpeedY >= 400 and rand2SpeedY <=410):

                rand2SpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand2SpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand3SpeedX >= 100 and rand3SpeedX <= 290) and (rand3SpeedY >= 400 and rand3SpeedY <=410):

                rand3SpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand3SpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand4SpeedX >= 100 and rand4SpeedX <= 290) and (rand4SpeedY >= 400 and rand4SpeedY <=410):

                rand4SpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand4SpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (randMultiX >= 100 and randMultiX <= 290) and (randMultiY >= 400 and randMultiY <=410):

                randMultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randMultiY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand1MultiX >= 100 and rand1MultiX <= 290) and (rand1MultiY >= 400 and rand1MultiY <=410):

                rand1MultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand1MultiY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand2MultiX >= 100 and rand2MultiX <= 290) and (rand2MultiY >= 400 and rand2MultiY <=410):

                rand2MultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand2MultiY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand3MultiX >= 100 and rand3MultiX <= 290) and (rand3MultiY >= 400 and rand3MultiY <=410):

                rand3MultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand3MultiY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand4MultiX >= 100 and rand4MultiX <= 290) and (rand4MultiY >= 400 and rand4MultiY <=410):

                rand4MultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand4MultiY= round (random.randrange(0, display_height - block_size)/10.0)*10


            if (lead_x >= 100 and lead_x <= 290) and (lead_y >=400 and lead_y<=410):

                lead_x = display_width/2
                lead_y = display_height/2

                lead_x_change = 0
                lead_y_change = 0

                snakeList= []
                snakeLength = 1

                vida-=1
                contador_de_vida-=1
                puntaje-=puntaje
                        
                randAppleX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randAppleY= round (random.randrange(0, display_height - block_size)/10.0)*10
                t1 = pygame.time.get_ticks()//1000    
                multiplicador=350
                FPS=20


            if (randAppleX >= 500 and randAppleX <= 690) and (randAppleY >= 400 and randAppleY <=410):

                randAppleX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randAppleY= round (random.randrange(0, display_height - block_size)/10.0)*10
                
            if (randPortalX >= 500 and randPortalX <= 690) and (randPortalY >= 400 and randPortalY <=410):

                randPortalX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randPortalY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (randHalfX >= 500 and randHalfX <= 690) and (randHalfY >= 400 and randHalfY <=410):

                randHalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randHalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand1HalfX >= 500 and rand1HalfX <= 690) and (rand1HalfY >= 400 and rand1HalfY <=410):

                rand1HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand1HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand2HalfX >= 500 and rand2HalfX <= 690) and (rand2HalfY >= 400 and rand2HalfY <=410):

                rand2HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand2HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand3HalfX >= 500 and rand3HalfX <= 690) and (rand3HalfY >= 400 and rand3HalfY <=410):

                rand3HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand3HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand4HalfX >= 500 and rand4HalfX <= 690) and (rand4HalfY >= 400 and rand4HalfY <=410):

                rand4HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand4HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (randSpeedX >= 500 and randSpeedX <= 690) and (randSpeedY >= 400 and randSpeedY <=410):

                randSpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randSpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand1SpeedX >= 500 and rand1SpeedX <= 690) and (rand1SpeedY >= 400 and rand1SpeedY <=410):

                rand1SpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand1SpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand2SpeedX >= 500 and rand2SpeedX <= 690) and (rand2SpeedY >= 400 and rand2SpeedY <=410):

                rand2SpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand2SpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand3SpeedX >= 500 and rand3SpeedX <= 690) and (rand3SpeedY >= 400 and rand3SpeedY <=410):

                rand3SpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand3SpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand4SpeedX >= 500 and rand4SpeedX <= 690) and (rand4SpeedY >= 400 and rand4SpeedY <=410):

                rand4SpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand4SpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (randMultiX >= 500 and randMultiX <= 690) and (randMultiY >= 400 and randMultiY <=410):

                randMultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randMultiY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand1MultiX >= 500 and rand1MultiX <= 690) and (rand1MultiY >= 400 and rand1MultiY <=410):

                rand1MultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand1MultiY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand2MultiX >= 500 and rand2MultiX <= 690) and (rand2MultiY >= 400 and rand2MultiY <=410):

                rand2MultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand2MultiY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand3MultiX >= 500 and rand3MultiX <= 690) and (rand3MultiY >= 400 and rand3MultiY <=410):

                rand3MultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand3MultiY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand4MultiX >= 500 and rand4MultiX <= 690) and (rand4MultiY >= 400 and rand4MultiY <=410):

                rand4MultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand4MultiY= round (random.randrange(0, display_height - block_size)/10.0)*10


            if (lead_x >= 500 and lead_x <= 690) and (lead_y >=400 and lead_y<=410):

                lead_x = display_width/2
                lead_y = display_height/2

                lead_x_change = 0
                lead_y_change = 0

                snakeList= []
                snakeLength = 1

                vida-=1
                contador_de_vida-=1
                puntaje-=puntaje
                        
                randAppleX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randAppleY= round (random.randrange(0, display_height - block_size)/10.0)*10
                t1 = pygame.time.get_ticks()//1000
                multiplicador=350
                FPS=20         

            if (randAppleX >= 150 and randAppleX <= 640) and (randAppleY >= 550 and randAppleY <=570):

                randAppleX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randAppleY= round (random.randrange(0, display_height - block_size)/10.0)*10
                
            if (randPortalX >= 150 and randPortalX <= 640) and (randPortalY >= 550 and randPortalY <=570):

                randPortalX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randPortalY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand1HalfX >= 150 and rand1HalfX <= 640) and (rand1HalfY >= 550 and rand1HalfY <=570):

                rand1HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand1HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand2HalfX >= 150 and rand2HalfX <= 640) and (rand2HalfY >= 550 and rand2HalfY <=570):

                rand2HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand2HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand3HalfX >= 150 and rand3HalfX <= 640) and (rand3HalfY >= 550 and rand3HalfY <=570):

                rand3HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand3HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand4HalfX >= 150 and rand4HalfX <= 640) and (rand4HalfY >= 550 and rand4HalfY <=570):

                rand4HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand4HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (randHalfX >= 150 and randHalfX <= 640) and (randHalfY >= 550 and randHalfY <=570):

                randHalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randHalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand1HalfX >= 150 and rand1HalfX <= 640) and (rand1HalfY >= 550 and rand1HalfY <=570):

                rand1HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand1HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand2HalfX >= 150 and rand2HalfX <= 640) and (rand2HalfY >= 550 and rand2HalfY <=570):

                rand2HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand2HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand3HalfX >= 150 and rand3HalfX <= 640) and (rand3HalfY >= 550 and rand3HalfY <=570):

                rand3HalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand3HalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand4HalfX >= 150 and rand4HalfX <= 640) and (rand4HalfY >= 550 and rand4HalfY <=570):

                randHalfX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randHalfY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (randSpeedX >= 150 and randSpeedX <= 640) and (randSpeedY >= 550 and randSpeedY <=570):

                randSpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randSpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10

            
            if (rand1SpeedX >= 150 and rand1SpeedX <= 640) and (rand1SpeedY >= 550 and rand1SpeedY <=570):

                rand1SpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand1SpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10

            
            if (rand2SpeedX >= 150 and rand2SpeedX <= 640) and (rand2SpeedY >= 550 and rand2SpeedY <=570):

                rand2SpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand2SpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10

            
            if (rand3SpeedX >= 150 and rand3SpeedX <= 640) and (rand3SpeedY >= 550 and rand3SpeedY <=570):

                rand3SpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand3SpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10

            
            if (rand4SpeedX >= 150 and rand4SpeedX <= 640) and (rand4SpeedY >= 550 and rand4SpeedY <=570):

                rand4SpeedX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand4SpeedY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (randMultiX >= 150 and randMultiX <= 640) and (randMultiY >= 550 and randMultiY <=570):

                randMultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randMultiY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand1MultiX >= 150 and rand1MultiX <= 640) and (rand1MultiY >= 550 and rand1MultiY <=570):

                rand1MultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand1MultiY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand2MultiX >= 150 and rand2MultiX <= 640) and (rand2MultiY >= 550 and rand2MultiY <=570):

                rand2MultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand2MultiY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand3MultiX >= 150 and rand3MultiX <= 640) and (rand3MultiY >= 550 and rand3MultiY <=570):

                rand3MultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand3MultiY= round (random.randrange(0, display_height - block_size)/10.0)*10

            if (rand4MultiX >= 150 and rand4MultiX <= 640) and (rand4MultiY >= 550 and rand4MultiY <=570):

                rand4MultiX= round (random.randrange(0, display_width - block_size)/10.0)*10
                rand4MultiY= round (random.randrange(0, display_height - block_size)/10.0)*10


            if (lead_x >= 150 and lead_x <= 640) and (lead_y >=550 and lead_y<570):
                
                lead_x = display_width/2
                lead_y = display_height/2

                lead_x_change = 0
                lead_y_change = 0

                snakeList= []
                snakeLength = 1
                
                vida-=1
                contador_de_vida-=1
                puntaje-=puntaje
                        
                randAppleX= round (random.randrange(0, display_width - block_size)/10.0)*10
                randAppleY= round (random.randrange(0, display_height - block_size)/10.0)*10
                t1 = pygame.time.get_ticks()//1000
                multiplicador=350
                FPS=20


        texto2= str(vida)
        texto3= str(nivel)
        palabra3= "Nivel:"
        palabra2 = "Vidas:"
        time= "Tiempo: "
        texto1= str(puntaje)
        palabra = "Puntaje: "
        nivelDisplayed=font.render(palabra3, 1, black)
        nivel2Displayed=font.render(texto3, 1, black)
        lifeDisplayed= font.render(texto2, 1, black)
        life1Displayed= font.render(palabra2, 1, black)
        time1Displayed= font.render(time, 1, black)
        scoreDisplayed= font.render(texto1, 1, black)
        score1Displayed= font.render(palabra, 1, black)
        gameDisplay.blit(nivelDisplayed,(50,30))
        gameDisplay.blit(nivel2Displayed,(100,30))
        gameDisplay.blit(lifeDisplayed,(410,30))
        gameDisplay.blit(life1Displayed,(350,30))
        gameDisplay.blit(time1Displayed,(575,30))
        gameDisplay.blit(scoreDisplayed,(275,30))
        gameDisplay.blit(score1Displayed,(175,30))


        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX= round (random.randrange(0, display_width-block_size)/10.0)*10
            randAppleY= round (random.randrange(0, display_height-block_size)/10.0)*10
            snakeLength += 1
            puntaje+=100
            
        
        
            
            
        display.update()
                    
        clock.tick(FPS)

    pygame.quit()
    sys.exit()
    quit()
game_intro()

