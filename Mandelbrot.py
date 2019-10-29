import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import sqrt

def madelbrot(x, y, max_step):
    c = complex(x, y)
    z = 0
    for step in range(0, max_step):
        if (abs(z) > 2):
            return step
        z = z * z + c
    return max_step

pixel = 500
pixels_N = np.zeros([pixel, pixel])

# Default: [-1, 1, -2, 1]
for row, y in enumerate(np.linspace(-1, 1, num=pixel)):
    for column, x in enumerate(np.linspace(-2, 1, num=pixel)):
        pixels_N[row, column] = madelbrot(x, y, max_step=100)

plt.figure(dpi=100)
plt.imshow(pixels_N, cmap="binary_r", interpolation="bilinear", extent=[-2, 1, -1, 1])
plt.title("Mandelbrot set")
plt.ylabel("Imaginary")
plt.xlabel("Real")

plt.show()
