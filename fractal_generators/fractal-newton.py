# Newton fractals
# FB - 201003291
from PIL import Image
imgx = 1920 
imgy = 1080
image = Image.new("RGB", (imgx, imgy))

# drawing area
xa = -1.0
xb = 1.0
ya = -1.0
yb = 1.0

maxIt = 25 # max iterations allowed
h = 1e-6 # step size for numerical derivative
eps = 1e-2 # max error allowed

# put any complex function here to generate a fractal for it!
def f(z):
    return z * z * z * z   - 1

# draw the fractal
for y in range(imgy):
    zy = y * (yb - ya) / (imgy - 1) + ya
    for x in range(imgx):
        zx = x * (xb - xa) / (imgx - 1) + xa
        z = complex(zx, zy)
        for i in range(maxIt):
            # complex numerical derivative
            dz = (f(z + complex(h, h)) - f(z)) / complex(h, h)
            z0 = z - f(z) / dz # Newton iteration
            if abs(z0 - z) < eps: # stop when close enough to any root
                break
            z = z0
        image.putpixel((x, y), (i % 4 * 64, i % 8 * 32, i % 16 * 16))

image.save("../../input/fractals/newtonFr.png", "PNG")
