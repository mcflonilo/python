def find_outlier(integers):
    is_even = [num % 2 == 0 for num in integers]
    is_even_count = is_even.count(True)
    return integers[is_even.index(False)] if is_even_count > 1 else integers[is_even.index(True)]


find_outlier([2, 4, 6, 8, 10, 3]) # 3