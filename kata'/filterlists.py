def filter_list( l):
    l= list(l)

    for i in range(l.__len__()):
        for i in l:
            if(type(i)==str):
                l.remove(i)
            print(i)
    return l

def filter_list2(l):
  'return a new list with the strings filtered out'
  return [i for i in l if not isinstance(i, str)]


print(filter_list2([1,2,'a','b']))