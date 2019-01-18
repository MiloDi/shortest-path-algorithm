# Author: Milo Dietrick
# CSCI 404: project 1 map searching
# Purpose: 
#  Implement a search algorithm that can find a route between any two cities. 
# Project Link: http://inside.mines.edu/~huawang/CSCI404_Projects/Project1/

#libraries
from pathlib import Path


input_file = str( Path.cwd() / 'input1.txt')
with open (input_file, "r") as myfile:
     data=myfile.read().splitlines()

#Now i need to create a graph
# start = []
# end = []
# dist = []

# for string in data:


#def find_route (input_file, origin_city, dest_city):

    #thoughts: use a dictionary to create a graph of nodes and
#i need to create a map (dictionary) that will hold each of the cities and the cities
#connected to it as well as the distances between them
#so maybe a dictionary within a dictionary? now how do i creat that
graph = dict()
for i in data:
    if i == "END OF INPUT": break    
    node = {i.split()[1]: i.split()[2]}
    start = i.split()[0]
    if start in graph: #if the start city is in the set then it has been added
        #add the corresponding node and the distance
        graph[start].append(node)
    else: # this is a new node add it to the dictionary
        graph[start] = [node]

for i in graph:
    print (i, graph[i])

