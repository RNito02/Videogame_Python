import pygame


class Enemigo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = 50
        self.alto = 50
        self.velocidad = .33
        self.color = (98, 39, 232)  # Definir el color rojo en RGB
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)

    def dibujar(self, ventana):  # Cambié "seft" a "self"
        self.color = (98, 39, 232)  # Definir el color rojo en RGB
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        pygame.draw.rect(ventana, self.color, self.rect)

    def movimiento(self):
        self.y += self.velocidad
