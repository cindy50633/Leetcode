def is_symmetric_tree(root):
    if not root:
        return True
    def is_symmetric_helper(left_tree_root, right_tree_root):
        if bool(left_tree_root) ^ bool(right_tree_root):
            return False
        if left_tree_root and right_tree_root:
            if left_tree_root.val == right_tree_root.val:
                return is_symmetric_helper(left_tree_root.left, right_tree_root.right) and is_symmetric_helper(left_tree_root.right, right_tree_root.left)
            else:
                return False
        return True
    return is_symmetric_helper(root.left, root.right)
