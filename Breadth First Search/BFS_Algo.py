from collections import deque
from typing import List, Dict, Set

def bfs_graph(graph: Dict[int, List[int]], start: int) -> List[int]:
    visited = set()
    queue = deque()
    
    # 1. Mark visited and enqueue start
    visited.add(start)
    queue.append(start)
    
    traversal_order = []
    
    # 2. Process the queue
    while queue:
        node = queue.popleft()
        traversal_order.append(node)
        
        # 3. Explore neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)      # Mark BEFORE enqueuing!
                queue.append(neighbor)
                
    return traversal_order

# Example Usage:
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}
print(bfs_graph(graph, 0))  # Output: [0, 1, 2, 3, 4]
