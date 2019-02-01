# Author: Milo Dietrick
# CSCI 404: project 1 map searching
# Purpose: 
#  Implement a search algorithm that can find a route between any two cities. 
# Project Link: http://inside.mines.edu/~huawang/CSCI404_Projects/Project1/


#Source http://www.gilles-bertrand.com/2014/03/dijkstra-algorithm-python-example-source-code-shortest-path.html

#libraries
from pathlib import Path



#NOTES:

#computerphile on youtube for explanation
#use a priority queue

def dijkstra(graph,start,end,visited=[],distances={},predecessors={}):
    """ calculates a shortest path tree routed in start
    """    
    # a few sanity checks
    if start not in graph:
        raise TypeError('The root of the shortest path tree cannot be found')
    if end not in graph:
        raise TypeError('The target of the shortest path cannot be found') 


    #base case of recusive loop
    if start == end:
        # We build the shortest path and display it
        path=[]
        pred=end
        print("distance:", str(distances[end]), "km")
        print("route:")
        while pred != None:
            path.append(pred)
            pred=predecessors.get(pred,None)
            print(pred)

        #print('shortest path: '+str(path)+" cost="+str(distances[end])) 
        print("distance", str(distances), "km")
        print("route: \n", str(path))





    else :     
        # if it is the initial  run, initializes the cost
        if not visited: 
            distances[start]=0
        # visit the neighbors
        for neighbor in graph[start] :
            if neighbor not in visited:
                new_distance = distances[start] + graph[start][neighbor]
                if new_distance < distances.get(neighbor,float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = start
        # mark as visited
        visited.append(start)
        # now that all neighbors have been visited: recurse                         
        # select the non visited node with lowest distance 'x'
        # run Dijskstra with start='x'
        unvisited={}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k,float('inf'))        
        x=min(unvisited, key=unvisited.get)
        dijkstra(graph,x,end,visited,distances,predecessors)










###########MAIN##########
#create the graph
print("")

#read in the data
input_file = str( Path.cwd() / 'input1.txt')
with open (input_file, "r") as myfile:
     data=myfile.read().splitlines()

graph = {}
for i in data:
    if i == "END OF INPUT": break  
    begin = i.split()[0]
    node = {i.split()[1]: int(i.split()[2])}
    if begin in graph: #if the start city is in the set then it has been added   
        graph[begin].update(node) #add the corresponding node and the distance
    else: # this is a new node add it to the dictionary
        graph[begin] = node

#add the double linked routes
for i in graph:    
    for key in graph[i]:
        if key in graph:
            graph[key].update({i: graph[i].get(key)}) 


for i in graph:
   print (i, graph[i])
print(" ")
# for i in graph:
#     if i == goal:
#         print('The distance between Bremen and Hannover is:', graph[i]['Hannover']) #to access the distance value
#         for key in graph[i]:
#             print(key)


#NOW FOR THE SEARCH
start = "Bremen"
goal = "Frankfurt"


dijkstra(graph, start, goal)



# #create a Breadth-First Search (BFS)

# visited = set()
# queue = collections.deque([start])
# while queue: 
#  vertex = queue.popleft()
#  for neighbour in graph[vertex].keys(): 
#   if neighbour not in visited: 
#    visited.add(neighbour) 
#    queue.append(neighbour) 

#loop through the keys in the graph
#for each key in the graph look through the keys in the corresponding dictionary
#save the key as a temporary value
#then search through the graph keys for the nested key (call this temp1)
#then search through the graph for temp1
#search through the temp1 keys and repeat the proccess 

#uniform class search, djasktas algorithm to find the city
