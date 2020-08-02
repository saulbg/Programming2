# Juego de piedra, papel, tijeras, lagarto o spock

# REGLAS
# Piedra gana a tijeras y lagarto
# Tijeras gana a papel y lagarto
# Papel gana a piedra y Spock
# Lagarto gana a spock y papel
# Spock gana a tijeras y piedra

# Importamos la funcion random para seleccionar aleatoriamente la palabra
import random
# Importamos la funcion sleep para dar una pausa entre cada instrucción
import time
from time import sleep

# Creamos lista de palabras
options=["piedra","papel","tijeras","lagarto","spock"]

# Usamos un while para jugar indefinidamente
while True:
  # Pedimos que ingrese la opción
  eleccion=input("Selecciona piedra, papel, tijeras, lagarto o spock:  ").lower()
  # Hacemos una pausa
  sleep(1.0)
  
  # Condicional para verificar que sea una opción valida
  if eleccion not in options:
    print("No es valida esa opcion, elige de nuevo \n")
    continue
  
  # Hacemos que el cpu seleccione aletoriamente
  cpu= random.choice(options)
  sleep(1.0)
  print(f"El CPU eligió {cpu} \n")
  sleep(1.0)
  
  # Condicional para checar si fue empate
  if eleccion == cpu:
    print(f"Ha sido un empate, ambos eligieron {cpu}\n")
  
  # Condicionales para decidir si gana
  elif eleccion== "piedra" and cpu== "tijeras":
    print(f"El usuario ha ganado! {eleccion} aplasta a {cpu}\n")
  elif eleccion== "piedra" and cpu== "lagarto":
    print(f"El usuario ha ganado! {eleccion} aplasta a {cpu}\n")

  elif eleccion== "tijeras" and cpu== "papel":
    print(f"El usuario ha ganado! {eleccion} cortan el  {cpu}\n")
  elif eleccion== "tijeras" and cpu== "lagarto":
    print(f"El usuario ha ganado! {eleccion} decapitan a {cpu}\n")

  elif eleccion== "papel" and cpu== "piedra":
    print(f"El usuario ha ganado! {eleccion} envuelve a {cpu}\n")
  elif eleccion== "papel" and cpu== "spock":
    print(f"El usuario ha ganado! {eleccion} desaprueba a {cpu}\n")
  
  elif eleccion== "lagarto" and cpu== "spock":
    print(f"El usuario ha ganado! {eleccion} envenena a {cpu}\n")
  elif eleccion== "lagarto" and cpu== "papel":
    print(f"El usuario ha ganado! {eleccion} se come el {cpu}\n")
  
  elif eleccion== "spock" and cpu== "tijeras":
    print(f"El usuario ha ganado! {eleccion} aplasta a {cpu}\n")
  elif eleccion== "spock" and cpu== "piedra":
    print(f"El usuario ha ganado! {eleccion} desintegra a {cpu}\n")

  # Si no se cumple una condicional donde gane entonces pierde
  else:
    print(f"Perdiste :(, {cpu} le gana a {eleccion}\n")
  break



