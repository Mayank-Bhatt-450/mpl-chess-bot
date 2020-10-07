from PIL import Image
import PIL
'''
imgs = Image.open('spot.png')
img=imgs.load()
k=[(545, 277), (559, 277), (558, 284), (546, 284), (543, 283), (547, 287), (552, 268), (544, 277), (552, 273), (540, 276), (547, 282), (559, 282), (547, 283), (559, 283)]

for i in k:
    imgs.putpixel(i,(0, 0, 0))#img[i[0],i[1]]=0
imgs.save('test.png')

'''
from PIL import Image

# PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
img = Image.new( 'RGB', (1440,900),(255,255,255)) # create a new black image
pixels = img.load() # create the pixel map
k=[(600, 377) ,(592, 372), (600, 368) ,(588, 371), (607, 372)]

for i in range(img.size[0]):    # for every col:
    for j in range(img.size[1]):    # For every row
        if (i,j) in k:
            pixels[i,j] = (0, 0,0) 

#img.show()
img.save('test.png')
