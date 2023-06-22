import pygame
import random
from algoritmos import *
import time


class StopSorting(Exception):
    pass


def mostrar_intercambio(ventana, v):
    dibujar(ventana, v)

    # interrumpir el algoritmo de ordenamiento si se aprieta la tecla R
    pygame.event.pump()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                raise StopSorting


def cambiar_algoritmo(algoritmos, actual, cambio):  # cambio va a ser 1, o -1
    actual += cambio
    n = len(algoritmos)
    # validar que no tengamos un índice fuera de rango
    if actual == n:
        actual = 0
    elif actual < 0:
        actual = n - 1

    print('Algoritmo:', algoritmos[actual].__name__)  # mostrar el nombre de la función del algoritmo actual
    return actual


def resetear(ventana, array):
    random.shuffle(array)
    dibujar(ventana, array)


def dibujar(ventana, array):
    n = len(array)
    ancho_ventana, alto_ventana = ventana.get_width(), ventana.get_height()

    # mismo ancho para todas las barras
    ancho_barra = ancho_ventana // n

    # fondo negro
    pygame.draw.rect(ventana, 'black', (0, 0, ancho_ventana, alto_ventana))

    for i in range(n):
        # si el alto de la barra con el número más alto es igual al alto de la ventana, entonces, por regla de 3 simple:
        alto_barra = array[i] * alto_ventana // n

        # coordenadas de la esquina superior izquierda de la barra
        x = i * ancho_barra
        y = alto_ventana - alto_barra

        # en HSV, los colores tienen Hue [0-360] (tono), Saturation [0-100] (saturación) y Value [0-100] (brillo)
        # si pusiéramos la saturación y el brillo al máximo y el tono dependiera de la altura de la barra:
        tono = array[i] * 360 // n
        color = pygame.Color(0, 0, 0)
        color.hsva = (tono, 100, 100)

        # dibujar rectángulo
        pygame.draw.rect(ventana, color, (x, y, ancho_barra, alto_barra))

    time.sleep(0.002)
    pygame.display.update()


def principal():
    # cantidad de elementos del array
    N = 1080
    # determinamos ancho y alto de la ventana. El máximo es 1080x360
    max_ancho = 1080
    alto = 360
    n = min(max_ancho, N)
    ancho = max_ancho // n * n

    # inicializamos la ventana
    pygame.init()
    ventana = pygame.display.set_mode((ancho, alto))

    # crearmos, mezclamos y dibujamos array
    array = [num for num in range(1, n + 1)]
    resetear(ventana, array)

    # guardamos todos los algoritmos en un arreglo para poder ir cambiándolo durante la visualización
    algoritmos = [bubble_sort, insertion_sort, shell_sort, heap_sort, quick_sort]
    actual = 0

    # loop que mantiene abierta la ventana
    abierto = True
    while abierto:
        for event in pygame.event.get():
            # cerrar
            if event.type == pygame.QUIT:
                abierto = False

            elif event.type == pygame.KEYDOWN:
                # resetear con R
                if event.key == pygame.K_r:
                    resetear(ventana, array)

                # ordenar con espacio
                elif event.key == pygame.K_SPACE:
                    try:
                        algoritmos[actual](ventana, array, mostrar_intercambio)
                    except StopSorting:
                        resetear(ventana, array)

                # cambiar algoritmo actual con flechitas
                elif event.key == pygame.K_RIGHT:
                    actual = cambiar_algoritmo(algoritmos, actual, 1)
                    resetear(ventana, array)
                elif event.key == pygame.K_LEFT:
                    actual = cambiar_algoritmo(algoritmos, actual, -1)
                    resetear(ventana, array)

    # cerramos ventana
    pygame.quit()


if __name__ == '__main__':
    principal()
