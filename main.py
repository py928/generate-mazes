

'''
email : python928@gmail.com
facebook : https://www.facebook.com/python928

'''

import random,png
def maze(h,w):
  h = h*2+1
  w = w*2+1
  points = [(i,j) for i in range(1,h-1) for j in range(1,w-1) if i%2 and j%2]
  matrix = [[0 for i in range(w)]for i in range(h)]
  i,j=random.choice(points)
  points.remove((i,j))
  used = []
  while 1:
    matrix[i][j] = 1
    for x,y,i,j in {(i+1,j,i+2,j),(i-1,j,i-2,j),(i,j+1,i,j+2),(i,j-1,i,j-2)}:
      if (i,j) in points:
        points.remove((i,j))
        break
    else:
      i,j = used.pop(random.randint(0,len(used)-1))
      if not used:
        break
      continue
    used.append((i,j))
    matrix[x][y] = 1
  img = []
  for values in matrix:
    row = []
    for value in values:
      row.extend([value]*10)
    img.extend([row]*10)
  with open('maze.png', 'wb') as f:
    w = png.Writer(len(img[0]), len(img), bitdepth=1)
    w.write(f, img)
maze(35,30)
