from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

while True:
  i=0
  if right_side()=='fruit':
    turn(1)
    while look()=='fruit':
      move()
  elif left_side()=='fruit':
    turn(2)
    while look()=='fruit':
      move()
  elif look()=='fruit':
    move()


  else:
    while i==0:
      turn(1)
      move()
      if look()=='fruit':
        i=1
    