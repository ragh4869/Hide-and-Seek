import sys

# Parse the map from a given filename
def parse_map(filename):
    with open(filename, "r") as f:
        return [[char for char in line] for line in f.read().rstrip("\n").split("\n")]
    
# Add a pichu to the house_map at the given position, and return a new house_map (doesn't change original)
def add_pichu(house_map, row, col):
    return house_map[0:row] + [house_map[row][0:col] + ['p',] + house_map[row][col+1:]] + house_map[row+1:]

# Return a string with the house_map rendered in a human-pichuly format
def printable_house_map(house_map):
    return "\n".join(["".join(row) for row in house_map])

# Identify valid successors of given house_map state - Part 1
def valid_successors(fringe,invalid_successors):
    # Get the all pichu coordinates from the fringe 
    pichu = fringe.pop()

    fringe2 = []
    if (-1,-1) in pichu:
        # Get all the valid state coordinates for the first pichu
        fringe2.extend(valid_successors2(fringe,invalid_successors,pichu))
        return fringe2
    
    for i in fringe:
        # Get the valid state coordinates after adding a new pichu
        pichu2 = pichu.copy()
        pichu2.append(i)
        fringe2.extend(valid_successors2(fringe,invalid_successors,pichu2))
    
    # Return list of all list of valid state coordinates along with the pichu coordinates
    return fringe2


# Identify valid successors of given house_map state - Part 2
def valid_successors2(fringe,invalid_successors,pichu):
    
    # Identify the valid state coordinates row-wise
    rows = [(r,c) for r,c in fringe for r2,c2 in invalid_successors if ((r!=pichu[-1][0] and c!=pichu[-1][1] and abs(r-pichu[-1][0])!=abs(c-pichu[-1][1])) or (r==pichu[-1][0] and r2==pichu[-1][0] and c>c2 and c2>pichu[-1][1]) or (r==pichu[-1][0] and r2==pichu[-1][0] and c<c2 and c2<pichu[-1][1]))]
    # Identify the valid state coordinates column-wise
    cols = [(r,c) for r,c in fringe for r2,c2 in invalid_successors if ((r!=pichu[-1][0] and c!=pichu[-1][1] and abs(r-pichu[-1][0])!=abs(c-pichu[-1][1])) or (c==pichu[-1][1] and c2==pichu[-1][1] and r>r2 and r2>pichu[-1][0]) or (c==pichu[-1][1] and c2==pichu[-1][1] and r<r2 and r2<pichu[-1][0]))]
    # Identify the valid state coordinates diagonal-wise
    diagonals = [(r,c) for r,c in fringe for r2,c2 in invalid_successors if ((r!=pichu[-1][0] and c!=pichu[-1][1] and abs(r-pichu[-1][0])!=abs(c-pichu[-1][1])) or (abs(r-pichu[-1][0])==abs(c-pichu[-1][1]) and abs(r2-pichu[-1][0])==abs(c2-pichu[-1][1]) and r>r2 and r2>pichu[-1][0] and c<c2 and c2<pichu[-1][1]) or (abs(r-pichu[-1][0])==abs(c-pichu[-1][1]) and abs(r2-pichu[-1][0])==abs(c2-pichu[-1][1]) and r<r2 and r2<pichu[-1][0] and c>c2 and c2>pichu[-1][1]))]
    
    if (-1,-1) in pichu:
        pichu.pop(0)
    
    # Return list of valid state coordinates along with the pichu coordinates
    return [list(set(rows + cols + diagonals))+[pichu]]


# Get list of successors of given house_map state
def successors(house_map,x=1):
    if x == 1:
        return [(r, c) for r in range(len(house_map)) for c in range(len(house_map[0])) if house_map[r][c] == '.']
    else:
        return [(r, c) for r in range(len(house_map)) for c in range(len(house_map[0])) if house_map[r][c] in 'X@']
    
# Arrange agents on the map
def solve(initial_house_map,k):
    
    # Get the initial pichu location
    pichu_loc=[(row_i,col_i) for col_i in range(len(initial_house_map[0])) for row_i in range(len(initial_house_map)) if initial_house_map[row_i][col_i]=="p"][0]
    # Get the initial set of state coordinates on which pichu could be placed
    fringe_ini = [successors(initial_house_map)+[[(-1,-1),pichu_loc]]]
    # Get the set of invalid coordinates to ascertain whether they come in between pichu and any state coordinate
    invalid_successors = successors(initial_house_map,0)
    
    # Get the list of valid state coordinates along with pichu location for first pichu
    fringe = valid_successors(fringe_ini.pop(), invalid_successors)

    while len(fringe) > 0:
        # Using DFS search method rather than BFS as it is 100 times more faster
        for s in valid_successors(fringe.pop(), invalid_successors):
            # Check if number of valid pichu selected is equal to number of desired pichus to be placed in the map 
            if len(s[-1]) == k:
                updated_map = initial_house_map.copy()
            
                for i in s[-1]:
                    # Update the initial map with all the pichu coordinates and return the output as a map
                    updated_map = add_pichu(updated_map,i[0],i[1])
                return (updated_map,True)
            
            fringe.append(s)
    else:
        # Return False and initial house map if all pichus could not be added to the map
        return (initial_house_map,False)

# Main Function
if __name__ == "__main__":
    house_map=parse_map(sys.argv[1])
    # This is k, the number of agents
    k = int(sys.argv[2])
    print ("Starting from initial house map:\n" + printable_house_map(house_map) + "\n\nLooking for solution...\n")
    solution = solve(house_map,k)
    print ("Here's what we found:")
    print (printable_house_map(solution[0]) if solution[1] else "False")