### Hide and Seek

##### Objective - 
To find the map having the desired k pichus with the condition that they do not face each other.

##### Initial State: 
The initial state consists of the house map with the 1 pichu along with all the obstacles and open positions.

##### State Space:
All the positions on the map (coordinates) which are valid to add the pichus.

##### Successor Function:
Provides all the valid positions/coordinates for the next pichu considering the valid states of current pichu.

##### Cost Function:
The cost function computes the number of positions available for the next pichu given current pichu.

##### Goal State:
The goal state is the state when all k pichus have been added to the map.

##### Search Abstraction Used:
Initially both BFS and DFS search method was used. Taking BFS, since it goes through all the possible list of valid states at each level, the computation becomes very slow. Instead, the DFS method is used as it does not go through every possible list of valid states and gives the output 100 times faster.

##### Solution Implemented:
The code first takes in the system arguments and the map is sent to the solve function. It then finds the location of the pichu and records the coordinates, all coordinates the next pichu can be added and invalid successors(obstacles). Having the first pichu location, the code then passes on to:
###### valid_successors() - Takes in the fringe, pichu coordinates and invalid_successors(obstacles). Takes in pichu coordinates separately in a list and passes to the valid_successors2(). When the first set of valid states are produced for the first pichu, it moves to a different section where iteratively takes in values from the fringe, calls valid_successors2() and updates the fringe with valid states for the next set of pichus. This function is called till it reaches k pichus.
###### valid_successors2() - Takes in the fringe, pichu coordinates and invalid_successors(obstacles). The logic for the valid states of the next pichu being added is defined by 3 checks which are - 
###### rows - Checks for different row, column and not in diagonal of pichu. Apart from this, checks the condition if it is same row and there is an obstacle in between then condition satisfies.
###### cols - Checks for different row, column and not in diagonal of pichu. Apart from this, checks the condition if it is same column and there is an obstacle in between then condition satisfies.
###### diagonals - Checks for different row, column and not in diagonal of pichu. Apart from this, checks the condition if it is same diagonal and there is an obstacle in between then condition satisfies.
The DFS search method is used for the computation as it is atleast 100 times faster than the BFS search method. Considering all the above conditions and applying them, a final list of k pichu positions/coordinates are returned and added to the initial_house_map and renamed as updated_map. The updated map having all the k pichus added and not facing each other is returned as the desired output. 

##### Command:
The following command can be used to run the program in the command prompt-

python arrange_pichus.py map3.txt 5
