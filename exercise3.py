

string = input()
for char in string:
    if(char.isupper()):
        print(char)
length = len(string)
print("___________")
for i in range(0,length,2):
    print(string[i])

print("___________")
for char in string:
    if(char.lower()== 'a'
       or char.lower()== 'e'
       or char.lower()== 'i'
       or char.lower()== 'o'
       or char.lower()== 'u'):
        print('_')
    else:
        print(char)

print("___________")
digits = 0
for char in string:
    if(char.isdigit()):
        digits+= 1
print("digits =",digits)
print("___________")
vowels = 0
for char in string:
    if(char.lower()== 'a'
       or char.lower()== 'e'
       or char.lower()== 'i'
       or char.lower()== 'o'
       or char.lower()== 'u'):
        vowels+=1
print("vowels = ",vowels)
print("___________")
for i in range(length-1,-1,-1):
    print(string[i])
print("___________")
for i in range(7):
    for i in range(1,i,1):
        print('*',end ="")

    print()
print("___________")
for i in range(5):
    size = 0
    if i==0 or i == 2 : size = 5
    else : size = 2
    for j in range(size):
        print('*',end ="")
    print()
print("___________")
for i in range(5):
    size = 0
    if i==4 : size = 5
    else : size = 2
    for j in range(size):
        print('*',end ="")
    print()
