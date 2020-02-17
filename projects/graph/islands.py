from graph import Stack, Queue

'''
Write a function that takes a 2D binary array and returns the number of 1 islands. 
An island consists of 1s that are connected to the north, south, east, or west.

For example:
'''



# islands = [[0,1,0,1,0],
#            [1,1,0,1,1],
#            [0,0,1,0,0],
#            [1,0,1,0,0],
#            [1,1,0,0,0]]


islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
           [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
           [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
           [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
           [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
           [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
           [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
           [0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
           [1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
           [1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
           [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

def get_neighbors(x,y,matrix):
    neighbors = []
    if x > 0 and matrix[x-1][y] == 1:
        neighbors.append((x-1,y))
    if y > 0 and matrix[x][y-1] == 1:
        neighbors.append((x, y-1))
    if len(matrix) > x+1 and matrix[x+1][y] == 1:
        neighbors.append((x+1,y))
    if len(matrix[x]) > y+1 and matrix[x][y+1] ==1:
        neighbors.append((x,y+1))
    return neighbors

def bft(x,y, matrix, visited):
    queue = Queue()
    queue.enqueue((x,y))
    while queue.size() > 0:
        v = queue.dequeue()
        x = v[0]
        y = v[1]
        if not visited[x][y]:
            visited[x][y]  = True
            for neighbor in get_neighbors(x,y, matrix):
                queue.enqueue(neighbor)
    return visited

def island_counter(matrix):
    count = 0
    visited = []
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))
    
    for y in range(len(matrix[0])):
        for x in range(len(matrix)):
            if not visited[x][y]:
                if matrix[x][y] == 1:
                    visited = bft(x,y,matrix, visited)
                    count += 1
    return count


print(island_counter(islands))