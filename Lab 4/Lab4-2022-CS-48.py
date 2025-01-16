class vertex:
    def __init__(self, value):
        self.value = value
        self.next = None
class graph:
    def __init__(self):
        self.HG = [None] * 10
    def add_edge(self,vertex1, vertex2):
        n_node1 = vertex(vertex1)
        n_node2 = vertex(vertex2)
        for i in range(10):
            if self.HG[i] is None:
                self.HG[i] = n_node1
                self.HG[i].next = n_node2
                break
            elif self.HG[i].value == n_node1.value:
                p = self.HG[i]
                while p.next:
                    p = p.next
                p.next = n_node2
                break
        n_node1 = vertex(vertex2)
        n_node2 = vertex(vertex1)
        if n_node1.value != n_node2.value:
            for i in range(10):
                if self.HG[i] is None:
                    self.HG[i] = n_node1
                    self.HG[i].next = n_node2
                    break
                elif self.HG[i].value == n_node1.value:
                    p = self.HG[i]
                    while p.next:
                        p = p.next
                    p.next = n_node2
                    break
    def delete_edge(self, vertex1, vertex2):
        if vertex1 == vertex2:
            for i in range(10):
                if self.HG[i] and self.HG[i].value == vertex1:
                    self.HG[i] = self.HG[i].next 
                    return
        for i in range(10):
            if self.HG[i]:
                if self.HG[i].value == vertex1:
                    next_pointer = self.HG[i]                
                    while next_pointer.next and next_pointer.next.value != vertex2:
                        next_pointer = next_pointer.next
                    if(next_pointer.next is not None):
                        next_pointer.next = next_pointer.next.next
                    else:
                        return 0
                    break
        for i in range(10):
            if self.HG[i]:
                if self.HG[i].value == vertex2:
                    next_pointer = self.HG[i]                
                    while next_pointer.next and next_pointer.next.value != vertex1:
                        next_pointer = next_pointer.next
                    if(next_pointer.next is not None):
                        next_pointer.next = next_pointer.next.next
                    else:
                        return 0
                    break
    def get_connected_nodes(self, node):
        nodes_list = []
        for i in range(10):
            if self.HG[i]:
                if self.HG[i].value == node:
                    p = self.HG[i].next
                    while p:
                        nodes_list.append(p.value)
                        p = p.next
                        
                    break
            
        return nodes_list
    def get_edge(self, vertex1, vertex2):
        for i in range(10):
            if self.HG[i]:
                if self.HG[i].value == vertex1:
                    p = self.HG[i].next
                    while p:
                        if p.value == vertex2:
                            return [vertex1,vertex2]
                        p = p.next
        return []
    def are_connected(self, vertex1, vertex2):
        for i in range(10):
            if self.HG[i] and self.HG[i].value == vertex1:
                p = self.HG[i].next
                while p:
                    if p.value == vertex2:
                        return True
                    p = p.next
        return False
    def is_valid_path(self, path):
        for i in range(len(path) - 1):
            node1 = path[i]
            node2 = path[i + 1]
            if not self.get_edge(node1, node2):
                return False
        return True
    def print_graph(self):
        for i in range(10):
            temp = self.HG[i]
            self.print_node(temp)            
    def print_node(self,head):
        temp = head
        if not temp:
            return
        while temp:
            print(temp.value, "->", end = " ")
            temp = temp.next 
        print("None")
g1 = graph()           
g1.add_edge(1, 1)
g1.add_edge(1, 3)
g1.add_edge(2, 4)
g1.add_edge(1, 2)
g1.print_graph()
print("after deletion")
result = g1.delete_edge(1, 1)
if result == 0:
    print("no edge found b/w given vertices")
g1.print_graph()
print(f"nodes that are connected to 1 :{g1.get_connected_nodes(1)}")
print(g1.get_edge(1, 3))
result = g1.are_connected(1, 1)
if result == True:
    print("found an edge between given two vertices")
else:
    print("can not found an edge between given two vertices")
path = [1, 2, 4]
print(f"Is valid path {path}: {g1.is_valid_path(path)}") 

path = [1, 3, 4]
print(f"Is valid path {path}: {g1.is_valid_path(path)}") 

def bfs(adj,starting):
    visited = [False] * len(adj)
    queue = []
    visited[starting] = True
    queue.append(starting)
    while queue:
        curr = queue.pop(0)
        
        print(curr, end = ' ')
        for i in adj[curr]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
def add_edge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)
vertices = 5
adj = [[] for _ in range(vertices)]
add_edge(adj, 0, 1)
add_edge(adj, 0, 2)
add_edge(adj, 1, 3)
add_edge(adj, 1, 4)
add_edge(adj, 2, 4)
bfs(adj, 4)

if __name__ == "__main__":
    pass 
