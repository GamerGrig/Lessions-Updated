list_ = ["BMW", "MB", "LADA", "KIA", "HONDA"]
cars_count = 0
for i in list_:
    print('Я езжу на автомобиле марки ' + i)
    for k in range(len(list_)):
        cars_count += 10
        print(cars_count)