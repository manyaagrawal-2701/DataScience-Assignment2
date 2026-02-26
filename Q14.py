# list to store items and their cost
cart={'apples':70, 'bread':20, 'milk':40, 'icecream':60, 'chocolate':60}
total=0 # to calculate the total of the items bought
for item, cost in cart.items(): # iterate over each key
    total=total+cost
print(f"Amount before discount:{total}")
if(total>100): # condition 
    print(f" Amount after 10 percent discount:{total-(total*.1)}") # amount after discount

