class Solution:
    #create a direction hashmap{'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0)}
    #create a set visited, iterating through the path string, finding it's according position, if it is in set, return false. and include it in the set. 
    #in the end if none positions had been visited, return True
    def isPathCrossing(self, path: str) -> bool:
        directions = {'N': [0, -1], 'S': [0, 1], 'E': [1, 0], 'W': [-1, 0]}
        visited = set()
        visited.add((0, 0))
        position = [0, 0]

        for direction in path:
            x, y = directions[direction]
            
            position[0] += x
            position[1] += y
            visit = tuple(position)
            # print('tuple', visit)
            if visit in visited:
                return True
            else: 
                visited.add(tuple(position))

        return False
