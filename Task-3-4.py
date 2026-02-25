from robot import *

nMovesLeft = 0
nMovesRight = 0

while(is_free_left()):
    if(is_cell_not_painted() and nMovesLeft != nMovesRight):
        paint()
    move_left()
    nMovesLeft += 1
paint()
    
while(is_free_right()):
    if(is_cell_not_painted() and nMovesLeft != nMovesRight):
        paint()
    move_right()
    nMovesRight += 1
paint()

while nMovesRight > nMovesLeft:
    move_left()
    nMovesRight -= 1