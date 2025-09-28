# Configuración de la ventana
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 1024
FPS = 60
TITLE = "TypingEdu - Aprende mecanografía"

# Estados del juego
ESTADO_INICIO = 'inicio'
ESTADO_JUGANDO = 'jugando'
ESTADO_PAUSA = 'pausa'
ESTADO_FINAL = 'final'

# Configuración del juego
INITIAL_SPEED = 2
SPEED_INCREMENT = 0.5
SPAWN_DELAY = 2000  # milisegundos entre cada letra
MIN_SPAWN_DELAY = 500  # mínimo delay entre letras
LETTER_SIZE = 48  # Tamaño de la fuente para las letras
LETTER_FONT = 'Arial'  # Fuente para las letras
LETTER_BOLD = True  # Letra en negrita

# Puntuación
POINTS_CORRECT = 1
POINTS_WRONG = 0
POINTS_TO_NEXT_LEVEL = 10

# Rutas de recursos
SPRITE_PATH = "sprite/"
FONTS_PATH = "sprite/fonts/"
BACKGROUNDS_PATH = "sprite/fondos/"
CHARACTERS_PATH = "sprite/personajes/"

# Configuración de letras
LETTER_SIZE = 64  # Letras más grandes
LETTER_FONT = "Comic Sans MS"  # Fuente más amigable para niños
LETTER_BOLD = True  # Letras en negrita

# Estados del juego
ESTADO_INICIO = 0
ESTADO_JUGANDO = 1

# Mensajes del juego
WELCOME_MESSAGE = "¡Bienvenido a TypingEdu!"
INSTRUCTIONS = "Presiona las letras antes de que toquen el suelo"
