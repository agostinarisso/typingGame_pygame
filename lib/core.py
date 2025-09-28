import pygame
import random
from .var import *
from .color import *

class Letra:
    def __init__(self, caracter, x):
        self.caracter = caracter
        self.x = x
        self.y = 0
        self.velocidad = INITIAL_SPEED
        self.fuente = pygame.font.SysFont(LETTER_FONT, LETTER_SIZE)
        self.superficie = self.fuente.render(self.caracter, True, TEXT_COLOR)
        self.rectangulo = self.superficie.get_rect(center=(x, self.y))
        
    def actualizar(self):
        self.y += self.velocidad
        self.rectangulo.center = (self.x, self.y)
        
    def dibujar(self, pantalla):
        pantalla.blit(self.superficie, self.rectangulo)
        
    def esta_fuera(self):
        return self.y > WINDOW_HEIGHT
        
class Marcador:
    def __init__(self):
        self.fuente = pygame.font.SysFont(LETTER_FONT, 24)
        self.puntos = 0
        self.nivel = 1
        
    def actualizar_puntos(self, puntos):
        self.puntos += puntos
        if self.puntos >= POINTS_TO_NEXT_LEVEL * self.nivel:
            self.nivel += 1
            return True
        return False
        
    def dibujar(self, pantalla):
        texto_puntos = self.fuente.render(f"Puntos: {self.puntos}", True, TEXT_COLOR)
        texto_nivel = self.fuente.render(f"Nivel: {self.nivel}", True, TEXT_COLOR)
        pantalla.blit(texto_puntos, (10, 10))
        pantalla.blit(texto_nivel, (10, 40))

class SistemaMensajes:
    def __init__(self):
        self.fuente = pygame.font.SysFont(LETTER_FONT, 32)
        self.mensaje = ""
        self.tiempo_mostrado = 0
        self.duracion = 2000  # 2 segundos
        
    def mostrar_mensaje(self, texto):
        self.mensaje = texto
        self.tiempo_mostrado = pygame.time.get_ticks()
        
    def actualizar(self):
        if pygame.time.get_ticks() - self.tiempo_mostrado > self.duracion:
            self.mensaje = ""
            
    def dibujar(self, pantalla):
        if self.mensaje:
            texto = self.fuente.render(self.mensaje, True, TEXT_COLOR)
            rect = texto.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50))
            pantalla.blit(texto, rect)
