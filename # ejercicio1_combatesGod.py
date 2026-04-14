# ejercicio1_combatesGod.py
def calcular_dano(ataque, defensa):
    dano = ataque - defensa
    if dano < 0:
        return 0
    return dano
#Sección para aplicar dano mi so
def aplicar_dano(hp_actual, dano):
    nuevo_hp = hp_actual - dano
    if nuevo_hp < 0:
        return 0
    return nuevo_hp

def mostrar_estado(nombre, hp, hp_max=100):
    print(f"{nombre}: {hp}/{hp_max}")


def realizar_ataque(atacante, defensor, dano):
    print(f"{atacante} ataca a {defensor} por {dano} de dano!")


hp_heroe = 100
hp_enemigo = 50

# Estado inicial del Heroe y enemigo
mostrar_estado("Héroe", hp_heroe)
mostrar_estado("Enemigo", hp_enemigo)


dano = calcular_dano(ataque=25, defensa=10)
realizar_ataque("Héroe", "Enemigo", dano)

hp_enemigo = aplicar_dano(hp_enemigo, dano)

mostrar_estado("Enemigo", hp_enemigo)


dano = calcular_dano(ataque=25, defensa=10)
realizar_ataque("Héroe", "Enemigo", dano)

hp_enemigo = aplicar_dano(hp_enemigo, dano)

mostrar_estado("Enemigo", hp_enemigo)