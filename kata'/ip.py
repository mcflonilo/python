def ips_between(start, end):
    a = start.split(".")
    b = end.split(".")
    difference = 0
    difference += int(a[3])-int(b[3])
    difference += int(a[2])-int(b[2])*256
    difference += int(a[1])-int(b[1])*256
    return difference.__abs__()


print(ips_between("20.0.0.10", "20.0.1.0"))