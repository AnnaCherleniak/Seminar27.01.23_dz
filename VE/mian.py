from isOdd import isOdd

some_list = [1, 5, 2, 3, 4, 8, 10]
for i in range(len(some_list)):
    print(f'{some_list[i]} - {isOdd(some_list[i])}')