
# BFS implementation

from util import Node, StackFrontier, QueueFrontier

# start with the source 
# find the target 
def shortest_path (source, target) {
    # create the start node and the BFS frontier 
    start = Node(state = source , parent = null , action = null)
    bfs = QueueFrontier () 
    bfs.add(start)
    
    # create an empty list to store explored nodes
    explored = set () 
    
    # create a while loop until the solution or null is returned 
    
    while not bfs.empty() :
        # remove the node 
        node = bfs.remove ()
        # check if the node is the target, if it is then trasnverse its path and return 
        if node == target : 
            # create a path list to store the actions it took 
            path = [] 
            while node.parent is not None :
                path.append(node.action, node.state)
                node = node.parent 
            path.reverse()
            return path 
        # if it is not the target, add to the explored set 
        explored.append(node.state)
        # go through the neighbors and find the next node to add 
        for movie_id, person_id in neighbors_for_person(node.state):
            if person_id not in explored and not bfs.contains_state(person_id):
                # new child node 
                child = Node(state=person_id, parent=node, action=movie_id)
                # add to the bfs list and while loop starts over 
                bfs.add(child)
                
    # if the list is empty and nothing has bee returned yet, value was not found 
    return None
        
}



