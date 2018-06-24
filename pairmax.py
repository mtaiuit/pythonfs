import sys
import os

inputArray = [3, 6, -2, -5, 7, 3]
def adjacentElementsProduct(inputArray):
    max=0
    for x in range(0,len(inputArray)-1):
        a=inputArray[x]*inputArray[x+1]
        if a>max:
            max=a
    return max

print(adjacentElementsProduct(inputArray))