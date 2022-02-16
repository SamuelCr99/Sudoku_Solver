import math
import pygame

DIM = 900
WIN = pygame.display.set_mode((DIM, DIM))

#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE  = (0, 50, 255)

pygame.font.init()

iterations = 0

map3 = [[0,7,0,0,2,0,0,4,6],
       [0,6,0,0,0,0,8,9,0],
       [2,0,0,8,0,0,7,1,5],
       [0,8,4,0,9,7,0,0,0],
       [7,1,0,0,0,0,0,5,9],
       [0,0,0,1,3,0,4,8,0],
       [6,9,7,0,0,2,0,0,8],
       [0,5,8,0,0,0,0,6,0],
       [4,3,0,0,8,0,0,7,0]]

map3 = [[0, 0, 6, 3, 0, 7, 0, 0, 0],
       [0, 0, 4, 0, 0, 0, 0, 0, 5],
       [1, 0, 0, 0, 0, 6, 0, 8, 2],
       [2, 0, 5, 0, 3, 0, 1, 0, 6],
       [0, 0, 0, 2, 0, 0, 3, 0, 0],
       [9, 0, 0, 0, 7, 0, 0, 0, 4],
       [0, 5, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 8, 1, 0, 9, 0, 4, 0]]

map = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 3, 6, 0, 0, 0, 0, 0],
       [0, 7, 0, 0, 9, 0, 2, 0, 0],
       [0, 5, 0, 0, 0, 7, 0, 0, 0],
       [0, 0, 0, 0, 4, 5, 7, 0, 0],
       [0, 0, 0, 1, 0, 0, 0, 3, 0],
       [0, 0, 1, 0, 0, 0, 0, 6, 8],
       [0, 0, 8, 5, 0, 0, 0, 1, 0],
       [0, 9, 0, 0, 0, 0, 4, 0, 0]]

FONT_SIZE = 70
PHASE_FONT = pygame.font.SysFont('ariel', FONT_SIZE)


def get_valid_numbers(row, col):
    invalid_number = []
    for i in range(9): #Gets all values from row
        num = map[i][col]
        invalid_number.append(num)
    for i in range(9):
        num = map[row][i]
        invalid_number.append(num)

    row_quad = math.floor(row / 3)*3 #Gets which quadrant we are in 
    col_quad = math.floor(col / 3)*3 # And then sets a good coordinate  



    for i in range(0,3):
        for k in range(0,3):
            num = map[row_quad+i][col_quad+k]
            invalid_number.append(num)

    valid_number = [] 
    for i in range(1,10):
        if not(i in invalid_number):
            valid_number.append(i)
    
    return valid_number



def solve(val):
    if(check_done()): #Checks if we are done
        global iterations
        print(iterations)
        while(1):
            check_quit()
    row =  math.floor(val/9) #Calculates the row based on which value we are currently on
    col = val - row*9  # Calculates the col based on which value we are currently on
    if(map[row][col] != 0): 
        solve(val+1)
    else:
        valid = get_valid_numbers(row, col)
        for i in range (len(valid)):
            map[row][col] = valid[i]
            iterations += 1
            draw_square(row,col)
            solve(val+1)
            map[row][col] = 0 #Resets the value
            remove_square(row, col)
    if (val == 0):
        print("No solution!")

def print_map(): #Function for better printing the puzzle
    for i in range (9):
        print(map[i])

def check_done(): #Checks if we are done by making sure no square is set to 0
    for i in range(9):
        for k in range(9):
            if map[i][k] == 0:
                return False
    return True

def check_quit():
    for event in pygame.event.get(): #Checks if we are trying to quit
        if event.type == pygame.QUIT:
            quit()    

def draw_square(row,col):
    num = map[row][col]
    num_str = str(num)
    if(num_str == "0"):
        num_str = " "
    font = PHASE_FONT.render(num_str, 1, BLUE)
    WIN.blit(font, (col*100+40, row*100 + 30))
    pygame.display.update()

def remove_square(row,col):
    block = pygame.Rect(col*100+10, row*100+10,80,80)
    pygame.draw.rect(WIN, WHITE, block)
    pygame.display.update()



def draw_initial_map():
    WIN.fill(WHITE)
    for i in range(1, 9): #Draws all the vertical and horizontal lines
        line_thickness = 2
        if(i % 3 == 0):
            line_thickness = 8
        line_y = pygame.Rect(i*100, 0, line_thickness, DIM)
        pygame.draw.rect(WIN, BLACK, line_y)

        line_x = pygame.Rect(0, i * 100, DIM, line_thickness)
        pygame.draw.rect(WIN, BLACK, line_x)

    for row in range(9):
        for col in range(9):
            num = map[col][row]
            num_str = str(num)
            if num_str == "0": #Removes our zeros
                num_str = ""
            font = PHASE_FONT.render(num_str, 1, BLACK)
            WIN.blit(font, (row*100+40, col*100 + 30))    
    pygame.display.update()







draw_initial_map()
solve(0)