zeros = []
negatives = []
positives = []
while True:
    number = input("Enter an integer (blank to quit):")
    if number == "":
        break
    elif not number.isdigit(): # sjekker om input er et tall, hvis ikke så kommer en feilmelding
        print("Invalid input")
    elif int(number) == 0: # sjekker om input er 0, hvis ja legg til i zeros arrayet
        zeros.append(int(number))
    elif int(number) < 0:
        negatives.append(int(number))# sjekker om input er negativt, hvis ja legg til i negatives arrayet
    elif int(number) > 0:
        positives.append(int(number)) # sjekker om input er positivt, hvis ja legg til i positives arrayet
    else:
        print("Invalid input")
    
result = positives + zeros + negatives # legger alle arrayene sammen
print("the numbers were: \n", result)