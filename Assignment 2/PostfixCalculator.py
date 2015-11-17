import operator
__author__ = 'Timmmmeh'

#stack from the internet
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
#if any operators are called run the right method
operators = {"+": operator.add, "-":operator.sub, "*":operator.mul, "/":operator.div}
print("Enter the Polish notation equation you want solved")
equation = raw_input("")
#split the equation into the right parts
equation = equation.split(" ")
for i in range(len(equation)):
    if equation[i] in operators:
        #rearange the values that come of first so it does devision/ subtracting right
        two = s.pop()
        one = s.pop()
        #do the equation
        new_value = operators[equation[i]](one, two)
        #push the new value onto the stack
        s.push(new_value)
    else:
        s.push(int(equation[i]))
print s.pop()