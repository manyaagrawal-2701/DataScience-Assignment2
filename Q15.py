dict={1:[1,2,3,3,5], 2:[4,4,5,5,6], 3:[1,2,4,9,9]}
for i in dict:
    dict[i]=list(set(dict[i])) # first use set and then covert back to list

print(dict)