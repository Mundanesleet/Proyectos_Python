#Proyecto Escape Room - Alejandro Sossa - !5/04/2023
import time 

rooms= {
    'Comienzo': {'habitaciones': ['1'], 'items': []},
    '1': {'habitaciones': ['Comienzo', '2', '3'], 'items': []},
    '2': {'habitaciones': ['1'], 'items': ['llave']},
    '3': {'habitaciones': ['1', '4'], 'items': []},
    '4': {'habitaciones': ['3', '5'], 'items': []},
    '5': {'habitaciones': ['4', 'Salida'], 'items': []} 
}

room = 'Comienzo'
key = False
while True:
    print('============================')
    print('Estas en una habitacion', room)
    for near_room in rooms[room]['habitaciones']:
        print('Puedes ir a ', near_room)
    new_room = input('Que habitacion elegiras? ')
    if new_room not in rooms[room]['habitaciones']:
        print('Esta habitacion no existe')
        time.sleep(2)
        continue 
    if new_room == 'Salida' and not key:
        print('No tienes la llave')
        time.sleep(2)
        continue
    if new_room == 'Salida':
        print('Felicidades, Escapaste de la habitacion')
        time.sleep(2)
        break
    room = new_room
    if 'llave' in rooms[room]['items']:
        key = True
        print('Encontraste una llave, Usala para salir')
        rooms[room]['items'].remove('llave')
        time.sleep(2)