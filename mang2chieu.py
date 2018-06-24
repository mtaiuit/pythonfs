import os
import sys
import string
map =  [[0, 0, 0, 0],
        [2, 0, 1, 0],
        [0, 1, 0, 0],
        [1, 0, 2, 0]]

lenmap=len(map)

for x in range(0,lenmap):
    for y in range(0,lenmap):
        if map[x][y]==2:
            print(x,y)