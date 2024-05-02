import random


def first_num():
    numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    num = random.choice(numbers)
    return num


num = first_num()
print(num)

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
result = []
for i in list_1:
    for k in list_2:
        sum = i + k
        if sum % num == 0:
            list_3 = [i,k]
            result.extend(list_3)
print(*result)



