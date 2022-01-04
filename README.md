### 1. Navigation

##### Objective -
To find the optimal path between pichu and the goal, and return the path length and direction to the goal.

##### Initial State: 
The initial state consists of the house map with the pichu in the starting point and the goal point in its location.

##### Set of Valid States:
All the positions marked "." are set of valid states/points the pichu can move to reach the goal.

##### Successor Function:
Provides all the valid moves for the pichu, from the current coordinate, to move along with the path direction.

##### Cost Function:
The cost function computes the number of moves taken for the pichu to reach the goal. Each move has a cost of 1.

##### Goal State:
The goal state is the state when the pichu has traveled the path optimally and reached the goal, that is, "@".

##### Reason for failure of skeleton code:
In the skeletal code, the algorithm implemented is DFS search method and while implementing it, there has been no precautions taken to check if a coordinate is revisited. Once the pichu revisits the coordinate, it keeps looping with the same 2 coordinates in DFS and falls into an infinite loop.
Also, the code does not provide the actual distance and path to the goal "@".

##### Solution Implemented:
The code first takes in the system arguments and the map is sent to the solve function. It then finds the location of the pichu and records the coordinates in the fringe and the visited_moves. The visited moves list is added to eliminate the possibility of infinite loop as the pichu will not visit the same coordinate again. The code then gets the possible moves for the pichu to move to the next position. I added the path directions along with the possible coordinates, and by adding this will eliminate the need to compute the path directions of the optimal path at a later time. Along with getting the next moves, I also keep appending the positions vistied by the pichu and append their coordinates in the visited_moves list. As in the skeletal code, the output returned was a random set. This is changed with returning the optimal path distance and directions taken by the pichu to reach the goal. Finally, I used 2 search methods. I used the DFS search method first and found that for maps having multiple complete paths, the path chosen by the pichu was not optimal. Due to this, I switched to using BFS search method as it checks all the coordinates at the same depth level, leading pichu to choose the ideal path.


### 2. Hide and Seek

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

