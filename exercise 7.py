def find_max_min_avg(lst):
    if not lst:
        return None

    max_val = lst[0]
    min_val = lst[0]
    sum_val = 0

    for num in lst:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
        sum_val += num

    avg_val = sum_val / len(lst)

    return max_val, min_val, avg_val

# Example usage
my_list = [5, 10, 15, 20, 25]
max_val, min_val, avg_val = find_max_min_avg(my_list)
print("Maximum:", max_val)
print("Minimum:", min_val)
print("Average:", avg_val)
