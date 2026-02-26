students={'class 1':{'Ronny':70,'Rachel':80,'Anna':60},
          'class 2':{'Radhika':85,'Berta':65,'Alma':70},
          'class 3':{'Eva':90,'Jenna':83,'Rasputin':50}}
def avg(students):
    for c, student in students.items():
        total=0
        count=0
        for s, grade in student.items():
            total=total+grade
            count=count+1
        avg=total/count
    print(avg)
avg(students)
        

        