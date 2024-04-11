import re
def count_smileys(arr):
    count= 0
    for x in arr:
        count += re.findall("[(:|;)]+[(-||~)]?[\)|D]+", x).__len__()
    return count

print(count_smileys([':D',':~)',';~D',':)']))