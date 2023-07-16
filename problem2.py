class LinkedList:
   
    class Node:
       

        def __init__(self, data):
           
            self.data = data
            self.next = None

    def __init__(self):
        
        self.head = None
        self.tail = None

    def insert_head(self, value):
       
        new_node = LinkedList.Node(value)  
        
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
       
        else:
            new_node.next = self.head 
            self.head = new_node     

    def insert_tail(self, value):
        
        new_node = LinkedList.Node(value)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        
        else:

            self.tail.next = new_node 
            self.tail = new_node      

 
    
    def __iter__(self):
        
        curr = self.head  # Start at the begining since this is a forward iteration.
        while curr is not None:
            yield curr.data  # Provide (yield) each item to the user
            curr = curr.next # Go forward in the linked list
    
    def __str__(self):
        """
        Return a string representation of the linked list.
        """
        output = "linkedlist["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output

    def remove_node(self, nodes):
        curr_node = self.head
        index = 0
        while index != nodes:
            curr_node = curr_node.next
            index = index + 1
        curr_node.next = curr_node.next.next

    def remove_duplicates(self):

        if self.head == None:
            return
        else:
            curr = self.head
            nodes = 0
            while curr.next != None:
                    more_nodes = 0
                    index = curr.next
                    while index != None:
                        if curr.data == index.data:
                            self.remove_node(more_nodes+nodes-1)
                            print(curr.data)
                        index = index.next
                        more_nodes = more_nodes + 1
                    nodes = nodes + 1
                    curr = curr.next


ll = LinkedList()
ll.insert_tail(1)
ll.insert_head(2)
ll.insert_head(2)
ll.insert_head(2)
ll.insert_head(3)
ll.insert_head(4)
ll.insert_head(5)
ll.insert_tail(3)
ll.insert_tail(0)
ll.insert_tail(-1)
print(ll) # linkedlist[5, 4, 3, 2, 2, 2, 1, 3, 0, -1]
ll.remove_duplicates()
print(ll) # linkedlist[5, 4, 3, 2, 1, 0, -1]