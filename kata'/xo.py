from operator import *
def xo(s):
    s.lower()
    return countOf(s,'x')==countOf(s,'o')

print(xo("ooxx"))