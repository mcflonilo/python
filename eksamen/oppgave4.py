import random
def substitute(list):
    for i in range(len(list)):
        temp = list[i]
        if temp % 5 == 0:
            list[i] = list[i]*list[i]
    return list

random_integers = []
for i in range(10):
    random_integers.append(random.randint(1, 50))  
print(random_integers)
random_integers = substitute(random_integers)
print(random_integers)

