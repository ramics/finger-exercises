import lib.Tree as tr
import lib.Queue as qu
import lib.Stack as st

def data_search(q, tree, value, show_progress = False):

    q.push(tree)

    while len(q) > 0:
        branch = q.pop()
        if branch is None:
            continue

        if show_progress:
            print branch.value,

        if branch.value == value:
            return True

        q.push(branch.left)
        q.push(branch.right)

    return False

def breadth_first_search(tree, value, show_progress=False):

    queue = qu.Queue()
    data_search(queue, tree, value, show_progress)

def depth_first_search(tree, value, show_progress=False):
 
    stack = st.Stack()
    data_search(stack, tree, value, show_progress)

def build_tree():
    """
    Build the binary tree in the animated example for breadth-first search.
    """

    # left and right separated for readability
    tree_left = tr.Tree('b', tr.Tree('e', tr.Tree('h')), tr.Tree('d'))
    tree_right = tr.Tree('e', tr.Tree('f'), tr.Tree('g'))
    return tr.Tree('a', tree_left, tree_right)


tree = build_tree()
breadth_first_search(tree, 'g', show_progress=True)
print
depth_first_search(tree, 'g', show_progress=True)


