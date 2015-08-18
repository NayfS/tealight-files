from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

while look()=='friut':
  move()
if right_side()=='fruit':
  turn(1)
  move()
if left_side()=='fruit':
  turn(2)
  move()
