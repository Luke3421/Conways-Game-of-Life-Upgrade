#GROUP AND LUKE BEEN
from conway_assignment_two import Update
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation

import time
import sys

#Test code
#gridsize = 12


"""
timesteps = sys.argz[1]
gridsize = sys.argz[2]
gridsize = sys.argz[3]
state = sys.argz[4]
sim = sys.argz[5]
"""
 
timesteps = input("Enter timesteps for simulation: ")
gridsize = input("Enter size of grid: ")
gridsize = int(gridsize)
state = input("Enter state: ")
sim = input("Would you like to simulate: ")


rows = gridsize
col = gridsize 
grid = np.zeros((rows, col), dtype = bool)


########just in case

def aliveordead(n, countalive, countdead):
    """cols = n
    rows = n
    grid = np.zeros((rows, col), dtype = bool)
    grid = random(grid,n)
    updated_grid = np.zeros((rows, col), dtype = bool)
    for i in range(n-1):
        for j in range(n-1):
            curr = grid[i,j]
            if(i == 0 or i == cols - 1 or j == 0 or j == rows - 1):
                updated_grid[i-1,j-1] = grid[i,j]
            neighbors = countNeighbors(grid, i, j)
            curr = grid[i,j]
            if curr == False and neighbors == 3:
                updated_grid[i,j] = True
            elif curr == True and (neighbors < 2 or neighbors > 3):
                updated_grid[i,j] = False
            else:
                updated_grid[i,j] = curr
            if(grid[i,j]):
                countalive += 1
             
            
    countdead = (n*n) - countalive
    grid = np.zeros((rows, col), dtype = bool)
    #boardplot(updated_grid, gridsize)"""
    cols = n
    rows = n
    grid = [[False] * cols for r in range(rows)]
    
    grid = random(grid,n)
    updated_grid = [[False] * cols for r in range(rows)]
    for i in range(n-1):
        for j in range(n-1):
            curr = grid[i][j]
            if(i == 0 or i == cols - 1 or j == 0 or j == rows - 1):
                updated_grid[i][j] = grid[i][j]
            neighbors = countNeighbors(grid, i, j)
            curr = grid[i][j]
            if curr == False and neighbors == 3:
                updated_grid[i][j] = True
            elif curr == True and (neighbors < 2 or neighbors > 3):
                updated_grid[i][j] = False
            else:
                updated_grid[i][j] = curr
            if(grid[i][j]):
                countalive += 1
             
            
    countdead = (n*n) - countalive
    grid = [[False] * cols for r in range(rows)]
    return countdead, countalive    
            
def conway_assignment_three():
    gridsize = 1000
    alivecnt = 0
    deadcnt = 0
   
    cells=[]
    Time = []
    print("Times and cell count for conway_assignment 3")
    for i in range(0,5):
        start= time.time()
        aliveordead(gridsize, alivecnt, deadcnt)
        end = time.time()
        print("Time taken: " , end - start)
        gridsize += 250   
        Time.append((end-start))
        cells.append(aliveordead(gridsize, alivecnt, deadcnt))
    plt.figure(1)
    plt.title("Alive and Dead Cells")
    plt.plot(cells)
    plt.xlabel("Steps")
    plt.ylabel("Number of Cells")
    plt.legend(['Alive','Dead'])
   
    
    plt.figure(2)
    plt.title("Time to Plot")
    plt.plot(Time)
    plt.xlabel("Steps")
    plt.ylabel("Time (seconds)")
    
    plt.show()

            
def conway_assignment_two ():
    start = time.time()
    gridsize = 1000
    alivecnt = 0
    deadcnt = 0
   
    cells=[]
    Time = []
    print("Times and cell count for conway_assignment 2")
    for i in range(0,5):
        start= time.time()
        Update(gridsize, alivecnt, deadcnt)
        end = time.time()
        print("Time taken: " , end - start)
        gridsize += 250    
        Time.append((end-start))
        cells.append(Update(gridsize, alivecnt, deadcnt))
    plt.figure(3)
    plt.title("Alive and Dead Cells_Assignment two")
    plt.plot(cells)
    plt.xlabel("Steps")
    plt.ylabel("Number of Cells")
    plt.legend(['Alive','Dead'])
   
    
    plt.figure(4)
    plt.title("Time to Plot for Assignment two")
    plt.plot(Time)
    plt.xlabel("Steps")
    plt.ylabel("Time (seconds)")
    
    plt.show()



def countNeighbors(grid, x, y):
    check = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if(x-i < len(grid) and y-j < len(grid) and grid[(x-i),(y-j)] ):
                check += 1
    if(grid[x,y]):
        check -= 1

    return check

