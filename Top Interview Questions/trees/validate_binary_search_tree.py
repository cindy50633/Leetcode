def is_valid_bfs(root):
    def __validate_node(node, min_val, max_val):
        if not node:
            return True
        if node.val <= min_val or node.val >= max_val:
            return False
        return __validate_node(node.left, min_val, node.val) and __validate_node(node.right, node.val, max_val)
    return __validate_node(root, -float('inf'), float('inf'))
