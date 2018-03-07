from queue import LifoQueue

class StackUnderflowError(Exception):
    def __init__(self, message):
        super().__init__(message)

def check_size(stack, size):
    if stack.qsize() < size:
        raise StackUnderflowError("Stack does not contain enough values for required pop")

def dup(stack):
    check_size(stack, 1)

    v = stack.get()
    stack.put(v); stack.put(v)
    return stack

def drop(stack):
    check_size(stack, 1)
    
    stack.get()
    return stack

def swap(stack):
    check_size(stack, 2)
    
    a = stack.get()
    b = stack.get()

    stack.put(a)
    stack.put(b)

    return stack

def over(stack):
    check_size(stack, 2)
    
    a = stack.get()
    b = stack.get()

    stack.put(b)
    stack.put(a)
    stack.put(b)

    return stack

def add(stack):
    check_size(stack, 2)

    a = stack.get()
    b = stack.get()

    stack.put(a + b)

    return stack

def subtract(stack):
    check_size(stack, 2)

    a = stack.get()
    b = stack.get()

    stack.put(b - a)

    return stack

def multiply(stack):
    check_size(stack, 2)

    a = stack.get()
    b = stack.get()

    stack.put(a * b)

    return stack

def divide(stack):
    check_size(stack, 2)

    a = stack.get()
    b = stack.get()

    stack.put(b // a)

    return stack

ops = {
    '+': add, '-': subtract, '*': multiply, '/': divide,
    'dup': dup, 'drop': drop, 'swap': swap, 'over': over
}
    
def stack_to_list(stack):
    elements = []
    while stack.qsize():
        elements.append(stack.get())

    return elements[::-1]

def execute(item, stack):
    if item.isnumeric():
        stack.put(int(item))

    elif item in ops:
        stack = ops[item](stack)

    else:
        raise ValueError("Unexpected item: {}".format(item))

    return stack

def evaluate(input_data):

    stack = LifoQueue()
    custom_ops = {}

    for line in input_data:

        line = line.lower().split(' ')

        if line[0] == ':' and line[-1] == ';': # define word
            if not line[1].isnumeric():
                custom_ops[line[1]] = line[2:-1]

            else:
                raise ValueError("Got fully numerical word-name")

        else:
            for item in line:
                if item in custom_ops: # replace with custom op expression:
                    for op in custom_ops[item]:
                        stack = execute(op, stack)
                
                else:
                    stack = execute(item, stack)

    return stack_to_list(stack)
    
