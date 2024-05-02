import random


def first_num():
    numbers = range(3,21)
    rock = random.choice(numbers)
    return rock


rock = first_num()
print(rock)

result = []

for i in range(1, rock):
    for k in range(1, rock):
        sum = i + k
        if i == k:
            continue
        if rock % sum == 0:
            list_3 = [i, k]
            if [k, i] in result:
                continue
            result.append(list_3)

print(*result)

