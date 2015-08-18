from tealight.logo import move, turn

def polygon(edges, size):
  angle = 360.0 / edges
  for i in range(0, edges):
    move(size)
    turn(angle)
    
polygon(4,100)

def board(edges, size):
  angle = 360/ edges
  decoration = size / 1
  for i in range(0, edges):
    move(size)
    square(decoration)
    turn(angle)

turn(-90)
waterwheel(12,75)
