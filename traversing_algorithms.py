
from queue import PriorityQueue
from timeit import default_timer as timer
import matplotlib.pyplot as plt

algorithms = ['BFS', 'DFS', 'UCS', "Greedy Search", "Astar"]
timerList = []
start = 0
end = 0
time = 0
 
class Graph:
    
    
    
    
    def __init__(self):
        
        self.graph = {
"A": [(146, ("A", "O")), (140, ("A", "S")), (494, ("A", "C"))],
"O": [(146, ("O", "A")), (151, ("O", "S"))],
"S": [(151, ("S", "O")), (140, ("S", "A")),(80, ("S", "R")),(99, ("S", "F"))],
"C": [(494, ("C", "A")), (146, ("C", "R"))],
"R": [(80, ("R", "S")), (146, ("R", "C")), (97, ("R", "P"))],
"F": [(99, ("F", "S")), (211, ("F", "B"))],
"B": [(211, ("B", "F")), (101, ("B", "P"))],
"P": [(101, ("P", "B")), (97, ("P", "R")), (138, ("P", "C"))] }
        
        self.edges = {}
        self.weights = {}
        self.heristics = {
            "A" : 10,
            "O" : 9,
            "S" : 7,
            "C" : 8,
            "R" : 6, 
            "F" : 5, 
            "P": 3,
            "B": 0
        }
        self.populate_edges()
        self.populate_weights()
        
       # print("edges : ", self.edges)
        #print("------------------------------------")
        #print("weights  : ", self.weights)
        
        

    def populate_edges(self):
        for key in self.graph:
            neighbours = []
            for each_tuple in self.graph[key]:
                #print(each_tuple[1][1])
                neighbours.append(each_tuple[1][1])
                #print(neighbours)
            self.edges[key] = neighbours
           

    def populate_weights(self):
        for key in self.graph:
            neighbours = self.graph[key]
#            print(neighbours)
            for each_tuple in neighbours:
#                print(each_tuple[1]," --- ",each_tuple[0])
                self.weights[each_tuple[1]] = each_tuple[0]
                
    def neighbors(self, node):
        return self.edges[node]

    def get_cost(self, from_node, to_node):
        return self.weights[(from_node,  to_node)]
    def get_heuristic(self, node):
        return self.heristics[node]

def greedy(graph, start, goal):
    
    
    visited = []
    queue = PriorityQueue()
    queue.put((0, start))
    while queue:
        cost, node = queue.get()
        if node not in visited:
            visited.append(node)
            if node == goal:
                break
            for i in graph.neighbors(node):
                if i not in visited:
                    total_cost = graph.get_heuristic(i)
                    queue.put((total_cost, i))
                    
                    
    return visited

def astar(graph, start, goal):
   
    visited = []
    queue = PriorityQueue()
    queue.put((0, start))
    while queue:
        cost, node = queue.get()
        if node not in visited:
            visited.append(node)
            if node == goal:
                break
            for i in graph.neighbors(node):
                if i not in visited:
                    total_cost = cost + graph.get_cost(node, i) + graph.get_heuristic(node)
                    queue.put((total_cost, i))
                    
    return visited



# visits all the nodes of a graph using DFS
def bfs(graph, start):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]
    while queue:
        print("queue : ", queue)
        
        node = queue.pop(0)
        print('node being explored: ',node)
        print("explored : ", explored)
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graph.edges[node]
            # add reversed neighbours of node to queue so they could pop in actual order.
            #neighbours.reverse()
            for neighbour in neighbours:
                queue.append(neighbour)
    return explored


def dfs(graph, start):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]
    # keep looping until there are nodes still to be checked
    while queue:
        print("queue : ", queue)
        # pop Top node (first node) from stack
        node = queue.pop()
#        node = queue.pop(0)
        print('node being explored: ',node)
        print("explored : ", explored)
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graph.edges[node]
            # add reversed neighbours of node to stack so they could pop in actual order.
            neighbours.reverse()
            for neighbour in neighbours:
                queue.append(neighbour)
    return explored



# Now Implementing UCS


def ucs(graph, start, goal):
    visited = []
    queue = PriorityQueue()
    queue.put((0, start))
    while queue:
        cost, node = queue.get()
        if node not in visited:
            visited.append(node)
            if node == goal:
                break
            for i in graph.neighbors(node):
                if i not in visited:
                    total_cost = cost + graph.get_cost(node, i)
                    queue.put((total_cost, i))
                    
    return visited




print("Executing Program Now!!!!\n\n\n")



print("Executing Bredth-First Search: \n\n")
start = timer()
print("Starting Time Of BFS Is: ", start)
print("\n")
print("Traversal: ", bfs(Graph(), 'A'))
end = timer()
print("\n")
print("Ending Time Of BFS Is: ", end)
print("\n\n\n")
time = end - start
timerList.append(time);



print("Executing Depth-First Search: \n\n")
start = timer()
print("Starting Time Of DFS Is: ", start)
print("\n")
print("Traversal: ", dfs(Graph(), 'A'))
end = timer()
print("\n")
print("Ending Time Of DFS Is: ", end)
print("\n\n\n")
time = end - start
timerList.append(time);

print("Executing Uniform Cost Search Search: \n\n")
start = timer()
print("Starting Time Of UCS Is: ", start)
print("\n")
print("Traversal: ", ucs(Graph(), "A", "P"))
end = timer()
print("\n")
print("Ending Time Of DFS Is: ", end)
print("\n\n\n")
time = end - start
timerList.append(time);

print("Executing Greedy Search Search: \n\n")
start = timer()
print("Starting Time Of Greedy Search Is: ", start)
print("\n")
print("Traversal: ", greedy(Graph(), "A", "P"))
end = timer()
print("\n")
print("Ending Time Of Greedy Search Is: ", end)
print("\n\n\n")
time = end - start
timerList.append(time);

print("Executing Astar Search: \n\n")
start = timer()
print("Starting Time Of Astar Search Is: ", start)
print("\n")
print("Traversal: ", astar(Graph(), "A", "P"))
end = timer()
print("\n")
print("Ending Time Of Astar Search Is: ", end)
print("\n\n\n")
time = end - start

timerList.append(time);

print(timerList)

plt.bar(algorithms, timerList)
plt.title('Time Complexity For Different Searching Algorithms')
plt.xlabel(algorithms)
plt.ylabel(timerList)
plt.show()



      



    




