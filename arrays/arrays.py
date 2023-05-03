def  access(list, index):
    elem = list[index]
    return elem

def search(list, target):
    if target in list:
        return True
    return False

def insert(list, index, value):
    if index == len(list):
        list.append(value)
        return True
    
    list.append(None)
    for i in range(len(list) - 1, index, -1):
        list[i] = list[i - 1]
    
    list[index] = value
    return True

my_list = [1,2,3,4]

result = access(my_list, 3)
print(result)

result = search(my_list, 2)
print(result)

insert(my_list, 4, 10)
print(my_list)

insert(my_list, 2, 10)
print(my_list)