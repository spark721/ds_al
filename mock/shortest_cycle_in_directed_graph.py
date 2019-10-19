
# Find a shortest cycle(in-order) that involves a given target node in a directed graph.
# Value of the nodes may be duplicate.

# Example:

#                 13  ->  23
#                 ^       ^
#                 |       |
# 
#         19  ->  2   ->  4   ->  7
#            <       <               
#             \   |   \   |   /   |
#                 <       <  <    < 
#                23   <-  X   -   19
# 
#                     \   |       |
#                      >  <       < 
#                         11      13


# Definition for graph-node
# class GraphNode:
#     def __init__(self, val):
#         self.val = val
#         self.outNodes: list = []


def shortest_cycle(target_node):
    '''
    init best_path
    init cur_path
    init seen set

    start dfs(node, path, seen)
        add node to the path and seen
        if target in outNodes:
            compare and update best_path
        loop thru outNodes
            on each nextNode
            if not seen and not target:
                dfs(nextNode, cur_path, cur_seen)

    invoke dfs(target_node, cur_path, seen)
    return best_path
    '''
