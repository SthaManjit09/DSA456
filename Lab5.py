class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self, capacity):
        self.top = None
        self.capacity = capacity
        self.size = 0

    def push(self, n):
        if self.isFull():
            raise Exception("Stack is full")
        new_node = Node(n)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        popped_value = self.top.data
        self.top = self.top.next
        self.size -= 1
        return popped_value

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.top is None

    def stack_size(self):
        return self.size

class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, n):
        if self.isFull():
            raise Exception("Queue is full")
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = n
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        dequeued_value = self.queue[self.front]
        self.queue[self.front] = None  # Optional: Clear the value
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return dequeued_value

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    def queue_size(self):
        return self.size

# Example usage:
if __name__ == "__main__":
    stack = Stack(5)  # Stack with capacity of 5
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Popped element:", stack.pop())  # Output: 30
    print("Stack size:", stack.stack_size())  # Output: 2
    print("Is stack empty?", stack.isEmpty())  # Output: False

    queue = Queue(5)  # Queue with capacity of 5
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("Dequeued element:", queue.dequeue())  # Output: 1
    print("Queue size:", queue.queue_size())  # Output: 2
    print("Is queue empty?", queue.isEmpty())  # Output: False
