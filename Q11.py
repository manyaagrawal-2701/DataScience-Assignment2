student=[('U2024002',60), ('U20240086',70), ('U20240030',99), ('U20240040',50), ('U20240012',86)]
def sort(student):
    sortedlist=sorted(student,key=lambda x:x[1],reverse=True) # key is extracting the score and ordering according to highest score to lowest
    for i in sortedlist:
        print(i)
sort(student)

    

        
