import re
def friend(x):
    b = []
    for y in x:
        b.append(re.findall("^[a-zA-Z]{4}$", y))
    return b
print(friend(["Ryan"]))