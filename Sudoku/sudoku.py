board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(board):   
      
    for i in range(len(board)): 
        if i % 3 == 0 and i != 0: 
            print('- - - - - - - - - - -')
        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0: 
                print('| ', end='')
            print(str(board[i][j]) + ' ', end='')
            if j == len(board[i]) - 1: 
                print()
            
#print_board(board)

def valid(number, position, board): 
    
    for i in range(len(board[position[1]])): # check row 
        if board[position[0]][i] == number and i != position[1]: 
            return False
        
    for i in range(len(board)): # check column
        if board[i][position[1]] == number and i != position[0]: 
            return False 
        
    for i in range((position[0]//3) * 3, ((position[0]//3)*3) + 3): # check box
        for j in range((position[1]//3)*3, ((position[1]//3)*3) + 3): 
            if board[i][j] == number and i != position[0] and j != position[1]: 
                return False
            
    return True 
            
def find_empty(board): 
    
    for i in range(len(board)):
        for j in range(len(board[i])): 
            if board[i][j] == 0: 
                return (i, j)
    
    return None

def solve(board): 
    
    find = find_empty(board)
    
    if not find:
        return True
    else:
        row,col = find 
    
    for i in range(1,10): 
        if valid(i, (row,col), board): 
            board[row][col] = i
            if solve(board): 
                return True  
                   
        board[row][col] = 0
        
    return False
      
solve(board)
print_board(board)

        