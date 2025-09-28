import pygame
import random
from .var import *
from .color import *

class Letra:
    @staticmethod
    def get_velocidad_nivel(puntos):
        """Calcula la velocidad basada en los puntos actuales"""
        nivel = puntos // 10  # Cada 10 puntos sube un nivel
        velocidad_base = INITIAL_SPEED
        if nivel > 0:
            velocidad_base += (nivel * 0.5)  # Aumenta 0.5 por nivel
        return velocidad_base

    def __init__(self, caracter, x, puntos_actuales=0):
        self.caracter = caracter
        self.x = x
        self.y = 0
        self.velocidad = self.get_velocidad_nivel(puntos_actuales)
        self.seleccionada = False
        self._crear_superficie()
    
    def _crear_superficie(self):
        """Crea la superficie de la letra con un color aleatorio"""
        self.fuente = pygame.font.SysFont(LETTER_FONT, LETTER_SIZE, bold=LETTER_BOLD)
        color_letra = random.choice([TEXT_COLOR, SUCCESS, HIGHLIGHT])
        self.superficie = self.fuente.render(self.caracter, True, color_letra)
        self.rectangulo = self.superficie.get_rect(center=(self.x, self.y))
        
    def actualizar(self):
        """Actualiza la posición de la letra si no está seleccionada"""
        if not self.seleccionada:
            self.y += self.velocidad
            self.rectangulo.center = (self.x, self.y)
        
    def dibujar(self, pantalla):
        """Dibuja la letra en la pantalla"""
        pantalla.blit(self.superficie, self.rectangulo)
        
    def esta_fuera(self):
        """Verifica si la letra está fuera de la pantalla"""
        return self.y > WINDOW_HEIGHT
