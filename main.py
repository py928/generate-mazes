
'''
email : python928@gmail.com
facebook : https://www.facebook.com/python928

'''
import random
import png
def maze(h,w):
  result = [ j for i in range(h) for j in ([1,1]*w+[1],[1,0]*w+[1]) ]+[[1,1]*w+[1]]
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
    result[x][y] = 0
    used.append((i,j))
  return result
r = maze(45,35)
img = []
n = 20
for i in r:
  row = []
  for j in i:
    row.extend([j]*n)
  img.extend([row]*n)
height = len(img)
width = len(img[0])
w = png.Writer(width, height, bitdepth=1)
f = open('maze.png', 'wb')
w.write(f, img)
