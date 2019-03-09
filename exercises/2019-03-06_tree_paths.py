"""
Question: For a given binary tree, write a function to return all root-to-leaf paths.
We'll use the tree below to walk through how your code should work.
"A" is the root, and "D" would be considered the leaf in the path A -> B -> D.
The expectation for your function is to return all root to leaf combinations.
The output of your code, given the tree below, would be:
["A -> B -> D", "A -> C"]
"""
from collections import namedtuple

# define a tree node. Get via Node.val, Node.left, etc
Node = namedtuple('Node', ['val', 'left', 'right'])


def get_paths(tree):
    """ return all paths from root to leaves, concatenating node values """
    def f(s, n):
        if not n:  # empty leaf
            return []
        elif not n.left and not n.right:  # value leaf
            return [s + n.val]
        else:
            return f(s + n.val, n.left) + f(s + n.val, n.right)
    return f('', tree)


def test_get_paths():
    # tree:
    #   a
    # b   c
    # d
    tree = Node(
        'a',
        Node(
            'b',
            Node('d', None, None),
            None
        ),
        Node('c', None, None)
    )
    assert get_paths(tree) == ['abd', 'ac']


test_get_paths()
