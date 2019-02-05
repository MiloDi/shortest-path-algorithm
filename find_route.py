# Author: Milo Dietrick
# CSCI 404: project 1 map searching
# Purpose: 
# Implement a search algorithm that can find a route between any two cities. 
# Project Link: http://inside.mines.edu/~huawang/CSCI404_Projects/Project1/

#libraries
from pathlib import Path

def find_route(graph, start, end, seen=[], previous={}, dist={}):
    if start not in graph:  #if the current starting point does not exists in the graph
        print("distance: infinity\nroute:\n none")
        return 
    if end not in graph: #if the ending point does not exists in the graph
        print("distance: infinity\n route:\n none")
        return

    # base case of recusive loop
    if start == end:    
        p = end
        path_list,distance_list = [],[]
        #iterate through the list of previsous visted nodes
        #to find the way back to the starting point
        while p != None:
            path_list.append(p)
            distance_list.append(dist[p])
            p=previous.get(p)

        # print the ouput for the path, since the path is built
        # backwards it needs to be print it out from the end
        print("distance:", distance_list[0], "km\nroute:")       
        distance_list[0] = distance_list[0] - distance_list[1]
        i = len(path_list) - 1
        while i > 0:
            print (path_list[i], "to", path_list[i-1] + ",",  distance_list[i-1])
            i-=1
    else :     
        # At the start the initial distance is 0
        if len(seen) == 0: 
            dist[start]=0  
        #look through the graph for unseen points 
        for node in graph[start]:
            if node not in seen:
                x = graph[start][node] + dist[start]
                #pick the point with the shortest distance
                if x < dist.get(node,float('inf')):
                    previous[node] = start
                    dist[node] = x                  
        # add the current point to the list of points that have been seen
        seen.append(start)
        #look for unseen points
        unseen={}
        for i in graph:
            if i not in seen:
                unseen[i] = dist.get(i,float('inf'))  
        #find the minimum distance in the unseen dictionary
        current_postion = min(unseen, key=unseen.get)
        #make the recusive call
        find_route(graph,current_postion,end,seen,previous,dist)

###########MAIN##########

#read in the data

#TO-Do
#change this string to the name of the file that is to be used to test
#the program, make sure the file is in the same directory as the program
file_name= 'input1.txt'

input_file = str( Path.cwd() / file_name)
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

# for i in graph:
#     print(i, graph[i])
#NOW FOR THE SEARCH

start = "Bremen"
goal = "Frankfurt"
print(" ")
find_route(graph, start, goal)