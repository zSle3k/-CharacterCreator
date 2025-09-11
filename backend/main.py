import numpy as np
from PIL import Image
import hashlib

np.random.seed(100)

IMAGE_FORMAT = "png"    

class ImageCreator:
    """Va a permitir crear una imagen dando una altura y un ancho"""
    def __init__(self, width, heights):
        self.witdh = width
        self.height = heights
        # R G B
        self.image = np.zeros((heights, width, 3), dtype=np.uint8)
# [[[0, 0, 0]..[0, 0, 0]...[0, 0, 0]]...]

class ImageManipulations:
    """Va a ser la clase que va a permitir hacer manipulaciones de pixeles"""
    def __init__(self, image):
        self.image = image

    def write_pixel_with_color(self, x, y, color):
        self.image[y, x] = color
    
    def make_rectangle(self, x, y, width, height, color):
        """Dibuja un rectangulo en la imagen en el luenzo en la cordenada x e y y con largo y ancho"""
        for i in range(x, x + width):
            for j in range(y, y + height):
                # x: 2 y: 0 w: 2 h: 2
                # [ 0 0 1 1 ]
                # [ 0 0 1 1 ]
                self.write_pixel_with_color(x+i, y+j, color)

    def make_squire(self, x, y, side, color):      
        """Dibuja un cuadrado en la imagen en el luenzo en la cordenada x e y y con lado"""
        self.make_rectangle(x, y, side, side, color)

    def make_circle(self, x0, y0, radius, color):
        """Draw a circle using the midpoint circle algorithm.
        
        Args:
            x0, y0: Center coordinates of the circle
            radius: Radius of the circle
            color: RGB color as a list [R, G, B]
        """
        x = radius
        y = 0
        err = 0

        while x >= y:
            self.write_pixel_with_color(x0 + x, y0 + y, color)
            self.write_pixel_with_color(x0 + y, y0 + x, color)
            self.write_pixel_with_color(x0 - y, y0 + x, color)
            self.write_pixel_with_color(x0 - x, y0 + y, color)
            self.write_pixel_with_color(x0 - x, y0 - y, color)
            self.write_pixel_with_color(x0 - y, y0 - x, color)
            self.write_pixel_with_color(x0 + y, y0 - x, color)
            self.write_pixel_with_color(x0 + x, y0 - y, color)
            
            if err <= 0:
                y += 1
                err += 2*y + 1
            if err > 0:
                x -= 1
                err -= 2*x + 1

def save_image(image, filmname):
    Image.fromarray(image)\
        .save(f"img/{filmname}.{IMAGE_FORMAT}")

# Funcion de hash

def get_hash(data):
    # Unicode son numeros
    return hashlib.sha256(data.encode()).hexdigest()

#
#
#

# Definicion del sistema
# El sistema tiene que tener funciones para moverse a la derecha y hacia abajo pero no hacia arriba
#  A esto se le denmino cursores x e y
# Ademas tiene que tener un brush color que es el color
# Metodos del sistema
# Moverse_hacia_derecha()
# Moverse_hacia_abajo()
# Cambiar_color(r, g, b)
# Pintar_cuadrado()
# Generar una imagen
# Generar un color aleatorio y pintarlo en una posicion aleatoria
# //Sistema es cualquier cosa que tenga un limite



# Codigo de prueba
# Generar un pequeño set de intrucciones que ndique como manpular la imagen
# 0 16 # argumentos
# 0 -> cambiar color a segun los sigueinte 3 pares de digitos
# 1 -> Invertir el color
# 2 -> generar cuadrado x e y
# 3 -> Genear un color aleatorio y lo aplica a una posicion aleatoria
# 4 -> moverse a la derecha
# 5 -> moverse hacia abajo
# 6 -> Abrir una imagen existente reescalarla y aplicarla como liezo
# 7 -> Dividir los colores de la brocha por 2
# 8 -> Rotar la imagen segun lo que diga el par de numero siguiente

class CJOImplementation:
    def __init__(self, hash_string):
        # Programa.
        self.hash_string = hash_string # Interpretar este numero como el actual
        self.image = ImageCreator(600, 600)
        self.im = ImageManipulations(self.image.image)
        self.cursor_x = 0
        self.cursor_y = 0
        self.brush = [255, 255, 255]

if __name__ == "__main__":
    width, height = 600, 600
    im = ImageCreator(width, height)
    im = ImageManipulations(im.image)
    im.make_circle(200, 200, 200, (255, 0, 0))
    save_image(im.image, "test")

    #print(get_hash("Hola mundo"))
    
    

