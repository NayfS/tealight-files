from tealight.art import (color, line, spot, circle, box, image, text, background)
import random
from random import randint
import github.fourthdwarflord.art.Minesweeper.py

list=[]

for i in range (0, 100):
  list.append(0)


for j in range(0,10):
  for i in range(0,10):
    box(i*50,j*50,40,40)
    
for i in range (0,15):
  x=random.randrange(1,100,1)
  y=random.randrange(1,100,1)
  setbox(list, x, y, 1)

print list