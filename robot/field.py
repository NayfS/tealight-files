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
  elif left_side()=='fruit':
    turn(2)
    move()
  elif look()=='fruit':
    move()
  if i>3:
    i=0
    for j in (0,5):
      move
  else:
    turn(1)
    move()
    i=i+1
    