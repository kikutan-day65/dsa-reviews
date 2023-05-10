def find_num(mylist, target):
    flag = False
    for i in range(len(mylist)):
        if mylist[i] == target:
            flag = True
            return flag
    return flag

int_list = [1,2,3,4,5,6,7,8,9,10]
result = find_num(int_list, 5)
print(result)

int_list = [1,2,3,4,5,6,7,8,9,10]
result = find_num(int_list, 11)
print(result)