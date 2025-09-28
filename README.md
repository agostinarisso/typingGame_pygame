# TypingEdu - Juego de Mecanografía

Un juego educativo desarrollado en Python usando Pygame para ayudar a practicar mecanografía de una manera divertida.

## Descripción

En este juego, las letras caen desde la parte superior de la pantalla y el jugador debe escribirlas usando el teclado antes de que lleguen al fondo. Un hada mágica atrapará las letras correctamente tecleadas, aumentando la puntuación del jugador.

## Características

- Interfaz gráfica intuitiva y amigable
- Sistema de puntuación
- Efectos visuales y retroalimentación inmediata
- Personaje animado (hada) que atrapa las letras
- Mensajes de motivación

## Requisitos

- Python 3.x
- Pygame

## Instalación

1. Clona este repositorio
2. Crea un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Windows: .venv\Scripts\activate
   ```
3. Instala las dependencias:
   ```bash
   pip install pygame
   ```

## Cómo jugar

1. Ejecuta el juego:
   ```bash
   python main.py
   ```
2. Presiona ESPACIO para comenzar
3. Escribe las letras que van cayendo antes de que lleguen al fondo
4. Presiona ESC para salir

## Estructura del proyecto

```
TP2/
├── main.py           # Punto de entrada del juego
├── lib/              # Módulos del juego
│   ├── letra.py     # Clase para manejar las letras
│   ├── personaje.py # Clase del personaje (hada)
│   └── gestor_mensajes.py # Sistema de mensajes
└── sprite/           # Recursos gráficos
    ├── fondos/      # Imágenes de fondo
    └── personajes/  # Sprites de personajes
```

## Controles

- ESPACIO: Iniciar juego
- Letras (A-Z): Capturar letras
- ESC: Salir del juego
