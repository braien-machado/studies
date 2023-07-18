def binary_search(ordered_list, value):
    max = len(ordered_list) - 1
    min = 0
    iteration = 1

    while max >= min:
        middle = (max + min) // 2
        cur_value = ordered_list[middle]

        if (cur_value == value):
            return f'The value {value} is in position {middle}. Iterations needed: {iteration}.'

        if (cur_value < value):
            min = middle + 1
        else:
            max = middle - 1
    
        iteration += 1

    return f'{value} is not in the given list.'


example_list = [1,3,5,7,9]
print(binary_search(example_list, 1)) # iterations needed: 2
print(binary_search(example_list, 3)) # iterations needed: 3
print(binary_search(example_list, 5)) # iterations needed: 1
print(binary_search(example_list, 7)) # iterations needed: 2
print(binary_search(example_list, 9)) # iterations needed: 3
print(binary_search(example_list, -1)) # not found

print(binary_search(range(1, 4000000001), 4000000000)) # iterations needed: 32
