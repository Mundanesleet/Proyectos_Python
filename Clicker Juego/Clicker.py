#Proyecto Clicker - Alejandro Sossa - 15/04/2023
import pgzrun
from pgzero.builtins import Actor, animate, mouse
import pgzero.screen
screen : pgzero.screen.Screen

WIDTH = 600
HEIGHT = 400

TITLE = 'Clicker Animal'
FPS = 30

#Objetos 
jirafa = Actor('jirafa', (150,250))
fondo = Actor('fondo')
bonus_1 = Actor('bono', (450, 100))
bonus_2 = Actor('bono', (450, 200))
bonus_3 = Actor('bono', (450, 300))
play = Actor('jugar', (300, 100))
cross = Actor('cerrar', (580, 20))
tienda = Actor('tienda',(300, 200))
coleccion = Actor('coleccion', (300, 300))
cocodrilo = Actor('cocodrilo', (120, 200))
hipopotamo = Actor('hipopotamo', (300, 200))
morsa = Actor('morsa', (480, 200))

#Variables
count = 0
click = 1
mode = 'menu'
price_1 = 15
price_2 = 200
price_3 = 600
animals = []

#Mostrando en pantalla
def draw():
    #En el menu
    if mode == 'menu':
        fondo.draw()
        play.draw()
        screen.draw.text(count, center = (30, 20), color = 'white')
        tienda.draw()
        coleccion.draw()
    
    #En juego    
    elif mode == 'game':
        fondo.draw()
        jirafa.draw()
        screen.draw.text(count, center=(150, 100), color="white", fontsize = 96)
        bonus_1.draw()
        screen.draw.text("+1$ cada 2s", center=(450, 80), color="black", fontsize = 20)
        screen.draw.text(price_1, center=(450, 110), color="black", fontsize = 20)
        bonus_2.draw()
        screen.draw.text("+15$ cada 2s", center=(450, 180), color="black", fontsize = 20)
        screen.draw.text(price_2, center=(450, 210), color="black", fontsize = 20)
        bonus_3.draw()
        screen.draw.text("+50$ cada 2s", center=(450, 280), color="black", fontsize = 20)
        screen.draw.text(price_3, center=(450, 310), color="black", fontsize = 20)
        cross.draw()
    #En la tienda
    elif mode == 'shop':
        fondo.draw()
        cocodrilo.draw()
        screen.draw.text("500$", center= (120, 300), color="white", fontsize = 36)
        hipopotamo.draw()
        screen.draw.text("2500$", center= (300, 300), color="white", fontsize = 36)
        morsa.draw()
        screen.draw.text("7000$", center= (480, 300), color="white", fontsize = 36)
        cross.draw()
        screen.draw.text(count, center=(30, 20), color="white", fontsize = 36)
    
    #Coleccion
    elif mode == 'coleccion':
        fondo.draw()
        for i in range(len(animals)):
            animals[i].draw()
        cross.draw()
        screen.draw.text(count, center=(30, 20), color="white", fontsize = 36)
        screen.draw.text("+2$", center= (120, 300), color="white", fontsize = 36)
        screen.draw.text("+3$", center= (300, 300), color="white", fontsize = 36)
        screen.draw.text("+4$", center= (480, 300), color="white", fontsize = 36)

#Creando los bonos
def for_bonus_1():
    global count
    count += 1

def for_bonus_2():
    global count
    count += 5

def for_bonus_3():
    global count
    count += 15

#Funciones del click 
def on_mouse_down(button, pos):
    global count
    global mode 
    global price_1, price_2, price_3
    global click
    if button == mouse.LEFT and mode == 'game':
        #Click en el objeto animal
        if jirafa.collidepoint(pos):
            count += click
            jirafa.y = 200
            animate(jirafa, tween='bounce_end', duration=0.5, y=250)
        #Click en el boton 1
        elif bonus_1.collidepoint(pos):
            bonus_1.y = 105
            animate(bonus_1, tween='bounce_end', duration=0.5, y=100)
            if count >= price_1:
                schedule_interval(for_bonus_1, 2)
                count -= price_1
                price_1 *= 2
        # Click en el botón bonus_2 
        elif bonus_2.collidepoint(pos):
            bonus_2.y = 205
            animate(bonus_2, tween='bounce_end', duration=0.5, y=200)
            if count >= price_2:
                schedule_interval(for_bonus_2, 2)
                count -= price_2
                price_2 *= 2
        # Click en el botón bonus_3
        elif bonus_3.collidepoint(pos):
            bonus_3.y = 305
            animate(bonus_3, tween='bounce_end', duration=0.5, y=300)
            if count >= price_3:
                schedule_interval(for_bonus_3, 2)
                count -= price_3
                price_3 *= 2

        
        
pgzrun.go()


