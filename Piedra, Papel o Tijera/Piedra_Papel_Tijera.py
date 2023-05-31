#Piedra Papel o Tijera - Alejandro Sossa - 14/04/2023
import time 
import random

#Variables Iniciales
mipuntaje = 0
puntajepc = 0
#Bucle del juego y comprobacion de las opciones
for i in range(30):
    jugador = str(input('Piedra, Papel o Tijera?: ')).lower()
    if jugador == 'piedra' or jugador == 'tijera' or jugador == 'papel':
        pc = random.randint(1, 3)
        if pc == 1:
            pc = 'piedra'
        elif pc == 2:
            pc = 'tijera'
        else:
            pc = 'papel'
        
        #Hora del juego
        print('Piedra, Papel o Tijera!')
        time.sleep(1)
        print('1')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('3')
        time.sleep(1)
        print('La pc ha elegido: ', pc)

        #Comprobacion de los resultados
        if pc == jugador:
            print('Empate')
            time.sleep(2)
        elif jugador == 'piedra' and pc == 'tijera':
            print('Ganaste!')
            mipuntaje += 1
            time.sleep(1)
        elif jugador == 'papel' and pc == 'piedra':
            print('Ganaste!')
            mipuntaje += 1
            time.sleep(1)
        elif jugador == 'tijera' and pc == 'papel':
            print('Ganaste!')
            mipuntaje += 1
            time.sleep(1)
        else:
            print('Perdiste :( ')
            puntajepc += 1
        print('Mi puntaje: ', mipuntaje)
        print('Puntaje pc: ', puntajepc)
        time.sleep(2)
        print('Nuevo Juego')
    else:
        print('Escoge una opcion correcta')
        

        
