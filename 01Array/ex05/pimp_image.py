from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = ft_load("landscape.jpg")
if not isinstance(img, np.ndarray):
    raise TypeError("The loaded object is not a NumPy array.")
hauteur, largeur,  _ = img.shape
center_x = largeur // 2
center_y = hauteur // 2
left = center_x - 200
upper = center_y - 200
right = center_x + 200
lower = center_y + 200

# Découpage de l'image
img_pil = Image.open("landscape.jpg")
cropped_img = img_pil.crop((left, upper, right, lower))

# Conversion et extraction du canal rouge
array = np.array(cropped_img)
red_channel = array[:, :, 0]


def ft_invert(array) -> array:
    """
    Inverse les couleurs de l'image reçue.
    Chaque pixel devient 255 - valeur.
    """
    inverted = 255 - array
    plt.imshow(inverted)
    plt.title("inverted Image")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.axis('on')
    plt.show()
    return inverted


def ft_red(array) -> array:
    """
    Conserve uniquement le canal rouge de l'image.
    Les canaux vert et bleu sont mis à zéro.
    """
    red = array.copy()
    red[:, :, 1] = 0
    red[:, :, 2] = 0
    plt.imshow(red)
    plt.title("red Image")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.axis('on')
    plt.show()
    return red


def ft_green(array) -> array:
    """
    Conserve uniquement le canal green de l'image.
    Les canaux rouge et bleu sont mis à zéro.
    """
    green = array.copy()
    green[:, :, 0] = 0
    green[:, :, 2] = 0
    plt.imshow(green)
    plt.title("green Image")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.axis('on')
    plt.show()
    return green


def ft_blue(array) -> array:
    """
    Conserve uniquement le canal blue de l'image.
    Les canaux green et rouge sont mis à zéro.
    """
    blue = array.copy()
    blue[:, :, 0] = 0
    blue[:, :, 1] = 0
    plt.imshow(blue)
    plt.title("blue Image")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.axis('on')
    plt.show()
    return blue


def ft_grey(array) -> array:
    """
    Convertit l'image en niveaux de gris.
    Chaque pixel devient la moyenne de R, G et B.
    """
    grey = array.mean(axis=2).astype(np.uint8)
    plt.imshow(grey, cmap='gray')
    plt.title("Grey Image")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.axis('on')
    plt.show()
    return grey
