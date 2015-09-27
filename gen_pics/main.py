from PIL import Image
import random, math

width = 255
height = 255

img = Image.new( 'RGB', (width,height),"black") # create a new black image
pixels = img.load() # create the pixel map


def distance(p1,p2):
	x_diff = p2[0] - p1[0]
	y_diff = p2[1] - p1[1]
	return math.sqrt(x_diff**2 + y_diff**2)

def avg(l):
    return sum(l)/len(l)


positions = [(0,0),(0,height),(width,0),(width,height)]
colors = [[1, 0, 0.5],[0, 1, 0.5],[1, 0.5, 1],[0.5, 0, 0.5]]
colors = [[random.random() for i in xrange(3)] for j in xrange(4)]

for x in range(img.size[0]):    # for every pixel:
    for y in range(img.size[1]):

        '''
        distances = [distance((x,y),k) for k in positions]
        distances = [d**3 for d in distances]
  
        normalized = [i/sum(distances) for i in distances]
        #print normalized

        final_color = [0,0,0]
        for n in xrange(4):
            for c in xrange(3):
                final_color[c] += colors[n][c] * normalized[n]

        final_color = tuple([int(i*255) for i in final_color])
        pixels[x,y] = final_color # set the colour accordingly
        '''

        this_color = [127*math.sin(x/127.0)+127,127*math.cos(y/127.0)+127,127*math.sin(y/127.0)+127]

        pixels[x,y] = tuple([int(i) for i in this_color])

img.show()
img.save('test.png')


