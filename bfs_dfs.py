def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        if node in graph:
            for neighbour in graph[node]:
                dfs(visited, graph, neighbour)

def bfs(visited, graph, node, queue):
    visited.add(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        if s in graph:
            for neighbour in graph[s]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

def main():
    visited1 = set()  # To keep track of DFS visited nodes
    visited2 = set()  # To keep track of BFS visited nodes
    queue = []        # For BFS
    n = int(input("Enter number of nodes: "))
    graph = dict()

    for i in range(1, n + 1):
        edges = int(input("Enter number of edges for node {}: ".format(i)))
        graph[i] = set()  # Change from list to set for better performance
        for j in range(1, edges + 1):
            node = int(input("Enter edge {} for node {}: ".format(j, i)))
            graph[i].add(node)

    start_node = int(input("Enter the starting node: "))

    while True: 
        print("\nChoose traversal method:")
        print("1. DFS (Depth-First Search)")
        print("2. BFS (Breadth-First Search)")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("The following is DFS")
            dfs(visited1, graph, start_node)
        elif choice == '2':
            print("The following is BFS")
            bfs(visited2, graph, start_node, queue)
        else:
            print("Invalid choice! Please enter 1 for DFS or 2 for BFS.")

if __name__ == "__main__":
    main()
