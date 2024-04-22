zeros = []
negatives = []
positives = []
while True:
    number = input("Enter an integer (blank to quit):")
    if number == "":
        break
    elif int(number) == 0:
        zeros.append(int(number))
    elif int(number) < 0:
        negatives.append(int(number))
    elif int(number) > 0:
        positives.append(int(number))
    else:
        print("Invalid input")
    
result = positives + zeros + negatives
print("the numbers were: \n", result)