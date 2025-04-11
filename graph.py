import collections

class Graph:
    def __init__(self,adjlist):
        self.adjacency_list=adjlist

    def print(self):
        for node in self.adjacency_list:
            print(node)
            for child in self.adjacency_list[node]:
                print(f'>>{child}\n')

    def bfs(self,root):
        visited=[] 
        fringe=collections.deque([root])

        while fringe:
            node=fringe.popleft()
            if node not in visited:
              visited.append(node)
              print(node)
             
            for child in self.adjacency_list[node]:
                if(child not in visited):
                   fringe.append(child)
        return visited
    def add_edge(self,node1,node2):
        print('Printed first')
        try:
          if node1 not in self.adjacency_list:
              self.adjacency_list[node1]=[]
          self.adjacency_list[node1].append(node2)
          self.adjacency_list[node2]=[]
        except Exception as e:
           print(e)

    def dfs(self,root):
        visited=[]
        fringe=collections.deque([root])
        while fringe:
            node=fringe.pop()
            print(node)
            if node not in visited:
                visited.append(node)
            
            for child in self.adjacency_list[node]:
                if child not in visited:
                    fringe.append(child)
        print(visited)


adlist={
    'A':['B','C'],
    'B':['E','F'],
    'C':['G','H'],
    'E':[],
    'F':[],
    'G':[],
    'H':[]
    }
g=Graph(adjlist=adlist)
g.add_edge('T','Z')
print(g.dfs('A'))
print('bfs')
print(g.bfs('A'))
print(g.adjacency_list)