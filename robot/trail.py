from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

while True:
  if right_side()=='none' && left_side()=='none':
    move()
    
  