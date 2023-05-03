def  access(list, index):
    elem = list[index]
    return elem

def search(list, target):
    if target in list:
        return True
    return False

int_list = [1,2,3,4]
char_list = ['a', 'b', 'c', 'd']

result = access(int_list, 3)
print(result)

result = access(char_list, 0)
print(result)

result = search(int_list, 2)
print(result)

result = search(char_list, 'x')
print(result)