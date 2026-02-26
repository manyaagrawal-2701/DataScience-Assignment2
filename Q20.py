# calculate the sum of digits
def sumdigits(i):
    total=0
    while(i>0):
        r=i%10
        total=total+r
        i=i//10
    return total
s=set() # empty set
for i in range(2, 101):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 2:
        s.add(i) # find prime numbers and store in set

dict={} # empty dictionary
for j in s:
    d=sumdigits(j)
    if d not in dict:
        dict[d]=[] # d acts as key
    dict[d].append(j)
print(dict)
     

