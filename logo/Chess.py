from tealight.logo import move, turn
def square(edges, size):
  angle = 0
  for i in range(0,16):
    for i in range(0, edges):
        move(size)
        turn(angle)
    turn(angle+90)


square(4,100)