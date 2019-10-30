#0.1100, 0.1104
#-0.7460, -0.7465

#0.110002, 0.110004
#-0.746000, -0.746003

import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

def mandelbrot(re, im, max_step):
    c = complex(re, im)
    z = 0
    for step in range(0, max_step):
        if (abs(z) > 2):
            return step
        z = z * z + c
    return max_step

def mandelbrot_set(pixel, max_step):
    pixels_N = np.zeros([pixel, pixel])
    # Default: [-1, 1, -2, 1]
    for row, im in enumerate(np.linspace(-1, 1, num=pixel)):
        for column, re in enumerate(np.linspace(-2, 1, num=pixel)):
            pixels_N[row, column] = madelbrot(re, im, max_step)
    return pixels_N

pixel = 500
max_step = 100

plt.imshow(pixels(pixel, max_step), cmap="binary_r", interpolation="bilinear", extent=[-2, 1, -1, 1])
plt.title("Mandelbrot set")
plt.ylabel("Imaginary")
plt.xlabel("Real")

plt.show()
