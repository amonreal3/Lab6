"""
Adrian Monreal
Lab 6
CS2302
"""
import dsf
import matplotlib.pyplot as plt
import numpy as np
import random

"""
# Starting point for program to build and draw a maze
# Modify program using disjoint set forest to ensure there is exactly one
# simple path joining any two cells
# Programmed by Olac Fuentes
"""




def draw_maze(walls,maze_rows,maze_cols,cell_nums=False):
    fig, ax = plt.subplots()
    for w in walls:
        if w[1]-w[0] ==1: #vertical wall
            x0 = (w[1]%maze_cols)
            x1 = x0
            y0 = (w[1]//maze_cols)
            y1 = y0+1
        else:#horizontal wall
            x0 = (w[0]%maze_cols)
            x1 = x0+1
            y0 = (w[1]//maze_cols)
            y1 = y0
        ax.plot([x0,x1],[y0,y1],linewidth=1,color='k')
    sx = maze_cols
    sy = maze_rows
    ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0],linewidth=2,color='k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r*maze_cols
                ax.text((c+.5),(r+.5), str(cell), size=10,
                        ha="center", va="center")
    ax.axis('off')
    ax.set_aspect(1.0)
              #M          #n
def wall_list(maze_rows , maze_cols):
    # Creates a list with all the walls in the maze
    w =[]
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r*maze_cols
            if c!=maze_cols-1:
                w.append([cell,cell+1])
            if r!=maze_rows-1:
                w.append([cell,cell+maze_cols])
    return w
"""
While S has more than one set
choose a random wall from the list of walls that
the wall list function gives you
check to see if they belong to the same set
if they do not union the 2 sets
if they do belong to the same set dont do anything
then pop that wall from the wall list
"""
def dsfMaze(rows,columns,wallList):
    cells = rows * columns
    s = dsf.DisjointSetForest(cells)
    while dsf.NumSets(s)> 1:
        curr = random.randint(0,len(wallList)-1)
        wall = wallList[curr]
        if dsf.find(s,wall[0]) != dsf.find(s,wall[1]):
            dsf.union(s, wall[0], wall[1])
            wallList.pop(curr)






plt.close("all")
maze_rows = 10
maze_cols = 15


walls = wall_list(maze_rows,maze_cols)

draw_maze(walls,maze_rows,maze_cols,cell_nums=True)

dsfMaze(maze_rows,maze_cols,walls)
draw_maze(walls,maze_rows,maze_cols)
