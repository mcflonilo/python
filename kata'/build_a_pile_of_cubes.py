def find_nb(m):
    
    n = 1
    sum = 0
    while sum < m:
        sum += n**3
        if sum == m:
            return n
        n += 1
    return -1
    
print(find_nb(4)) # 2022