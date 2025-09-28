import pygame
import random
from .var import *
from .color import *

class GestorMensajes:
    def __init__(self):
        self.mensajes_exito = ["¡Bien hecho!", "¡Excelente!", "¡Genial!", "¡Sigue así!", "¡Fantástico!"]
        self.mensajes_error = ["¡Ups!", "¡Inténtalo de nuevo!", "¡Casi!", "¡Sigue intentando!"]
        self.mensajes_caida = ["¡Se escapó!", "¡Más rápido!", "¡No la dejes caer!", "¡Cuidado!"]
        self.mensaje_actual = ""
        self.tiempo_mensaje = 0
        self.color_mensaje = WHITE
        self.fuente = pygame.font.SysFont(LETTER_FONT, 36)
    
    def mostrar_exito(self):
        """Muestra un mensaje de éxito aleatorio"""
        self.mensaje_actual = random.choice(self.mensajes_exito)
        self.color_mensaje = BLUE
        self.tiempo_mensaje = pygame.time.get_ticks()
    
    def mostrar_error(self):
        """Muestra un mensaje de error aleatorio"""
        self.mensaje_actual = random.choice(self.mensajes_error)
        self.color_mensaje = RED
        self.tiempo_mensaje = pygame.time.get_ticks()
    
    def mostrar_caida(self):
        """Muestra un mensaje de letra caída aleatorio"""
        self.mensaje_actual = random.choice(self.mensajes_caida)
        self.color_mensaje = RED
        self.tiempo_mensaje = pygame.time.get_ticks()
    
    def dibujar(self, pantalla):
        """Dibuja el mensaje actual si está dentro del tiempo de visualización"""
        if self.mensaje_actual and pygame.time.get_ticks() - self.tiempo_mensaje < 1000:
            texto = self.fuente.render(self.mensaje_actual, True, self.color_mensaje)
            rect = texto.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT - 100))
            pantalla.blit(texto, rect)
