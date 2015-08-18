from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)



if right_side()=='fruit':
    turn(1)
    while look()=='friut':
      move()
  
  elif left_side()=='fruit':
      turn(2)
      while look()=='friut':
        move()

