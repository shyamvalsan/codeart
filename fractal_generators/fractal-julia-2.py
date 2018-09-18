#!/usr/bin/env python
# 020211 Raoul Meuldijk
# From http://oak.kcsd.k12.pa.us/~projects/fractal/what2.html :
# f(n) = f(n) * f(n) + c or f(n)^2 + c
# f(n) = f(2 + 1i) =
# (2 + 1i)(2 + 1i) + (1 + 1i) =
# 2*2 + 2i + 2i + i^2 + 1 + 1i =
# 5 + 5i + -1 = .............remember i^2 = -1 => 4 + 5i
# Run function again with f(4 + 5i) etc..
# https://raoulm.home.xs4all.nl/fractals/Fractals/Fractals.html
# Interesting values to play around with:
# c, maxiter, windowWidth & windowHeight, and, to a lesser extent, xl, xh, yl, yh.

def julia(a, b, e, f):
	""" One run of the Julia function, returns new a and b.
	
	f(n) = f(n)^2 + c
	f(n) = f(a + bi)
	c = e + fi
	"""
	ii = -1	# i-squared
	an=0.0	# new a and b
	bn=0.0	# needed so bn = ... can be done.
	an = a*a + b*b*ii + e
	bn = a*b + a*b + f
	a=an
	b=bn
	return a, b

def iterate(a, b, e, f):
	""" Loop the Julia-function until a boundary condition.
	
	Returns the number of iterations needed to reach a boundary condition.
	"""
	xl=-10.0		# boundaries: orbit should stay within this range
	xh=10.0
	yl=-10.0
	yh=10.0

	maxiter = 100	# boundary: maximum number of iterations

	iterations = 0		# iteration 0 is at the starting values for a and b
	boundary = False	# a or b outside range or too many iterations set boundary to True
	while not boundary:
		#print iterations, a, b, boundary
		a, b = julia(a, b, e, f)
		iterations += 1
		if a < xl:
			boundary = True
		elif a > xh:
			boundary = True
		elif b < yl:
			boundary = True
		elif b > yh:
			boundary = True
			
		if iterations >= maxiter:
			boundary = True

	return iterations

# Set up variables and lists.
c=(0.4, 0.2)		# c = 0.4 + 0.2i
#c=(1.0, 1.0)

amin = -2.0			# axis ranges
amax = 2.0			# a horizontal real
bmin = -2.0			# b vertical imaginary
bmax = 2.0

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

# Do the math.
# Fill a list of (a , b, iterations) from top left to bottom right in the window.
present_iterations = set()	# Which numbers of iterations are present, is useful for deciding the colour scale.
for j in range(len(b_axis)):
	k = len(b_axis) - (j+1)
	for i in range(len(a_axis)):
		iters = iterate(a_axis[i],b_axis[k],c[0],c[1])
		#print '(%2.1f)' % a_axis[i], '(%2.1f)' % b_axis[k] , iters
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
		#print 'drawing line y=',y
		numberOfIters = point[2]

	a_previous = a_current
	aDot = [x, y, x, y]
	# Hier wat experimenten met colour verdelen
	#colour = (numberOfIters-(lowest_iteration+1)) * colourStep	# nice if iters 17 to 48
	colour = log(numberOfIters, iter_range) * 255		# nice if lowest_iteration = 2; log(x, base)

	colour = int(colour)
	if colour > 255:
		colour = 255
	#colour = 255 - colour	#	invert picture
	tk_rgb = "#%02x%02x%02x" % (128, colour, colour)
	#tk_rgb = "#%02x%02x%02x" % (colour, colour, colour)		# grey scale, lighter means more iterations
	pixel = C.create_rectangle(aDot, fill=tk_rgb, outline="darkblue", width=0)


C.pack()
top.mainloop()
