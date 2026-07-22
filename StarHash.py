s = '****#'
star = 0
haash = 0
numbers = s.split(" ")



for arr in s:
    if(arr == '*'):
        star+=1
    else:
        haash+=1
print(star-haash)