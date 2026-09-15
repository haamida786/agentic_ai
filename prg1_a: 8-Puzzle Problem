from collections import deque
goal = [1,2,3,4,5,6,7,8,0]
def get_neighbors(state):
    neighbors = []
    i = state.index(0)
    moves =[(-1,0),(1,0),(0,-1),(0,1)]
    x,y = divmod(i,3)

    for dx,dy in moves:
        nx,ny=x+dx,y+dy
        if 0<=nx<3 and 0<=ny<3:
          new = state[:]
          ni=nx*3+ny
          new[i],new[ni]=new[ni],new[i]
          neighbors.append(new)
    return neighbors

def bfs(start):
    queue = deque([(start,[])])
    visited = set()

    while queue:
        state,path = queue.popleft()
        if state == goal:
            return path + [state]

        visited.add(tuple(state))
        for n in get_neighbors(state):
            if tuple(n) not in visited:
                queue.append((n,path+[state]))

start = [1,2,3,4,0,5,6,7,8]
print(bfs(start))
