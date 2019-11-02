import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
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

# Run animation
def run_animation():

    anim_running = True

    # Stop animation
    def onClick(event):
        if event.dblclick:
            anim.frame_seq = anim.new_frame_seq()
        else:
            nonlocal anim_running
            if anim_running:
                anim.event_source.stop()
                anim_running = False
            else:
                anim.event_source.start()
                anim_running = True

    # Define animation
    def func(i):
        # Remove previous drawing
        plt.cla()
        # Style and layout
        plt.style.use("seaborn")
        plt.tight_layout()
        # Labels
        ax.set_title("Mandelbrot set")
        ax.set_ylabel("Imaginary")
        ax.set_xlabel("Real")
        # Remove grid
        ax.grid(b=False)
        # Image
        # Default: miny=-1, maxy=1, minx=-2, maxx=1, pixels=500, max_i=i
        pixels_N = mandelbrotSet(miny=-1, maxy=1, minx=-2, maxx=1, pixels=500, max_i=i)
        im = ax.imshow(pixels_N, cmap="binary_r", interpolation="sinc", extent=[-2, 1, -1, 1])
        return im

    # Connect fig to click
    fig.canvas.mpl_connect('button_press_event', onClick)

    # Repeat animation
    anim = animation.FuncAnimation(fig, func)

# Subplots
fig, ax = plt.subplots(figsize=(8.5, 5))

# Instructions
print("Pause---[click] ")
print("Restart-[dblclick] ")

# Show
run_animation()
plt.show()
