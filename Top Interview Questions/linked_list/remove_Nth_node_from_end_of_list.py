def remove_Nth_from_end(head, n):
    if head.next is None:
        return None
    prev_node = ListNode(val=0, next=head)
    current_node = head
    interval_node = 0

    while current_node is not None:
        current_node = current_node.next
        interval_node += 1
        if interval_node == n+1:
            prev_node = prev_node.next
            interval_node = n
    if prev_node.next == head:
        return head.next
    prev_node.next = prev_node.next.next
    return head
