from tealight.logo import move, turn
def square(edges, size):
j=0
  angle = 360.0 / edges
  for i in range(0,16):
    for i in range(0, edges):
        move(size)
        turn(angle)
    turn(j+90)


square(4,100)