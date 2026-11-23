#!/usr/bin/env python3
# graph_traverse.py  UNFINISHED
# Glenn G. Chappell
# 2026-11-22
"""Graph traversals: DFS.
For CS 311 Fall 2026
"""


import bisect       # For .bisect_right


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


def dfs(adj_lists):
    """Given a graph, print a DFS (no ending newline).

    Parameters:
    * adj_lists - Adjacency lists for a graph, formatted as described
      above.
    """

    print("<NOT WRITTEN>", end="")  # Dummy
    # TODO: WRITE THIS!!!


def print_traversals(adj_lists):
    """Given a graph, print a DFS.

    Parameters:
    * adj_lists - Adjacency lists for a graph, formatted as described
      above.
    """

    assert isinstance(adj_lists, list)

    print("DFS: ", end="")
    dfs(adj_lists)
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

    # Insert b in adj list for vertex a; find spot with Binary Search.
    insert_pt = bisect.bisect_right(adj_lists[a], b)
    adj_lists[a].insert(insert_pt, b)

    # Insert a in adj list for vertex b; find spot with Binary Search.
    insert_pt = bisect.bisect_right(adj_lists[b], a)
    adj_lists[b].insert(insert_pt, a)


def make_adj_lists_tree():
    """Return adjacency lists for a particular tree.

    Graph: tree.
    7 vertices: 0 .. 6.
    Adjacencies: 0 - 1, 0 - 2
                 1 - 3, 1 - 4
                 2 - 5, 2 - 6
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
# Do DFS on various graphs, printing results.

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

