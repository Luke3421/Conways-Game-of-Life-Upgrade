#GROUP AND LUKE BEEN
from conway_assignment_two import Update
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation
from numpy.lib.stride_tricks import sliding_window_view
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
    shape = (3,3)
    cols = n
    rows = n
    grid = np.zeros((rows, col), dtype = bool)
    grid = random(grid,n)
    alive = np.array([0,0,1,1,0,0,0,0,0])
    dead = np.array([0,0,0,1,0,0,0,0,0])
    split = sliding_window_view(np.pad(grid,1,'wrap'),shape)
    count = np.count_nonzero(split,axis=(2,3)) - grid
    countalive = np.sum(alive[count])
    
   
    countdead = (n*n) - countalive
    return countdead, countalive    
            
def conway_assignment_three():
    gridsize = 1000
    alivecnt = 0
    deadcnt = 0
   
    cells=[]
    Time = []
    print("Times and cell count for conway_assignment 3")
    for i in range(0,30):
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


def updatefunc3(grid, n):
    shape = (3,3)
    alive = np.array([0,0,1,1,0,0,0,0,0])
    dead = np.array([0,0,0,1,0,0,0,0,0])
    split = sliding_window_view(np.pad(grid,1,'wrap'),shape)
    count = np.count_nonzero(split,axis=(2,3)) - grid
    updated = np.where(grid, alive[count], dead[count])
    return updated

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
        newgrid = updatefunc3(grid,gridsize)        
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
    #conway_assignment_two()
  
    

    
