#!/usr/bin/env python3
# graph_traverse.py
# Glenn G. Chappell
# Started: 2026-11-22
# Updated: 2026-11-23
"""Graph traversals: DFS & BFS.
For CS 311 Fall 2026
"""


import collections  # For .deque
import bisect       # For .bisect_left


# CONVENTIONS

# A GRAPH, in this program, is finite and simple; that is, there is no
# edge from a vertex to itself, and each pair of vertices has at most
# one edge joining them.
#
# We use V for the number of vertices in a graph. Vertices are numbered
# 0 .. V-1.
#
# A graph is represented by adjacency lists. Adjacency lists are stored
# in a list of size V, each item of which is a list. Item #i a list of
# the neighbors of vertex i, in ascending order.
#
# To create a graph represented by adjacency lists, call function
# empty_adj_lists to create a new edgeless graph. Then call function
# add_edge for each edge the graph.

# A traversal of a graph is printed as a list of vertex indices (each an
# integer in 0 .. V-1) separated by blanks.


def dfs_helper(adj_lists, start, visited):
    """Given a graph, start vertex, and vertex-visited data, print DFS
    of unvisited vertices reachable from start vertex.

    Parameters:
    * adj_lists - Adjacency lists for a graph, formatted as described
      above.
    * start - Index (0 .. V-1) of the start vertex.
    * visited - List of bool, size V. visited[i] is True if vertex i has
      been visited. The altered version of this list, with visited
      vertices marked as such, is available to the caller.
    """

    assert isinstance(adj_lists, list)
    assert isinstance(start, int)
    assert 0 <= start < len(adj_lists)
    assert isinstance(visited, list)
    assert len(visited) == len(adj_lists)

    s = []           # Stack holding vertices to visit

    s.append(start)  # Push start vertex

    while s:            # Loop while Stack is nonempty
        # Get next vertex
        curr = s.pop()  # Pop Stack

        # Make sure it is unvisited
        if visited[curr]:
            continue

        # Visit it
        print(f"{curr} ", end="")
        visited[curr] = True

        # And push its unvisited neighbors
        # Do this in reverse order, so we pop lower numbers first.
        # Note that *reversed* does not make a copy of the list.
        for nbr in reversed(adj_lists[curr]):
            if not visited[nbr]:
                s.append(nbr)


def dfs(adj_lists):
    """Given a graph, print a DFS (no ending newline).

    Parameters:
    * adj_lists - Adjacency lists for a graph, formatted as described
      above.
    """

    assert isinstance(adj_lists, list)

    # Set up visited array
    V = len(adj_lists)
    visited = [ False for _ in adj_lists ]

    # Try DFS starting at each vertex
    # visited is modified by dfs_helper call. Modified version is passed
    # to the next call, and so on.
    for start in range(V):
        dfs_helper(adj_lists, start, visited);


def bfs_helper(adj_lists, start, visited):
    """Given a graph, start vertex, and vertex-visited data, print BFS
    of unvisited vertices reachable from start vertex.

    Parameters:
    * adj_lists - Adjacency lists for a graph, formatted as described
      above.
    * start - Index (0 .. V-1) of the start vertex.
    * visited - List of bool, size V. visited[i] is True if vertex i has
      been visited. The altered version of this list, with visited
      vertices marked as such, is available to the caller.
    """

    assert isinstance(adj_lists, list)
    assert isinstance(start, int)
    assert 0 <= start < len(adj_lists)
    assert isinstance(visited, list)
    assert len(visited) == len(adj_lists)

    q = collections.deque()  # Queue holding vertices to visit

    q.append(start)  # Enqueue start vertex

    while q:            # Loop while Queue is nonempty
        # Get next vertex
        curr = q.popleft()  # Dequeue

        # Make sure it is unvisited
        if visited[curr]:
            continue

        # Visit it
        print(f"{curr} ", end="")
        visited[curr] = True

        # And enqueue its unvisited neighbors
        for nbr in adj_lists[curr]:
            if not visited[nbr]:
                q.append(nbr)


def bfs(adj_lists):
    """Given a graph, print a BFS (no ending newline).

    Parameters:
    * adj_lists - Adjacency lists for a graph, formatted as described
      above.
    """

    assert isinstance(adj_lists, list)

    # Set up visited array
    V = len(adj_lists)
    visited = [ False for _ in adj_lists ]

    # Try BFS starting at each vertex
    # visited is modified by bfs_helper call. Modified version is passed
    # to the next call, and so on.
    for start in range(V):
        bfs_helper(adj_lists, start, visited);


