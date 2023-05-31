#Proyecto piedra papel o tijera - Alejandro Sossa - 14/04/2023
import time 
import random 

puntajepc1 = 0
puntajepc2 = 0

for i in range(30):
    pc1 = random.randint(1, 3)
    pc2 = random.randint(1, 3)
    
    #Organizando las opciones de pc1
    if pc1 == 1:
        pc1 = 'piedra'
    elif pc1 == 2:
        pc1 = 'tijera'
    else:
        pc1 = 'papel'
    
    #Organizando las opciones de pc2
    if pc2 == 1:
        pc2 = 'piedra'
    elif pc2 == 2:
        pc2 = 'tijera'
    else:
        pc2 = 'papel'

    #Creando las comparaciones
    if pc1 == pc2:
        print('Pc1 escogio: ', pc1)
        print('Pc2 escogio: ', pc2)
        print('Empate')
        time.sleep(2)
    elif pc1 == 'piedra' and pc2 == 'tijera':
        print('Pc1 escogio: ', pc1)
        print('Pc2 escogio: ', pc2)
        print('Gana pc1')
        puntajepc1 += 1
        time.sleep(2)
    elif pc1 == 'papel' and pc2 == 'piedra':
        print('Pc1 escogio: ', pc1)
        print('Pc2 escogio: ', pc2)
        print('Gana pc1')
        puntajepc1 += 1
        time.sleep(2)
    elif pc1 == 'tijera' and pc2 == 'papel':
        print('Pc1 escogio: ', pc1)
        print('Pc2 escogio: ', pc2)
        print('Gana pc1')
        puntajepc1 += 1
        time.sleep(2)
    else:
        print('Pc1 escogio: ', pc1)
        print('Pc2 escogio: ', pc2)
        print('Gana pc2')
        puntajepc2 += 1
        time.sleep(2)
    print('Puntaje Pc1: ', puntajepc1)
    print('Puntaje Pc2: ', puntajepc2)
    time.sleep(2)
    print('Nuevo Juego')