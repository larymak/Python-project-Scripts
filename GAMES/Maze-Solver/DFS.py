import Path_Backtrack
import copy
import Draw
import timeit
import File_Opener

class Stack:
    def __init__(self):
        self.stack = []

    def Add_element(self, data):
        # print("data : ",data)

        if data is None:
            return

        flag = any(isinstance(i, list) for i in data)

        if not flag:
            self.stack.append(data)
             
        else:
            for i in data:
                self.stack.append(i)
                
    def remove(self):
        if len(self.stack) != 0:
            last_element = self.stack.pop()
            return last_element

        else:
            return 0

    def display(self):
        return self.stack

    def is_empty(self):
        return True if len(self.stack) == 0 else False


def read_file(FileLoc):
    Map = []

    with open(FileLoc) as file:
        lines = file.readlines()

        for line in lines:
            temp = []
            temp.extend(line)

            if "\n" in temp:
                temp.remove("\n")

            Map.append(temp)

        file.close()

    #print("File loaded successfully")

    return Map


def Map_Dimension(map):
    row, column = 0, 0
    row, column = len(map), len(map[0])

    return row, column


def Location(map, element):
    row, column = Map_Dimension(map)
    #print(row,column)
    walls = []

    if element == "Walls":
        wall_element = "+"
        #print(row,column)
        for x in range(row):
            for y in range(column):
                #print(x,y)
                if map[x][y] == wall_element:
                    walls.append([x, y])

        return walls

    else:
        for x in range(row):
            for y in range(column):
                if map[x][y] == element:
                    return [x, y]


def Available_move(map, pos, walls, explored):
    row, column = Map_Dimension(map)
    #print("pos : ", pos)
    up = [pos[0] - 1, pos[1]]
    down = [pos[0] + 1, pos[1]]
    left = [pos[0], pos[1] - 1]
    right = [pos[0], pos[1] + 1]

    moves = [up, down, left, right]

    result = copy.deepcopy(moves)

    for x in range(4):
        i = moves[x]
        # print(i)
        if (i[0]) < 0:
            if i in result:
                result.remove(i)
        if (i[1]) < 0:
            if i in result:
                result.remove(i)
        if i[0] >= row:
            if i in result:
                result.remove(i)
        if i[1] >= column:
            if i in result:
                result.remove(i)

    moves = copy.deepcopy(result)

    for i in moves:
        if i in walls:
            result.remove(i)

    moves = copy.deepcopy(result)

    for i in moves:
        if i in explored:
            result.remove(i)

    #print("available move : ", result)

    if len(result) != 0:
        return result
    else:
        return None


def DFS_Algorithm(grid, start_point, end_point):
    t0 = timeit.default_timer()
    frontier = Stack()
    path = Path_Backtrack.Path_Finder()
    explored = []
    destination = Location(grid, end_point)
    walls = Location(grid, "Walls")
    #print("Walls -->", walls)
    initial_position = Location(grid, start_point)
    frontier.Add_element(initial_position)
    while not frontier.is_empty():

        x = frontier.remove()
        #print(x, "--> Pop Element")  # printing pop element
        #print("Frontier->", frontier.display())

        if x == destination:
            #path.Print()
            res = path.Trace(initial_position, destination)
            t1 = timeit.default_timer()
            print(res)
            elapsed_time = round((t1 - t0) * 10 ** 6, 3)
            l = len(res)  # type: ignore
            property = {"method":"DFS",
                        "speed":str(elapsed_time)+str(" nano seconds"),
                        "cost":str(len(explored)),
                        "moves":str(l)}
            graph = Draw.Create_Graph(res,walls,Map_Dimension(grid),property,explored)
            graph.graph()
            return
        else:
            explored.append(x)
            moves = Available_move(grid, x, walls, explored)

            path.Add_element(x, moves)

            if not moves:
                continue
            else:
                frontier.Add_element(moves)

    else:
        print("No Solutions Found !")

    #path.Trace(start_point, end_point)


def runner(Loc,Start,Destination):
    #print("working 1")
    #location = Loc
    #location = File_Opener.get_path()
    Map = read_file(Loc)
    
    DFS_Algorithm(Map, Start, Destination)
    
    

#runner()

