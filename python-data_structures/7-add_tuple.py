def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure each tuple has at least 2 elements by adding (0, 0) as defaults
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)
    
    # Use only the first two elements from each tuple
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
