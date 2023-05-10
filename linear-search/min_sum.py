def find_min_sum(list1, list2):
    min_sum = 20000000
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] + list2[j] <= min_sum:
                min_sum = list1[i] + list2[j]
    return min_sum

mylist1 = [1,2,3,4]
mylist2 = [1,2,3,4]
result = find_min_sum(mylist1, mylist2)
print(result)

mylist1 = [10,9,8,7,6,5,4,3,2]
mylist2 = [10,9,8,7,6,5,4,3,2]
result = find_min_sum(mylist1, mylist2)
print(result)