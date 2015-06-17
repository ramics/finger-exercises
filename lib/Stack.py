class Stack:

    def __init__(self):
        self.values = []

    def __getitem__(self, index):
        return self.values[index]

    def __len__(self):
        return len(self.values)

    def push(self, value):
        self.values.append(value)

    def pop(self):
        return self.values.pop()
