import random
dict={1:'Rock', 2:'Paper', 3:'Scissor'}
user_win=set() # to store rounds in which user wins
comp_win=set() # to store rounds in which computer wns
for i in range(1,6):
    user=int(input("Enter choice"))
    computer=random.randint(1,3) # generating random choice
    print("User chose:" ,dict[user])
    print("Computer chose:", dict[computer])
    if(user==computer):
        print("Draw")
    elif(user==1 and computer==2): # rules of game
        comp_win.add(i)
    elif(user==1 and computer==3):
        user_win.add(i)
    elif(user==2 and computer==3):
        comp_win.add(i)
    elif(user==3 and computer==2):
        user_win.add(i)
    elif(user==3 and computer==1):
        comp_win.add(i)
    else:
         user_win.add(i)
if(len(user_win)>len(comp_win)):
    print("User wins")
else:
    print("Computer wins")
