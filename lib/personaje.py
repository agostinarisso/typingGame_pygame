import pygame
import os
from .var import *

class Personaje:
    def __init__(self):
        self.velocidad = 15
        self.objetivo = None
        self.letra_objetivo = None
        self._cargar_sprite()
        self._posicionar_inicial()
    
    def _cargar_sprite(self):
        """Carga y escala la imagen del personaje"""
        try:
            self.sprite = pygame.image.load(os.path.join(SPRITE_PATH, "personajes", "hada.png"))
            self.sprite = pygame.transform.scale(self.sprite, (200, 200))
            self.rect = self.sprite.get_rect()
        except Exception as e:
            raise Exception(f"Error al cargar sprite del personaje: {e}")
    
    def _posicionar_inicial(self):
        """Coloca al personaje en su posición inicial"""
        self.rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50)
    
    def actualizar(self):
        """Actualiza la posición del personaje hacia su objetivo
        Retorna: True si llegó al objetivo, False si aún está en movimiento"""
        if self.objetivo:
            dx = self.objetivo[0] - self.rect.centerx
            dy = self.objetivo[1] - self.rect.centery
            distancia = (dx**2 + dy**2)**0.5
            
            if distancia > self.velocidad:
                factor = self.velocidad / distancia
                self.rect.x += dx * factor
                self.rect.y += dy * factor
                return False
            else:
                self.rect.center = self.objetivo
                return True
        return False
    
    def dibujar(self, pantalla):
        """Dibuja el personaje en la pantalla"""
        pantalla.blit(self.sprite, self.rect)
    
    def ir_a_letra(self, letra):
        """Establece una letra como objetivo del personaje"""
        self.objetivo = letra.rectangulo.center
        self.letra_objetivo = letra
        
    def reiniciar_posicion(self):
        """Devuelve al personaje a su posición inicial"""
        self._posicionar_inicial()
        self.objetivo = None
        self.letra_objetivo = None
