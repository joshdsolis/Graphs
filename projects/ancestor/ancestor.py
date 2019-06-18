def earliest_ancestor(family_list, child):
    vertices = {}
    for (v1, v2) in family_list:
        vertices[v1] = set()
        vertices[v1].add(v2)
    
    visited = set()
    q = []
    q.append([child])
    # While the queue is not empty...
    while len(q) > 0:
        # Dequeue the first PATH
        p = q.pop(0)
        # GRAB THE VERTEX FROM THE END OF THE PATH
        v = p[-1]
        # If that vertex has not been visited...
        if v not in visited:
            # Mark it as visited
            visited.add(v)
            # Then add A PATH TO all of its neighbors to the back of the queue
            for neighbor in vertices[v]:
                # Copy the path
                path_copy = [p]
                # Append the neighbor to the back of the copy
                # Enqueue copy
                path_copy.append(neighbor)
                q.append(path_copy)
    print(path_copy)
    print(vertices)
    pass


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

earliest_ancestor(test_ancestors, 1)
