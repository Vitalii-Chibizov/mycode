import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    img = np.empty((width, height))

    for i in range(width):
        for j in range(height):
            img[i, j] = mandelbrot(x[i] + 1j * y[j], max_iter)

    return img

if __name__ == "__main__":
    xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
    width, height = 800, 600
    max_iter = 256

    fractal = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)

    plt.imshow(fractal.T, extent=(xmin, xmax, ymin, ymax))
    plt.title("Mandelbrot Fractal")
    plt.show()

