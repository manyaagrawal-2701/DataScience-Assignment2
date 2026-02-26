l1=[1,2,3,4,5]

def rev(l1): # loop
    rev=[]
    for i in range(len(l1)-1,-1,-1):
        rev.append(l1[i])
    print(rev)
rev(l1)

def reverse(l1): # slicing
    print(l1[::-1])
        
reverse(l1)

    

t=(1,2,3,4,5)
def tuprev(t): # comapre with tuples
    rev=t[::-1]
    print(rev)
tuprev(t)
print(t)