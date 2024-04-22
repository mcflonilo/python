def likes(names):
    x = ""
    if(names.__len__()>=4):
            x += names[0] +", "+ names[1] + f" and {names.__len__()-2} others likes this"
    elif(names.__len__()==3):
          x += f"{names[0]}, {names[1]} and {names[2]} likes this"

    elif(names.__len__()==2):
          x += f"{names[0]} and {names[1]} like this"
    elif(names.__len__()==1):
          x += f"{names[0]} likes this"
    elif(names.__len__()==0):
          x += "no one likes this"
    return x

print(likes(['Alex']))

def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)