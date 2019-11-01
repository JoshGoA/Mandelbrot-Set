#0.1100, 0.1104
#-0.7460, -0.7465

#0.110002, 0.110004
#-0.746000, -0.746003

import numpy as np
import matplotlib.pyplot as plt
from numba import jit

@jit(nopython=True)
def mandelbrot(re, im, max_i):
    c = complex(re, im)
    z = 0
    for i in range(0, max_i):
        if (abs(z) > 2):
            return i
        z = z * z + c
    return max_i

def mandelbrotSet(miny, maxy, minx, maxx, pixels, max_i):
    pixels_N = np.empty([pixels, pixels])
    for row, im in enumerate(np.linspace(miny, maxy, pixels)):
        for column, re in enumerate(np.linspace(minx, maxx, pixels)):
            pixels_N[row, column] = mandelbrot(re, im, max_i)
    return pixels_N

def image(miny, maxy, minx, maxx, pixels, max_i):
    pixels_N = mandelbrotSet(miny, maxy, minx, maxx, pixels, max_i)
    plt.imshow(pixels_N, cmap="binary_r", interpolation="sinc", extent=[minx, maxx, miny, maxy])
    plt.title("Mandelbrot set")
    plt.ylabel("Imaginary")
    plt.xlabel("Real")

# Default: miny=-1, maxy=1, minx=-2, maxx=1, pixels=500, max_i=100
image(miny=-1, maxy=1, minx=-2, maxx=1, pixels=500, max_i=100)
plt.show()
