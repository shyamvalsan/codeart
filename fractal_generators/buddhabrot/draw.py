from PIL import Image


HEIGHT = 1000


R_DATA = []
G_DATA = []
B_DATA = []


def map_to_scale(x, in_min, in_max, out_min, out_max):
    # returns int
    if(in_max == 0):
        return 0
    else:
        return (((x - in_min) * (out_max - out_min)) / (in_max - in_min)) + out_min


with open('r.txt') as f:
    for line in f:
        int_list = line.split(',')  # [int(i) for i in line.split(',')]
        for i in int_list:
            if(i != ''):
                R_DATA.append(int(i))


with open('g.txt') as f:
    for line in f:
        int_list = line.split(',')  # [int(i) for i in line.split(',')]
        for i in int_list:
            if(i != ''):
                G_DATA.append(int(i))


with open('b.txt') as f:
    for line in f:
        int_list = line.split(',')  # [int(i) for i in line.split(',')]
        for i in int_list:
            if(i != ''):
                B_DATA.append(int(i))


maxR = max(R_DATA)
maxG = max(G_DATA)
maxB = max(B_DATA)

R_byte = [map_to_scale(i, 0, maxR, 0, 255) for i in R_DATA]
G_byte = [map_to_scale(i, 0, maxG, 0, 255) for i in G_DATA]
B_byte = [map_to_scale(i, 0, maxB, 0, 255) for i in B_DATA]

pil_byte = [(R_byte[i], G_byte[i], B_byte[i]) for i in xrange(HEIGHT * HEIGHT)]

img = Image.new('RGB', (HEIGHT, HEIGHT))

img.putdata(pil_byte)

img.save('buddha.png')
