def max_integer(my_list=[]):
    if not my_list:  # Check if the list is empty
        return None
    max_value = my_list[0]  # Assume the first element is the largest
    for num in my_list:
        if num > max_value:  # Compare each element with the current max
            max_value = num
    return max_value
