class Stack:
    # Stack Data Stracture
    def __init__(self):
        # Initialize empty list
        self.items = [] 
    def push(self, x):
        # Append an element to the list
        self.items.append(x)
    def pop(self, x):
        # Pop top element from the list
        self.items.pop()
    def is_empty(self):
        # Return true if stack is empty
        return len(self.items)
    def peek(self):
        # Peek top of stuck
        return self.items[-1]
    def size(self):
        # Return size of stack
        return len(self.items)
    def clear(self):
        # Clears stuck
        self.items = []