def reverse_linked_list(head): # space complexity: O(n)
    if head is None:
        return None
    if head.next is None:
        return head
    reverse_node_stack = []
    while head is not None:
        reverse_node_stack.append(head)
        head = head.next

    for node in reverse_node_stack:
        node.next = None
    last_stack_node = reverse_node_stack.pop(-1)
    reversed_head = last_stack_node
    current_node = reversed_head
    while reverse_node_stack:
        last_stack_node = reverse_node_stack.pop(-1)
        current_node.next = last_stack_node
        current_node = current_node.next
    return reversed_head
