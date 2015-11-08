import operator

__author__ = 'Timmmmeh'
class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.insert(0, item)
    def pop(self):
        return self.items.pop(0)
    def peek(self):
        return self.items[0]
    def size(self):
        return len(self.items)
s = Stack()
operators = {"+": operator.add, "-":operator.sub, "*":operator.mul, "/":operator.div}
print("Enter the Polish notation equation you want solved in this notation: 76 43 +")
equation = raw_input("")
equation = equation.split(" ")
for i in range(len(equation)):
    if equation[i] in operators:
        two = s.pop()
        one = s.pop()
        new_value = operators[equation[i]](one, two)
        s.push(new_value)
    else:
        s.push(int(equation[i]))
print s.pop()