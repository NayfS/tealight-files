from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)


while True:
  if right_side()=='fruit':
    turn(1)
    move()
  elif left_side()=='fruit':
    turn(1)
    move()
  elif look()=='fruit':
    move()
  else:
    turn(1)
    move()
    