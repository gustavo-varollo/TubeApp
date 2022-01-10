class Node:
    """
        Class that start the nodes
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """
        Class taking care of the Doubly Linked List and its functions
    """
    def __init__(self):
        self.head = None

    def append(self, data):
        """
            function that append data to the nodes
        """
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    def prepend(self, data):
        """
            function that prepend data to the nodes
        """
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def clean_list(self):
        """
            function that remove the data of all nodes
        """
        if self.head is None:
            print("The list has no element")
            return
        cur = self.head
        while cur:
            cur.data = None
            cur = cur.next
        # if cur.next is not None:
        #     cur.prev.next = None

    def print_list(self):
        """
            function that print the whole list
        """
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def return_data_for_alg(self):
        """
            function that return specific data used for the algorithm calculation
        """
        cur = self.head
        x =[]
        while cur != None:
            x.append([cur.data[1], cur.data[2], cur.data[3]])
            cur = cur.next
        return x

    def return_all_data(self):
        """
            function that return all the data in the list
        """
        cur = self.head
        x = []
        while cur != None:
            x.append([cur.data[0], cur.data[1], cur.data[2], cur.data[3]])
            cur = cur.next
        return x

    def return_sorted_data(self):
        """
            function that return all the data in the list in a sorted format
        """
        cur = self.head
        x =[]
        while cur != None:
            x.append(cur.data)
            cur = cur.next
        x.sort()
        return x

    def n_data(self, x):
        """
            function that check if the list have the value of a specific node and return a boolean value
        """
        cur = self.head
        while cur != None:
            if cur.data == x:
                return True
            cur = cur.next
        return False