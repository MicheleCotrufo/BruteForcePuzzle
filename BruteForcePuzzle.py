'''
Code to solve this puzzle https://www.enchambered.com/puzzles/puzzle_4_mystery_box/game/
by brute-force. 
The script calculates all possible combination achievable with 1 moves, 2 moves, 3 moves, etc.
and stops when it finds a sequence of moves which creates the desired matrix
 '''
import numpy as np
import copy

def rotate(M,n):
    ''' Given a 3x3 matrix, it rotates by 90 degrees clockwise the 2x2 matrix
    identified by n. n is an index which can have the values 1,2,3, o 4.
    n=1 -> top left submatrix
    n=2 -> top right submatrix
    n=3 -> bottom left submatrix
    n=4 -> bottom right submatrix
    '''
    M = copy.deepcopy(M)
    if n == 1:
        ix = (slice(0,2),slice(0,2))
    if n == 2:
        ix = (slice(0,2),slice(1,3))
    if n == 3:
        ix = (slice(1,3),slice(0,2))
    if n == 4:
        ix = (slice(1,3),slice(1,3))
    m = M[ix]
    m = np.flip(np.transpose(m) ,axis=1) #This effectively rotates the 2x2 matrix clockwise
    M[ix] = m
    return M

def generate_next_move(M_List,history_list):
    '''
    Given a list of 3x3 matrices it generates a new list of matrices by performing 
    all possible sub-matrix rotations on all matrices.
    Each input matrix is also characterized by an history of rotations,
    contained in the corresponding element of history_list.
    A new list of histories is also generated.
    '''
    M_List_New = []
    history_list_New = []
    for j,M in enumerate(M_List): #sweep over all the input matrices
        for p in [1,2,3,4]: #sweep over all the moves
        
            #if the last 3 moves of the history of a given matrix are identical 
            #(e.g. three consecutive rotations of the submatrix 1) we avoid repeating 
            #that same move a fourth time, since that will correspond to an 
            #identity operation and will generate a matrix that 
            #has been already considered in the past.
            if len(history_list[j])>2 and history_list[j][-3:]==str(p)*3:
                continue
            
            #Generate the new matrix by rotating the p-th submatrix
            Mp = rotate(M,p)
            #Update the history
            h = history_list[j] + str(p)
            
            M_List_New.append(Mp)
            history_list_New.append(h)
            
            if np.array_equal(Mp,M_target):
                return Mp,h

    return M_List_New, history_list_New

M_start = np.array([ [7,6,5],[8,4,9],[3,2,1]])
M_target = np.array([ [1,2,3],[4,5,6],[7,8,9]])
N=10 #Maximum number of moves that will be checked
M_List = [M_start]
history_list = ['']

for i in range(N):
    print("Checking all matrices that can be generated with " + str(i+1) + " moves...")
    M_List, history_list = generate_next_move(M_List,history_list)
    if isinstance(M_List,list):
        print("No solution was found.")
    else:
        print("Found a solution:")
        print(history_list)
    
    
