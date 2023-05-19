def create_stack():
    stack = []
    return stack


def is_empty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)
    return stack


def pop(stack):
    if is_empty(stack):
        return None
    stack.pop()
    return stack


stack1 = create_stack()
print(push(stack1, 0))
print(push(stack1, 1))
print(push(stack1, 2))
print(push(stack1, 3))
print(pop(stack1))