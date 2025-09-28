import sys
import os
import pygame
import random
from lib.var import *
from lib.color import *
from lib.letra import Letra
from lib.personaje import Personaje
from lib.gestor_mensajes import GestorMensajes

# Inicialización de Pygame
pygame.init()
pantalla = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tipeando")
reloj = pygame.time.Clock()

# Cargar recursos
try:
    fondo = pygame.image.load(os.path.join(SPRITE_PATH, "fondos", "classroom.png"))
    fondo = pygame.transform.scale(fondo, (WINDOW_WIDTH, WINDOW_HEIGHT))
except Exception as e:
    print(f"Error cargando recursos: {e}")
    print(f"Ruta actual: {SPRITE_PATH}")
    pygame.quit()
    sys.exit(1)

# Crear instancias de las clases
personaje = Personaje()
gestor_mensajes = GestorMensajes()

# Variables del juego
estado_actual = ESTADO_INICIO
letras = []
ultimo_spawn = pygame.time.get_ticks()
puntos = 0

# Fuentes para textos de inicio
fuente_titulo = pygame.font.SysFont(LETTER_FONT, 72, bold=True)
fuente_instrucciones = pygame.font.SysFont(LETTER_FONT, 69, bold=True)  # Fuente ligeramente más pequeña para instrucciones

# Crear el mensaje de inicio con sombreado para mejor visibilidad
texto_inicio_0 = fuente_titulo.render("¡No dejes caer las letras!", True, BLUE)  # Texto principal
texto_inicio0 = fuente_titulo.render("¡No dejes caer las letras!", True, BLACK)  # Sombra
texto_inicio_sub = fuente_titulo.render("usa el teclado", True, BLUE)  # Texto secundario
texto_iniciosub = fuente_titulo.render("usa el teclado", True, BLACK)  # Sombra
texto_inicio1 = fuente_instrucciones.render("Presiona la tecla ESPACIO", True, BLACK)  # Sombra
texto_inicio2 = fuente_instrucciones.render("Presiona la tecla ESPACIO", True, WHITE)  # Texto instrucción
texto_inicio3 = fuente_instrucciones.render("para comenzar", True, BLACK)  # Sombra segunda línea
texto_inicio4 = fuente_instrucciones.render("para comenzar", True, WHITE)  # Texto instrucción segunda línea

# Loop principal
salir = False
while not salir:
    tiempo_actual = pygame.time.get_ticks()
    
    # Control de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            salir = True
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                salir = True
            elif estado_actual == ESTADO_INICIO and evento.key == pygame.K_SPACE:
                estado_actual = ESTADO_JUGANDO
                personaje.reiniciar_posicion()  # Asegurar posición inicial
            elif estado_actual == ESTADO_JUGANDO:
                # Verificar si la tecla coincide con alguna letra
                tecla = evento.unicode.upper()
                letra_encontrada = False
                for letra in letras[:]:
                    if letra.caracter == tecla and not personaje.objetivo:
                        personaje.ir_a_letra(letra)
                        letra.seleccionada = True
                        gestor_mensajes.mostrar_exito()
                        letra_encontrada = True
                        break
                
                if tecla and not letra_encontrada and not personaje.objetivo:
                    gestor_mensajes.mostrar_error()

    # Generar nuevas letras
    if estado_actual == ESTADO_JUGANDO and tiempo_actual - ultimo_spawn > SPAWN_DELAY:
        caracter = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        x = random.randint(LETTER_SIZE, WINDOW_WIDTH - LETTER_SIZE)
        letras.append(Letra(caracter, x, puntos))  # Pasamos los puntos actuales
        ultimo_spawn = tiempo_actual

    # Actualizar letras
    for letra in letras[:]:
        letra.actualizar()
        if letra.esta_fuera():
            letras.remove(letra)
            if not letra.seleccionada:
                gestor_mensajes.mostrar_caida()

    # Actualizar personaje y comprobar si alcanzó su objetivo
    if personaje.actualizar() and personaje.letra_objetivo:
        letras.remove(personaje.letra_objetivo)
        puntos += 1
        personaje.letra_objetivo = None
        personaje.objetivo = None

    # Limpiar pantalla y dibujar fondo
    pantalla.fill(BLACK)
    pantalla.blit(fondo, (0, 0))

    if estado_actual == ESTADO_INICIO:
        # Dibujar texto de inicio con efecto de sombreado
        # Título principal - "¡No dejes caer las letras!"
        rect_sombra0 = texto_inicio0.get_rect(center=(WINDOW_WIDTH//2 + 2, WINDOW_HEIGHT//2 - 150 + 2))
        rect_texto0 = texto_inicio_0.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 150))
        
        # Subtítulo - "usa el teclado"
        rect_sombra_sub = texto_iniciosub.get_rect(center=(WINDOW_WIDTH//2 + 2, WINDOW_HEIGHT//2 - 70 + 2))
        rect_texto_sub = texto_inicio_sub.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 70))
        
        # Instrucción - "Presiona la tecla ESPACIO"
        rect_sombra1 = texto_inicio1.get_rect(center=(WINDOW_WIDTH//2 + 2, WINDOW_HEIGHT//2 + 20 + 2))
        rect_texto2 = texto_inicio2.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 20))
        
        # "para comenzar"
        rect_sombra3 = texto_inicio3.get_rect(center=(WINDOW_WIDTH//2 + 2, WINDOW_HEIGHT//2 + 80 + 2))
        rect_texto4 = texto_inicio4.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 80))

        # Dibujar primero las sombras
        pantalla.blit(texto_inicio0, rect_sombra0)
        pantalla.blit(texto_iniciosub, rect_sombra_sub)
        pantalla.blit(texto_inicio1, rect_sombra1)
        pantalla.blit(texto_inicio3, rect_sombra3)
        
        # Luego dibujar los textos principales
        pantalla.blit(texto_inicio_0, rect_texto0)
        pantalla.blit(texto_inicio_sub, rect_texto_sub)
        pantalla.blit(texto_inicio2, rect_texto2)
        pantalla.blit(texto_inicio4, rect_texto4)
    else:
        # Dibujar elementos del juego
        for letra in letras:
            letra.dibujar(pantalla)
        
        personaje.dibujar(pantalla)

        # Dibujar puntuación
        texto_puntos = gestor_mensajes.fuente.render(f'Puntos: {puntos}', True, WHITE)
        pantalla.blit(texto_puntos, (10, 10))

        # Dibujar mensaje actual
        gestor_mensajes.dibujar(pantalla)
    
    # Actualizar pantalla
    pygame.display.flip()
    reloj.tick(FPS)

# Finalizar Pygame
pygame.quit()
sys.exit()
