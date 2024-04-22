def scramble(s1, s2):
    char_count = {}
    for char in s1:
        char_count[char] = char_count.get(char, 0) + 1
    for char in s2:
        if char_count.get(char, 0) <= 0:
            return False
        char_count[char] -= 1
    return True

print(scramble('rkqodlw', 'world'))  # True

def scramble(s1,s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True