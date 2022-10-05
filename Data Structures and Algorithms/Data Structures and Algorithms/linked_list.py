class Node:
    """
    An object for storing a single node of a linked list
    model two attributes - data and the link to the next node in the list
    """

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data


class LinkedList:
    """
    singly linked list
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        returns the number of nodes in the list
        takes 0(n) time
        """
        current = self.head
        count = 0

        while current:  # or while current!= None:
            count += 1
            current = current.next_node
        return count

    def add(self, data):
        """
        adds new node containing data at head of the list
        takes 0(1) time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        search for the first node containing data that matches the key
        returns the node or "None" if not found
        takes 0(n) time
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        """
        insert a new node containing data at index position
        insertion takes 0(1) time but finding the node at the
        insertion point takes 0(n) time
        takes overall 0(n) time
        """
        if index == 0:
            self.add(data)
        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = node.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):
        """
        removes nodes containing data that matches the key
        returns the node or "none" if the key doesn't exist
        takes 0(n) time
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current == self.head:  # or current is self.head
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

            return current
        
    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0
            
            while position < index:
                current = current.next_node
                position += 1
            return current

    def __repr__(self):
        """
        returns a string representation of the list
        takes 0(n) time
        """
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return "->".join(nodes)
