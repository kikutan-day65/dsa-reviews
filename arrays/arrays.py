def  access_elem(list, index):
    elem = list[index]
    return elem

int_list = [1,2,3,4]
char_list = ['a', 'b', 'c', 'd']

result = access_elem(int_list, 3)
print(result)

result = access_elem(char_list, 0)
print(result)
