class SortedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0  # Keeps track of the number of elements

    def insert(self, data):
        """Inserts data in sorted order. O(n) complexity."""
        new_node = self.Node(data)
        
        if self.front is None:  # Empty list case (O(1))
            self.front = self.back = new_node
        else:
            curr = self.front
            prev = None
            while curr and curr.data < data:  # Searching for the correct position (O(n))
                prev = curr
                curr = curr.next
            
            if curr == self.front:  # Insert at the front (O(1))
                new_node.next = self.front
                self.front.prev = new_node
                self.front = new_node
            elif curr is None:  # Insert at the back (O(1))
                self.back.next = new_node
                new_node.prev = self.back
                self.back = new_node
            else:  # Insert in the middle (O(n))
                prev.next = new_node
                new_node.prev = prev
                new_node.next = curr
                curr.prev = new_node
        
        self.size += 1

    def remove(self, data):
        """Removes a node with the given data. O(n) complexity."""
        curr = self.front
        while curr and curr.data != data:  # Searching for the node to remove (O(n))
            curr = curr.next
        
        if curr is None:  # Data not found (O(1))
            return False
        
        if curr == self.front:  # Remove from front (O(1))
            self.front = curr.next
            if self.front:
                self.front.prev = None
        elif curr == self.back:  # Remove from back (O(1))
            self.back = curr.prev
            if self.back:
                self.back.next = None
        else:  # Remove from middle (O(n))
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
        
        self.size -= 1
        return True

    def is_present(self, data):
        """Returns True if data is present in the list, otherwise False. O(n) complexity."""
        curr = self.front
        while curr:
            if curr.data == data:
                return True  # Found (O(1))
            elif curr.data > data:
                return False  # Since it's sorted, stop early (O(n) worst case)
            curr = curr.next
        return False

    def __len__(self):
        """Returns the number of elements in the list. O(1) complexity."""
        return self.size

    def __iter__(self):
        """Allows forward iteration through the list. O(n) complexity."""
        curr = self.front
        while curr:
            yield curr.data
            curr = curr.next

    def __reversed__(self):
        """Allows backward iteration through the list. O(n) complexity."""
        curr = self.back
        while curr:
            yield curr.data
            curr = curr.prev

# Testing the SortedList
if __name__ == "__main__":
    sl = SortedList()
    sl.insert(10)
    sl.insert(5)
    sl.insert(30)
    sl.insert(20)
    sl.insert(2)
    
    print("List after insertions:", list(sl))
    
    sl.remove(10)
    print("List after removing 10:", list(sl))
    
    print("Is 30 present?", sl.is_present(30))
    print("Is 15 present?", sl.is_present(15))
    
    print("List in reverse:", list(reversed(sl)))