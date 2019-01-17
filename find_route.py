# Author: Milo Dietrick
# CSCI 404: project 1 map searching
# Purpose: 
#  Implement a search algorithm that can find a route between any two cities. 
# Project Link: http://inside.mines.edu/~huawang/CSCI404_Projects/Project1/

#libraries
from pathlib import Path
input_file = str( Path.cwd() / 'input1.txt')
with open (input_file, "r") as myfile:
     data=myfile.readlines()
print(data)

#def find_route (input_file, origin_city, dest_city):
    #read the input file, the file contains two cities per line and the distance 
    #between them


    #thoughts: use a dictionary to create a graph of nodes and


