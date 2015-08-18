from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

i=0
j=1
while True:
  if right_side()=='fruit':
    turn(1)
    move()
    i=0
  elif left_side()=='fruit':
    turn(2)
    move()
    i=0
  elif look()=='fruit':
    move()
    i=0
  if i>3:
    i=0
    for j in (0,5):
      move
  else:
    turn(1)
    move()
    i=i+1
    