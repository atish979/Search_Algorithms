# Breadth-First Search (BFS)

## Overview
Breadth-First Search (BFS) is a fundamental graph traversal algorithm that explores vertices in layers, visiting all neighbors of a vertex before moving to the next level.

## Why Use BFS?

1. **Shortest Path Finding**: BFS finds the shortest path between two nodes in an unweighted graph.
2. **Level-Order Traversal**: Ideal for exploring nodes level by level, useful in tree structures.
3. **Connected Components**: Efficiently finds all connected components in a graph.
4. **Social Networks**: Used to find friends at a specific distance (e.g., "friends of friends").
5. **Web Crawling**: Explores web pages in breadth-first manner.
6. **Simple Implementation**: Easier to understand compared to DFS for many applications.

## How BFS Works

BFS uses a **queue** data structure to process nodes in a First-In-First-Out (FIFO) manner:

### Algorithm Steps:

1. **Initialize**: Create a queue and a visited set. Add the starting node to both.
2. **Dequeue**: Remove the front node from the queue.
3. **Process**: Add it to the traversal order.
4. **Explore Neighbors**: For each unvisited neighbor:
   - Mark it as visited
   - Add it to the queue
5. **Repeat**: Continue until the queue is empty.

### Example:

For the graph:
```
    0
   / \
  1   2
 / \ /
3   4
```

Starting from node 0:
- **Step 1**: Visit 0, queue: [0]
- **Step 2**: Process 0, add neighbors 1, 2, queue: [1, 2]
- **Step 3**: Process 1, add neighbors 3, 4, queue: [2, 3, 4]
- **Step 4**: Process 2, neighbors already visited, queue: [3, 4]
- **Step 5**: Process 3, no new neighbors, queue: [4]
- **Step 6**: Process 4, no new neighbors, queue: []

**Traversal Order**: [0, 1, 2, 3, 4]

## Time & Space Complexity

- **Time Complexity**: O(V + E)
  - V = number of vertices
  - E = number of edges
  
- **Space Complexity**: O(V)
  - Queue and visited set store at most V nodes

## Key Advantages

✅ Finds shortest path in unweighted graphs  
✅ Complete and optimal for unweighted cases  
✅ Simple to implement and understand  
✅ Efficient for sparse graphs  

## Key Disadvantages

❌ Requires more memory than DFS  
❌ Not suitable for finding longest paths  
❌ Less efficient for deep trees  

## Use Cases

- **GPS Navigation**: Finding shortest route
- **Social Media**: Finding mutual connections
- **Puzzle Solving**: Finding minimum moves to solve
- **AI Search**: Game state exploration
- **Network Broadcasting**: Message routing
