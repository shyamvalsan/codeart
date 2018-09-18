#!/usr/bin/env python
# 140211 Raoul Meuldijk
# http://en.wikipedia.org/wiki/Mandelbrot_set
# https://raoulm.home.xs4all.nl/fractals/Fractals/Fractals.html

def mandel(x0, y0):
	""" Iterate the Mandelbrot function, returns the number of
	iterations until x^2 + y^2 > 4 or 200 iterations.
	"""
	x = 0
	y = 0
	
	iteration = 0
	max_iteration = 200
	
	while ( x*x + y*y <= (2*2) and iteration < max_iteration ):
		xtemp = x*x - y*y + x0
		y = 2*x*y + y0
		x = xtemp
		iteration += 1
	
	if (iteration == max_iteration):
		iterations = max_iteration
	else:
		iterations = iteration
	
	return(iterations)

# Set up variables and lists.
amin = -2.25			# axis ranges:
amax = 1.25				# a horizontal, real part
bmin = -1.75			# b vertical, imaginary part
bmax = 1.75

windowWidth = 300	# in pixels
windowHeight = 300

iterlist=[]			# list of coordinates (a,bi) and number of iters on that point
tup=()				# tuple with (a, bi, iterations) for extending iterList
a_axis = []			# points on the a-axis
b_axis = []			# points on the bi-axis

# project range on window
# a_axis is list of coordinates -2.0 .. 2.0 divided over 300 pixels
step_a = (amax - amin) / windowWidth		# step size of coordinates between each pixel
step_b = (bmax - bmin) / windowHeight

u = amin
while u < amax:
	a_axis = a_axis + [u]
	u += step_a
u = bmin
while u < bmax:
	b_axis = b_axis + [u]
	u += step_b

print 'Mandelbrot with python, February 2011.'

# Do the math.
# Fill a list of (a , b, iterations) from top left to bottom right in the window.
present_iterations = set()	# Which numbers of iterations are present, is useful for deciding the colour scale.
for j in range(len(b_axis)):
	k = len(b_axis) - (j+1)
	for i in range(len(a_axis)):
		iters = mandel(a_axis[i],b_axis[k])
		tup=()
		tup = (a_axis[i],b_axis[k],iters)		# a, b, iters
		iterlist.append(tup)
		if iters not in present_iterations:
			present_iterations.add(iters)
			
highest_iteration = max(present_iterations)		# highest and lowest iteration numbers
lowest_iteration = min(present_iterations)
colourStep = int(255/(highest_iteration-lowest_iteration))		# divide 255 colours linearly over the found iteration range
iter_range = (highest_iteration-lowest_iteration)

# Draw picture.
from math import *				# only used for log() in colour scaling
from Tkinter import *			# Python's access to the Tcl/Tk GUI

top = Tk()
C = Canvas(top, bg="yellow", bd=0, height=windowHeight, width=windowWidth)

# Iterlist is one-dimensional, so the end of each line of pixels needs to be found.
a_previous = amin		# To keep track of the end of a pixel line in the window
a_current = 0

# Tk Canvas coordinates have a strangely big offset.
x=2		# x is 1 lower than offset here, because first loop step adds 1
y=3

# point[0]	is a
# point[1]	is bi
# point[2]	is number of iterations

# Loop iterlist
for point in iterlist:
	a_current = point[0]
	if a_current >= a_previous:	# if a_current is getting bigger, still on same line
		x += 1
		numberOfIters = point[2]
	else:						# else, new line starts
		x = 3
		y += 1
		numberOfIters = point[2]

	a_previous = a_current
	aDot = [x, y, x, y]
	# Some experiments in distributing colours.
	#colour = (numberOfIters-(lowest_iteration+1)) * colourStep	# nice if iters 17 to 48
	colour = log(numberOfIters, iter_range) * 255		# nice if lowest_iteration = 2; log(x, base)

	colour = int(colour)
	if colour > 255:
		colour = 255
	#colour = 255 - colour	#	invert picture
	tk_rgb = "#%02x%02x%02x" % (128, colour, colour)
	#tk_rgb = "#%02x%02x%02x" % (colour, colour, colour)		# grey scale, lighter means more iterations
	pixel = C.create_rectangle(aDot, fill=tk_rgb, outline="darkblue", width=0)

print 'Iteration numbers present in the picture: ', present_iterations

C.pack()
top.mainloop()
