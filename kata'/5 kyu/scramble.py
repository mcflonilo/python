def scramble(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    for i in s2:
        if i in s1:
            s1.remove(i)
        else:
            return False
    return True

print (scramble('rkqodlw', 'world')) # True