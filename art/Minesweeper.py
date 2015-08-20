from tealight.art import (color, line, spot, circle, box, image, text, background)
import random
from random import randint
list=[]

for j in range(0,10):
  for i in range(0,10):
    box(i*50,j*50,40,40)
    
for i in range (0,15):
  x=random.randrange(1,100,1)
  y=random.randrange(1,100,1)
  list.append((x,y))

print list