import matplotlib.pyplot as plt
import numpy as np
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
def mandelbrotSet(y, x, zoom, pixels, max_i):
    pixels_N = np.empty([pixels, pixels])
    for row, im in enumerate(np.linspace(y-zoom, y+zoom, pixels)):
        for column, re in enumerate(np.linspace(x-zoom, x+zoom, pixels)):
            pixels_N[row, column] = mandelbrot(re, im, max_i)
    return pixels_N

# Display mandelbrot set
def image(y, x, zoom, pixels, max_i):
    # Figure size
    plt.figure(figsize=(5.5, 5))
    # Style and layout
    plt.style.use("seaborn")
    plt.tight_layout()
    # Image
    pixels_N = mandelbrotSet(y, x, zoom, pixels, max_i)
    plt.imshow(pixels_N, cmap="binary_r", interpolation="sinc", extent=[x-zoom, x+zoom, y-zoom, y+zoom])
    # Labels
    plt.title("Mandelbrot set")
    plt.ylabel("Imaginary")
    plt.xlabel("Real")
    # Remove grid
    plt.grid(b=False)
    # Show
    plt.show()

# Zooms: http://www.cuug.ab.ca/dewara/mandelbrot/images.html
image(y=0.266, x=-0.925, zoom=0.032, pixels=500, max_i=1000)