def update2(grid, n):
    cols = n
    rows = n
    updated_grid = np.zeros((rows, col), dtype = bool)
    for i in range(n-1):
        for j in range(n-1):
            curr = grid[i,j]
            if(i == 0 or i == cols - 1 or j == 0 or j == rows - 1):
                updated_grid[i,j] = grid[i,j]
            neighbors = countNeighbors(grid, i, j)
            curr = grid[i,j]
            if curr == False and neighbors == 3:
                updated_grid[i,j] = True
            elif curr == True and (neighbors < 2 or neighbors > 3):
                updated_grid[i,j] = False
            else:
                updated_grid[i,j] = curr
    grid = np.zeros((rows, col), dtype = bool)
    return updated_grid

def blinker (grid, n):
    mid = int(n / 2)
    grid[mid,mid]= True
    grid[mid-1, mid] = True
    grid[mid+1, mid]= True
    return grid

def random(grid, n):
    choice = [True, False]
    grid = np.random.choice(choice, size = (n,n))
    return grid

def glidergun(grid, n):
    mid = int(n / 2)

    grid[mid, mid] = True
    grid[mid+1, mid+2] = True
    grid[mid+2, mid+1] = True
    grid[mid+2, mid] = True
    grid[mid+3, mid] = True
    grid[mid+2, mid-1] = True
    grid[mid+1, mid-2] = True
    grid[mid-1, mid-3] = True
    grid[mid-2, mid-3] = True
    grid[mid-3, mid-2] = True
    grid[mid-4, mid-1] = True
    grid[mid-4, mid] = True
    grid[mid-4, mid+1] = True
    grid[mid-3, mid+2] = True
    grid[mid-2, mid+3] = True
    grid[mid-1, mid+3] = True

    grid[mid-13, mid] = True
    grid[mid-14, mid] = True
    grid[mid-14, mid+1] = True
    grid[mid-13, mid+1] = True

    grid[mid+6, mid+1] = True
    grid[mid+6, mid+2] = True
    grid[mid+6, mid+3] = True
    grid[mid+7, mid+1] = True
    grid[mid+7, mid+2] = True
    grid[mid+7, mid+3] = True
    grid[mid+8, mid] = True
    grid[mid+8, mid+4] = True
    grid[mid+10, mid] = True
    grid[mid+10, mid-1] = True
    grid[mid+10, mid+4] = True
    grid[mid+10, mid+5] = True

    grid[mid+20, mid+2] = True
    grid[mid+20, mid+3] = True
    grid[mid+21, mid+2] = True
    grid[mid+21, mid+3] = True
    return grid

def person(grid, n):
    
    
    mid = int(gridsize / 2)
    grid[mid,mid] = True
    grid[mid, mid+1] = True
    grid[mid+1, mid+2] = True
    grid[mid+1, mid+3] = True
    grid[mid+1, mid+4] = True
    grid[mid, mid+4] = True
    grid[mid-1, mid+4] = True
    grid[mid-1, mid+3] = True
    grid[mid-1, mid+2] = True
    grid[mid-1, mid] = True
    grid[mid-1, mid-3] = True
    grid[mid-1, mid-4] = True
    grid[mid-3, mid] = True
    grid[mid-2, mid-1] = True
    grid[mid+1, mid] = True
    grid[mid+1, mid-3] = True
    grid[mid+1, mid-4] = True
    grid[mid+3, mid-2] = True
    grid[mid+2, mid-1] = True
    grid[mid, mid-1] = True
    grid[mid, mid-2] = True
    return grid


if sim == 'yes':
    fig, ax = plt.subplots()
    life = [(x, y) for x in range(gridsize) for y in range(gridsize) if grid[x,y]]
    xs = [x for (x, _) in life]
    ys = [y for (_, y) in life]
    if state == 'random':
        grid = random(grid, gridsize)
    elif state == 'glider gun':
        grid = glidergun(grid, gridsize)
    elif state == 'blinker':
        grid = blinker(grid, gridsize)
    elif state == 'person':
        grid = person(grid, gridsize)
    sc = ax.scatter(xs, ys, marker = 'x')
    plt.xlim([0,gridsize])
    plt.ylim([0,gridsize])
    def animate(timesteps):
        global grid
        newgrid = update2(grid,gridsize)        
        grid = newgrid
        life = [(x, y) for x in range(gridsize) for y in range(gridsize) if grid[x,y]]
        xs = [x for (x, _) in life]
        ys = [y for (_, y) in life]
        news = [[xs[i],ys[i]] for i in range (len(xs))]
        sc.set_offsets(news)

    def dyngraph(grid, n, timesteps):

        ani = matplotlib.animation.FuncAnimation(fig, animate, 
                frames = 1000, interval=10, repeat = False) 
        plt.show()
        return ani

    ani = dyngraph(grid, gridsize, timesteps)
elif sim == 'no': 
    print("no similulation")
    conway_assignment_three()
    conway_assignment_two()
  
    

    
