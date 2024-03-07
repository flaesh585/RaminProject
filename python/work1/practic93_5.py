list1 = [8, 9, 148, 4]
list2 = [9, 1, 33, 83]
list3 = list()

for i in list1:
    for j in list2:
        list3.append(i * j)

print(list3)