import os
import sys

def matrixElementsSum(matrix):
    ray=len(matrix)
    dev=len(matrix[0])
    sum=0
    for i in range(0,ray):
        for j in range(0,dev):
            if i != 0 and matrix[i][j] != 0 :
                
                check=True
                for x in range(0,i):
                    print matrix[x][j]
                    if int(matrix[x][j]) == 0:
                        print matrix[x][j]
                        check=False
                if check:
                    sum=sum+int(matrix[i][j])
            else:
                sum=sum+int(matrix[i][j])
    return sum

matrix = [[0, 1, 1, 2], 
          [0, 5, 0, 0], 
          [2, 0, 3, 3]]

print matrixElementsSum(matrix)