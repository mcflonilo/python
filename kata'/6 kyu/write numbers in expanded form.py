def expanded_form(num):
    x = list(str(num))
    print(x)
    y = ""
    if len(x) == 1:
        return x[0]
    for i in range(len(x)):
        if x[i] != "0":
            if i == 0:
                print(x[i] + "0" * (len(x) - i - 1) + " + ")
                y += x[i] + "0" * (len(x) - i - 1) + " + "
            elif i == len(x) - 1:
                print(x[i])
                y += x[i]
            else:
                print(x[i] + "0" * (len(x) - i - 1) + " + ")
                y += x[i] + "0" * (len(x) - i - 1) + " + "
    return y

print (expanded_form(70304)) # '70000 + 300 + 4'