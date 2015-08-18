from tealight.logo import move, turn
def square(edges, size):
  angle = 360.0 / edges
    for i in range(0,5):
      for i in range(0, edges):
          move(size)
          turn(angle)
      turn(angle)


square(4,100)