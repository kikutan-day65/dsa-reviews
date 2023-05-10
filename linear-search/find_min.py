def find_min(mylist):
    min_value = mylist[0]
    for i in range(len(mylist)):
        if mylist[i] < min_value:
            min_value =  mylist[i]
    return min_value

int_list = [23,54,12,57,88,61]
result = find_min(int_list)
print(result)

int_list = [23,54,12,57,88,61,-11,-4,-15]
result = find_min(int_list)
print(result)