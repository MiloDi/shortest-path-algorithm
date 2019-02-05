Milo Dietrick
CWID: 10830362
Python programming language
This program was built and run in Linux

The code is structured with the find_route function implemented first
This function implements dijkstra's algorithm to find the shortest routes
It takes in a graph that is built below the function, a starting point and
and ending point when it is called. Underneath the function the program reads
in a file from the same directory as the program and converts it into a graph
that can be passed into the find_route function. This file is called input1.txt

To run the program:
1. navigate to the directory where the program is located and make sure
   that the input file that you wish to test is located in the same
   directory as the program.
2. Open the program file with a text editor and change the file_name variable
   located at line 68 of the code to the name of the input file you need to test
   the example test file is named input1.txt
3. Save the program, and run using 'python find_route.py'.

Note: you can use a virtual environment such as pipenv to run the program but it 
      shouldn't be necessary as the only library that the program uses is the Path
      module from the pathlib library, for which the only purpose is to have a dynamic
      file path for the program to locate the input file.