import math

map = [[0,7,0,0,2,0,0,4,6],
       [0,6,0,0,0,0,8,9,0],
       [2,0,0,8,0,0,7,1,5],
       [0,8,4,0,9,7,0,0,0],
       [7,1,0,0,0,0,0,5,9],
       [0,0,0,1,3,0,4,8,0],
       [6,9,7,0,0,2,0,0,8],
       [0,5,8,0,0,0,0,6,0],
       [4,3,0,0,8,0,0,7,0]]

def check_legal_line(row, col):
    invalid_number = []
    for i in range(9): #Gets all values from row
        invalid_number.append(map[i][col])
    for i in range(9):
        invalid_number.append(map[row][i])

    row_quad = math.floor(row / 3)*3 #Gets which quadrant we are in 
    col_quad = math.floor(col / 3)*3 # And then sets a good coordinate  



    for i in range(0,3):
        for k in range(0,3):
            invalid_number.append(map[row_quad+i][col_quad+k])

    valid_number = [] 
    for i in range(1,10):
        if not(i in invalid_number):
            valid_number.append(i)
    
    return valid_number

def solve(val):
    print(val)
    row = math.floor(val/9)
    col = val - row*9
    if(map[row][col] != 0):
        solve(val+1)
    else:
        valid = check_legal_line(row, col)
        for i in range (len(valid)):
            if(val > 81):
                print_nice()
                quit()
            map[row][col] = valid[i]
            solve(val+1)

def print_nice():
    for i in range (9):
        print(map[i])

def check_done():
    for i in range(9):
        for k in range(9):
            if map[i][k] == 0:
                return False
    return True

solve(0)
print_nice()