def print_traversals(adj_lists):
    """Given a graph, print a DFS and BFS.

    Parameters:
    * adj_lists - Adjacency lists for a graph, formatted as described
      above.
    """

    assert isinstance(adj_lists, list)

    print("DFS: ", end="")
    dfs(adj_lists)
    print()

    print("BFS: ", end="")
    bfs(adj_lists)
    print()


def empty_adj_lists(V):
    """V -> adjacency lists for empty graph with V vertices.

    The idea is that this function is called to create an empty graph,
    and then add_edge is called to add each edge. Thus, any finite graph
    can be constructed.

    Parameters:
    * V - Number of vertices in graph to construct.
    """

    assert isinstance(V, int)
    assert V >= 0

    return [ [] for _ in range(V) ]


def add_edge(adj_lists, a, b):
    """Adds edges a - b to given graph.

    The idea is that empty_adj_lists is called to create an empty graph,
    and this this function is called to add each edge. Thus, any finite
    graph can be constructed.

    Parameters:
    * adj_lists - Adjacency lists for a graph, formatted as described
      above.
    * a - One endpoint of edge to add.
    * b - The other endpoint of edge to add.
    """

    assert isinstance(adj_lists, list)
    assert isinstance(a, int)
    assert 0 <= a < len(adj_lists)
    assert isinstance(b, int)
    assert 0 <= b < len(adj_lists)
    assert a != b

    # Insert b in adj list for vertex a; find spot with Binary Search.
    insert_pt = bisect.bisect_left(adj_lists[a], b)
    assert insert_pt == len(adj_lists[a]) or adj_lists[a][insert_pt] != b
    adj_lists[a].insert(insert_pt, b)

    # Insert a in adj list for vertex b; find spot with Binary Search.
    insert_pt = bisect.bisect_left(adj_lists[b], a)
    assert insert_pt == len(adj_lists[b]) or adj_lists[b][insert_pt] != a
    adj_lists[b].insert(insert_pt, a)


def make_adj_lists_tree():
    """Return adjacency lists for a particular tree.

    Graph: tree.
    7 vertices: 0 .. 6.
    Adjacencies: 0 - 1, 0 - 2
                 1 - 5, 1 - 6
                 2 - 3, 2 - 4
    """

    V = 7
    adj_lists = empty_adj_lists(V)

    add_edge(adj_lists, 0, 1)
    add_edge(adj_lists, 0, 2)
    add_edge(adj_lists, 1, 5)
    add_edge(adj_lists, 1, 6)
    add_edge(adj_lists, 2, 3)
    add_edge(adj_lists, 2, 4)

    return adj_lists


def make_adj_lists_cycle():
    """Return adjacency lists for an 8-cycle.

    Graph: 8-cycle.
    8 vertices: 0 .. 7.
    Adjacencies: 0 - 1 - 2 - 3 - 4 - 5 - 6 - 7 - 0
    """

    V = 8
    adj_lists = empty_adj_lists(V)

    for i in range(V):
        add_edge(adj_lists, i, (i+1)%V)

    return adj_lists


def make_adj_lists_double_path():
    """Return adjacency lists for two random-ish 5-paths.

    Graph: two 5-paths
    10 vertices: 0 .. 9.
    Adjacencies: 3 - 5 - 0 - 1 - 8
                 7 - 2 - 4 - 9 - 6
    """

    V = 10
    adj_lists = empty_adj_lists(V)

    add_edge(adj_lists, 3, 5)
    add_edge(adj_lists, 5, 0)
    add_edge(adj_lists, 0, 1)
    add_edge(adj_lists, 1, 8)
    add_edge(adj_lists, 7, 2)
    add_edge(adj_lists, 2, 4)
    add_edge(adj_lists, 4, 9)
    add_edge(adj_lists, 9, 6)

    return adj_lists


def user_pause(msg):
    """Print given message and wait for user to press ENTER."""

    assert isinstance(msg, str)

    print("", end="", flush=True)
    _ = input(msg)


# Main program
# Do DFS & BFS on various graphs, printing results.

if __name__ == "__main__":
    # Opening Message
    print("Graph Traversals")

    # Traversals: Tree
    print()
    print("Tree")
    adj_lists = make_adj_lists_tree()
    print_traversals(adj_lists)

    # Traversals: Cycle
    print()
    print("8-Cycle")
    adj_lists = make_adj_lists_cycle()
    print_traversals(adj_lists)

    # Traversals: Two Paths
    print()
    print("Two 5-Paths")
    adj_lists = make_adj_lists_double_path()
    print_traversals(adj_lists)

    # Wait for user
    print()
    user_pause("Press ENTER to quit ")

