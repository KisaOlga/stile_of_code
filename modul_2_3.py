my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
numbers = len(my_list)
index = 0
print(my_list)
while index < numbers :
    if my_list[index] == 0:
        index = index + 1
        continue
    elif my_list[index] > 0:
        print(my_list[index])
        index = index + 1
    elif my_list[index] < 0:
        break






