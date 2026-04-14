# ejercicio2_aventura.py

import random
from datetime import datetime


def generar_nombre():
    nombres = ["Arion", "Luna", "Kael", "Zara"]
    return random.choice(nombres)


def generar_clase():
    clases = ["Guerrero", "Mago", "Arquero", "Asesino"]
    return random.choice(clases)


def generar_hp():
    return random.randint(80, 120)


def mostrar_fecha():
    fecha = datetime.now()
    print(f"Fecha: {fecha.day}/{fecha.month}/{fecha.year}")



print("=== GENERADOR DE AVENTURAS ===")

mostrar_fecha()

print("=== Heroes Generados ===")

for i in range(1, 4):
    nombre = generar_nombre()
    clase = generar_clase()
    hp = generar_hp()
    print(f"Heroe {i}: {nombre} | Clase: {clase} | HP: {hp}")