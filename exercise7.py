import re
def average(list):
    total = 0
    for x in list:
        total+= float(x)
    return total / len(list)


#filnavn = input("skriv navnet på filen du vil åpne")
#filnavn2 = input("skriv navnep på filen du vil skrive til")


fil = open("column.txt")
fil2 = open("hello.txt")
#fil2 = open(filnavn2, "w")
count = 0
for line in fil:
    count+=1
    x = re.findall("(\d.\d)",line)
    avg = average(x)
    
    print("/*",avg,"*/" , line)
count = 0
lettercount=0
wordcount = 0
for line in fil2:
    x = re.findall("(\w+)", line)
    wordcount += x.__len__()
    lettercount += line.__len__()
    count+=1
print("letters = ",lettercount,"\n",
      "words = ", wordcount, "\n",
      "lines =",count,"\n")

condition = 0
lst = []
while(condition<2):
    inp = input("write a number")
    if(inp.isdigit()==False):
       condition+=1
       inp = 0
       print("not a number, one more attempt")
    lst.append(int(inp))

print(sum(lst))