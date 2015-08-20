from tealight.art import (color, line, spot, circle, box, image, text, background)
import random
from random import randint
x=0
for j in range(0,10):
  for i in range(0,10):
    x=+1
    x=box(i*50,j*50,40,40)
    