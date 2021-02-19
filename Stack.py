class Stack:
    def __init__(self):
        self.items = []
        self.size = 0

    def empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def push(self, data):  # O(1)
        self.items.append(data)
        self.size += 1

    def pop(self):  # O(1)
        if not self.empty():
            self.size -= 1
            return self.items.pop()
        else:
            raise Exception('Stack is empty')

    def peek(self):  # O(1)
        if not self.empty():
            return self.items[self.size - 1]
        else:
            raise Exception('Stack is empty')

    def __str__(self):
        return str(self.items)
