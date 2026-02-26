import random
unique=set()
freq={}
for i in range(1,21):
    num=random.randint(1,100) #generate random numbers
    unique.add(num) # add unique in set
    
    if num not in freq:
        freq[num]=1
    else:
        freq[num]+=1
print(unique)
print(freq)
max=0
for i in freq: 
    if(i>max):
        max=i
print("most common", max)