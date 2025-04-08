from collections import deque


def bfs(problem):
    fringe=deque()
    fringe.append(problem.initial_state)
    if fringe.count<1:
        return 'no possible solution'
    if fringe.popleft ==problem.goal_state:
        return 

def dfs():
    pass

def ucs():
    pass