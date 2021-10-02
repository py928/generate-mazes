

'''
email : python928@gmail.com
facebook : https://www.facebook.com/python928

'''
import random
import png
def maze(h,w):
  result = [ j for i in range(h) for j in ([0,0]*w+[0],[0,1]*w+[0]) ]+[[0,0]*w+[0]]
  points = [(i,j) for i in range(1,h*2+1,2) for j in range(1,w*2+1,2) ]
  i,j = random.choice(points)
  used = []
  while 1:
    if (i,j) in points:
      points.remove((i,j))
    d = [i for i in ((i+1,j,i+2,j),(i-1,j,i-2,j),(i,j+1,i,j+2),(i,j-1,i,j-2)) if i[-2:] in points]
    if not d:
      if not used:
        break
      i,j = used.pop(-1)
      continue
    x,y,i,j = random.choice(d)
    result[x][y] = 1
    used.append((i,j))
  return result
r = maze(35,25)
img = []
for i in r:
  row = []
  for j in i:
    row.extend([j]*10)
  img.extend([row]*10)

with open('maze.png', 'wb') as f:
  w = png.Writer(len(img[0]), len(img), bitdepth=1)
  w.write(f, img)
