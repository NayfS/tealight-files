from tealight.logo import move, turn

def polygon(edges, size):
  angle = 360.0 / edges
  for i in range(0, edges):
    move(size)
    turn(angle)
    


def board(edges, size):
  angle = 360/ edges
  decoration = size / 1
  for i in range(0, edges):
    move(size)
    polygon(4,100)
    turn(angle)

turn(-90)
board(12,75)
