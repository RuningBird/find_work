class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, element):
        self.stack1.append(element)

    def make_stack2(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())

    def restore_stack1(self):
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def top(self):
        self.make_stack2()
        if not self.stack2:
            return None
        value = self.stack2[-1]
        self.restore_stack1()
        return value

    def pop(self):
        self.make_stack2()
        if not self.stack2:
            return None
        value = self.stack2.pop()
        self.restore_stack1()
        return value


q = MyQueue()

q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.push(5)

print(q.pop())
print(q.pop())
print(q.stack2)
q.push(6)
q.push(7)
q.push(8)
q.push(9)
print(q.pop())
print(q.pop())
