graph = {'A':['B','C'],
              'B':['C','D'],
              'C':['D'],
              'D':['C'],
              'E':['F'],
              'F':['C']}
def find_path(graph,start,end,path=[]):
     path = path + [start]
     if start == end:
          return path
     if(start not in graph):
          return None
     for node in graph[start]:
          if node not in path:
               newpath = find_path(graph,node,end,path)
               if newpath: return newpath
     return None 
def find_all_path(graph,start,end,path=[]):
      path = path + [start]
      if start == end:
           return [path]
      if(start not in graph):
           return []
           path =[]
      for node in graph[start]:
           if node not in path:
                newpath = find_all_path(graph,node,end,path)
           for newpath in newpath:
               path.append(newpath)
               return path
def find_shortest_path (graph,start,end,path=[]):
     path = path + [start]
     if start == end:
          return path
     if(start not in graph):
          return None
     shortest = None
     for node in graph[start]:
          if node not in path:
               newpath = find_shortest_path(graph,node,end,path)
               if newpath:
                    if not shortest or len(newpath)<len(shortest):
                         shortest = newpath
     return shortest
print (find_path(graph,'A', ''))
print (find_path(graph,'A', 'D'))
print (find_shortest_path(graph, 'A', 'D'))
print (find_all_path(graph, 'A', 'D') )


                      
