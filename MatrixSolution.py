# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 22:34:57 2021

@author: lorie
"""
def solve_matrix(matrix):
    """ returns a solved matrix given a matrix that has a solution
        as well as rows must be in proper form (for now)
    """
    passes = len(matrix) - 1 #predetermined number of passes
    
    new_matrix = echelon(matrix) 
    sub_matrix = new_matrix #initialize the sub matrix
    for x in range(passes): #cycle through passes
         sub_matrix = create_sub(sub_matrix, 0) #create the next matrix
         echelon(sub_matrix) #put sub matrix in echelon form
         combine_matrices(new_matrix, sub_matrix, 1) #replace the section of the full matrix with the appropriate sub matrix
    
    sub_matrix = reduce_echelon(new_matrix, len(new_matrix) - 1)
    
    for x in range(passes):
        sub_matrix = create_sub(sub_matrix, 1)
        reduce_echelon(sub_matrix, len(sub_matrix) - x - 1)
        combine_matrices(new_matrix, sub_matrix, 0)
                     
    
    return new_matrix #return solved matrix
        

def echelon(matrix):
    """Returns the given matrix in echelon form (or at least does row reduction)
    """
    
    #Switches rows if the first one is already in a reduced form and second is not
    for z in range(0, len(matrix) - 1):
        if (matrix[z][0] == 0) and (matrix[z + 1][0] != 0):
            matrix[z], matrix[z + 1] = matrix[z + 1], matrix[z]
          
    for y in range(1, len(matrix)):
        
        if matrix[0][0] == 0:
            continue
        multiplier = matrix[y][0] / matrix[0][0] #multiplier to make the entry in the same column but the row below 0
    
        for x in range(0, len(matrix[0])):
            matrix[y][x] -= matrix[0][x] * multiplier #makes first entry of row 0, and changes the other columns appropriately
    return matrix
    

def create_sub(initial, corner):
    """Returns a sub matrix of dimensions n - 1 x m - 1 from the given matrix
        sub matrix is created by removing first row and columns if corner is 0
        sub matrix is created by removing last row if corner is 1. Assuming to reduce echelon form here.
    """
    sub = []
    
    if corner == 0:
        for x in range(1, len(initial)):
            row = []
            
            for y in range(1, len(initial[x])):
                
                row.append(initial[x][y])
            sub.append(row)
            
    elif corner == 1:
        for x in range(len(initial) - 1):
            sub.append(initial[x])
        
    return sub

def combine_matrices(initial, sub, corner):
    """Returns a matrix with the sub matrix substituted in the main matrix,
        assuming that the bottom right corners match places
        0 corner indicates top left corners match
        1 corner indicates bottom right corners match
    """
    
    columns = len(sub[0])
    rows = len(sub)
    
    
    if corner == 1:     
        for x in range(0, rows):
            for y in range(0, columns):
                #Cycle from the bottom right to the bottom left, then from the bottom row to the top row
                #Using the sub matrix positions
                initial[len(initial) - x - 1][len(initial[x]) - y - 1] = sub[len(sub) - x - 1][len(sub[x]) - y - 1]
    
    elif corner == 0:
        for x in range(0, rows):
            for y in range(0, columns):
                initial[x][y] = sub[x][y]
    
        
        
    return initial

def reduce_echelon(matrix, leading_index):
    """Returns a reduced echelon form matrix, given an echelon matrix
    """
    #for w in range(0, len(matrix[0]) - 1):
        
        #Here down works
    
    for x in range(len(matrix) - 1, 0, -1):
        for y in range(len(matrix[x]) - 2, 0, -1):
            
            if matrix[len(matrix) - 1][leading_index] == 0:
                continue
            
            multiplier = matrix[x - 1][leading_index] / matrix[len(matrix) - 1][leading_index] 
             
            for z in range(len(matrix[0]) - 1, -1, -1):
                
                matrix[x - 1][z] -= matrix[len(matrix) - 1][z] * multiplier
    
    
    return matrix

def find_last_leading(matrix):
    for x in range(len(matrix) - 1):
        if x != 0:
            return x
    
    return 1
        
    return matrix
    
my_m = [[1, 4, 8, 15], [2, 12, 20, 38], [0, 1, 1, 2], [-2, -9, -17, -32]]
your_m = [[0,0],[0,0]]

test_reduce = [[1, 1, 2, 1], [0, 1, 1, 1], [0, 0, 1, 1]]
print(solve_matrix(my_m))