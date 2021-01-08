import random
juego = {
    1: 'piedra',
    2: 'papel',
    3: 'tijeras',
    4: 'lagarto',
    5: 'spock'
}

resultado = {
    ('tijeras','papel'): True,
    ('tijeras','lagarto'): True,
    ('tijeras','spock'): False,
    ('tijeras','piedra'): False,

    ('papel','lagarto'): False,
    ('papel','tijeras'): False,
    ('papel','spock'): True,
    ('papel','piedra'): True,

    ('piedra','spock'): False,
    ('piedra','tijeras'): True,
    ('piedra','papel'): False,
    ('piedra','lagarto'): True,
    
    ('spock','papel'): False,
    ('spock','tijeras'): True,
    ('spock','piedra'): True,  
    ('spock','lagarto'): False,   

    ('lagarto','spock'): True,
    ('lagarto','papel'): True,
    ('lagarto','tijeras'): False,
    ('lagarto','piedra'): False,
}

victorias=0
empates=0
derrotas=0

i=True

#hasta que el usuario quiera, puede parar.
while i== True:
  print("______________________________")
  print("Opcion 1: JUGAR")
  print("Opcion 2: SALIR")
  opcion=int(input("Eliga una opcion: " ))
  print("\n")
  if opcion==1:
    compu = random.randint(1,5)
    for clave,valor in juego.items():
      print(clave,valor)
    jugador = int(input('Ingresa una opción ------> '))
    print('Jugador eligió >>>>',juego[jugador])
    print('PC eligió >>>>',juego[compu]) 
    #contador de partidas.
    if juego[jugador] == juego[compu]:
      empates +=1
      print("Empate!")
    elif(resultado[(juego[jugador],juego[compu])]):
      victorias +=1
      print("Ganaste!")
    else:
      derrotas +=1
      print("Perdiste!")
  elif opcion==2:
    print("____MARCADOR FINAL____: ","\n", "victorias: ", victorias,"\n", "Derrotas: ", derrotas,"\n", "Empates: ", empates )
    break
  i==True
  print("\n \n \n ") 
