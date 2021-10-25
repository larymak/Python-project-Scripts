from linked_list import LinkedList


def merge_sort(linked_list):
    """
    sorts a linked list in ascending order
    - recursively divides the linked list into sublist containing a single node
    - repeatedly merge the sublist to produce sorted sublists until one remains
    return a sorted linked list

    runs in O(kn log n) time
    """
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.size() is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(linked_list):
    """
    divide the unsorted list at the midpoint into sublists
    takes O(k log n) time
    """
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None
        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size // 2

        mid_node = linked_list.node_at_index(mid - 1)
        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half


def merge(left, right):
    """
    merges two linked lists, sorting data in nodes
    return a new, merged list
    takes O(n) time
    """

    # create a new linked list that contains node from
    # mergin left and right
    merged = LinkedList()

    # add a fake head that is discarded later
    merged.add(0)
    # set current to head of linked list
    current = merged.head
    # obtain head node for left and right linked list
    left_head = left.head
    right_head = right.head
    # iterate over the left and right until we reach the tail node of either
    while left_head or right_head:
        # if the head node of the left is none, we are past the tail
        # add the node from the right to the merged linked list
        if left_head is None:
            current.next_node = right_head
            # call next on right to set loop condition to false
            right_head = right_head.next_node
            # if the head node of right is none, we are past the tail
            # add the tail node from the left to merged linked list
        elif right_head is None:
            current.next_node = left_head
            # call next on left to set loop condition to false
            left_head = left_head.next_node
        else:
            # not at either tail node
            # obtain node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data
            # if data on the left is less than right, set current to left node
            if left_data < right_data:
                current.next_node = left_head
                # move left head to next node
                left_head = left_head.next_node
            # if data on the left is greater than right, set current to right node
            else:
                current.next_node = right_head
                # move right head to next node
                right_head = right_head.next_node

        # move current to next node
        current = current.next_node

    # discard the fake head and set the first merged node as head
    head = merged.head.next_node
    merged.head = head

    return merged


l = LinkedList()
l.add(10)
l.add(2)
l.add(44)
l.add(15)
l.add(200)

print(l)
sorted_linked_list = merge_sort(l)
print(sorted_linked_list)
