def find_outlier(integers):
    is_even = [num % 2 == 0 for num in integers]
    print(is_even)
    
    return None

find_outlier([2, 4, 6, 8, 10, 3]) # 3