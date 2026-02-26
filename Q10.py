set1={1,2,3,4,5,6} 
set2={4,5,6,7,8,9}
print(set1.union(set2)) # function to include everything from both sets but does not allow duplicates
print(set1.intersection(set2)) # function to include only common values
diff_set1=set1.difference(set2) # function to only keep values of set1 and exclude values of set2 and those common in both
print("diff of set1")
for i in diff_set1: # for loop to print the values 
    print(i)
print("diff of set2")
diff_set2=set2.difference(set1) # function to only keep values of set2 and exclude values of set1 and those coomon in both
print("diff of set1")
for i in diff_set2: # for loop to print the values 
    print(i)