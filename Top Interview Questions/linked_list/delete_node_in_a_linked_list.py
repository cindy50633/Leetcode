def delete_node1(node):
    def delete_node_helper(node):
        tmp = None
        if not node.next.next:
            tmp = node.next.val
            node.next = None
        if node.next:
            node.val = node.next.val
            return delete_node_helper(node.next)
        if tmp is not None:
            node.val = tmp
    delete_node_helper(node)


def delete_node2(node):
    tmp = None
    if not node.next.next:
        tmp = node.next.val
        node.next = None
    if tmp is not None:
        node.val = tmp
        return
    if node.next:
        node.val = node.next.val
        return self.delete_node2(node.next)


def delete_node3(node):
    node.val = node.next.val
    node.next = node.next.next
