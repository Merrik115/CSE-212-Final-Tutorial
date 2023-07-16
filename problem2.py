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
