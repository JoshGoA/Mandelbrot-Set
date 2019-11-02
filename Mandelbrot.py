import numpy as np
import matplotlib.pyplot as plt
from numba import jit

# Calculate mandelbrot set numbers
@jit(nopython=True)
def mandelbrot(re, im, max_i):
    c = complex(re, im)
    z = 0
    for i in range(0, max_i):
        if (abs(z) > 2):
            return i
        z = z * z + c
    return max_i

# Arrange each number value in array
def mandelbrotSet(miny, maxy, minx, maxx, pixels, max_i):
    pixels_N = np.empty([pixels, pixels])
    for row, im in enumerate(np.linspace(miny, maxy, pixels)):
        for column, re in enumerate(np.linspace(minx, maxx, pixels)):
            pixels_N[row, column] = mandelbrot(re, im, max_i)
    return pixels_N

# Display mandelbrot set
def image(miny, maxy, minx, maxx, pixels, max_i):
    # Figure size
    plt.figure(figsize=(5.5, 5))
    # Style and layout
    plt.style.use("seaborn")
    plt.tight_layout()
    # Image
    pixels_N = mandelbrotSet(miny, maxy, minx, maxx, pixels, max_i)
    plt.imshow(pixels_N, cmap="binary_r", interpolation="sinc", extent=[minx, maxx, miny, maxy])
    # Labels
    plt.title("Mandelbrot set")
    plt.ylabel("Imaginary")
    plt.xlabel("Real")
    # Remove grid
    plt.grid(b=False)
    # Show
    plt.show()

# Default: miny=-1, maxy=1, minx=-2, maxx=1, pixels=500, max_i=100
# Zoom 1: miny=0.11, maxy=0.12, minx=-0.74, maxx=-0.75, pixels=500, max_i=1000
image(miny=0.11, maxy=0.12, minx=-0.74, maxx=-0.75, pixels=500, max_i=1000)
