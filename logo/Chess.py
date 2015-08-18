from tealight.logo import move, turn
def square(edges, size):
  angle = 360.0 / edges
  for i in range(0,8):
    for i in range(0, edges):
      move(size)
      turn(angle)
    move(size)
  turn(angle)
  for i in range(0,2):
    for i in range(0, edges):
      move(size)
      turn(angle)
    move(size)
square(4,50)