def  access(list, index):
    elem = list[index]
    return elem

def search(list, target):
    if target in list:
        return True
    return False

my_list = [1,2,3,4]

result = access(my_list, 3)
print(result)

result = search(my_list, 2)
print(result)