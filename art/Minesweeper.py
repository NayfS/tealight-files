from tealight.art import (color, line, spot, circle, box, image, text, background)
import random
from random import randint

for j in range(0,10):
  for i in range(0,10):
    x=box(i*50,j*50,40,40)
    
x=random.randrange(15,100,5)
print(x)