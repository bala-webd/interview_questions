def is_set_can_be_partitioned(sets=None):
    if sets is None:
        sets = []
    total = sum_array(sets)
    result = total % 2 == 0
    if total % 2 == 0: # To determine whether it can be split by two sets.
        partition_value = total // 2

        partitioned_set_one = []
        partitioned_set_two = []

        for index in range(len(sets)):
            if not partitioned_set_one:
                partitioned_set_one.append(sets[index])
            elif sum(partitioned_set_one) < partition_value:
                partitioned_set_one.append(sets[index])
            elif sum(partitioned_set_one) > partition_value:
                partitioned_set_two.append(partitioned_set_one.pop())
                partitioned_set_two.append(sets[index])
                if sum(partitioned_set_two) > partition_value:
                    partitioned_set_one.append(partitioned_set_two.pop())
        return f'Output is {result} and the sets are ' \
               f'Set ONE: {partitioned_set_one}' \
               f'Set TWO: {partitioned_set_two} '
    return f'Output is {result}'

def sum_array(array=None):
    total = 0
    for num in array:
        total += num
    return total


print(is_set_can_be_partitioned([1,6,8,3,4]))
