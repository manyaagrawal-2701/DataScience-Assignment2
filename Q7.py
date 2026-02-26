Dict={'Rose':15, 'Rohan':18, 'Anika':23, 'kartik':30} # dictionary with keys as names and ages
for name, age in Dict.items(): # loop to check each key for the condition
    if(age>=18): # condition 
        print(name, age)