import BFS
import DFS
import os
import time

'''
Default parameters:
    1) maze.txt is the default maze file
    2) b is the default starting point
    3) p is the default destination point
'''
grid = str(os.getcwd())+"\\maze.txt"
#grid = "D:\Code\Txt\maze.txt"
start_point = "b"
end_point = "p"
print("***Welcome to Maze Solver***\n")

print("Enter the Algorithm you want to use to solve the maze")
print("1. Depth First Search")
print("2. Breadth First Search")
print("3. Both\n")

choice = int(input("Enter your choice : "))

if choice == 1:
    print("You have selected Depth First Search")
    DFS.runner(grid, start_point, end_point)
elif choice == 2:
    print("You have selected Breadth First Search")
    BFS.runner(grid, start_point, end_point)

elif choice == 3:
    print("You have selected Both")
    
    time.sleep(1)
    BFS.runner(grid, start_point, end_point)
    DFS.runner(grid, start_point, end_point)

else:
    print("Invalid Choice")