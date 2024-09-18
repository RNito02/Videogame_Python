from personaje import Cubo
from enemigo import Enemigo
import pygame


pygame.init()

ANCHO = 800
ALTO = 600  # Cambié el orden para que ancho sea horizontal y alto vertical
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
FPS: 60

jugando = True

reloj = pygame.time.Clock()

tiempo_pasado = 0
tiempo_entre_enemigos = 500

cubo = Cubo(100, 100)

enemigos = []

enemigos.append(Enemigo(ANCHO/2, 100))


def gestiona_teclas(teclas):
    if teclas[pygame.K_w]:
        cubo.y -= cubo.velocidad
    if teclas[pygame.K_s]:
        cubo.y += cubo.velocidad
    if teclas[pygame.K_a]:
        cubo.x -= cubo.velocidad
    if teclas[pygame.K_d]:
        cubo.x += cubo.velocidad


while jugando:

    tiempo_pasado += reloj.tick(80)

    print(tiempo_pasado)

    eventos = pygame.event.get()

    teclas = pygame.key.get_pressed()

    gestiona_teclas(teclas)

    for evento in eventos:
        if evento.type == pygame.QUIT:
            jugando = False

    VENTANA.fill(("black"))
    cubo.dibujar(VENTANA)

    for enemigo in enemigos:
        enemigo.dibujar(VENTANA)
        enemigo.movimiento()

    pygame.display.update()

pygame.quit()
