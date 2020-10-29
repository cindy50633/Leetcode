def get_max_depth(root):
    if not root:
        return 0
    # DFS
    return max(get_max_depth(root.left), get_max_depth(root.right)) + 1
