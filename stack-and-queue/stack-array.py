def create_stack():
    stack = []
    return stack


def is_empty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)
    return stack




stack1 = create_stack()
print(push(stack1, 0))