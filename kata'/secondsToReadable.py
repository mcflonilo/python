def make_readable(seconds):    
    return '{:02d}:{:02d}:{:02d}'.format(int(seconds/3600),int((seconds%3600)/60),int((seconds%3600)%60))

print(make_readable(3661))