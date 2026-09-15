graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'J'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': [],
    'I': [],
    'J': [],
    'K': [],
    'L': [],
    'M': [],
    'N': [],
    'O': []
}
 
def MA(start, goal, path, level, maxD):
    path.append(start)
 
    if start == goal:
        return True
 
    if level == maxD:
        path.pop()
        return False
 
    for child in graph[start]:
        if MA(child, goal, path, level + 1, maxD):
            return True
 
    path.pop()
    return False
 
start = 'A'
goal = input("Enter the goal state: ")
maxD = int(input("Enter the maximum depth limit: "))
path = []
 
if MA(start, goal, path, 1, maxD):
    print("Path:", path)
else:
    print("No path available for the given depth limit")
