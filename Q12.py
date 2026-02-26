# dictionary of students name and grades
school={'Raghav':[50,60,80], 'Sam':[80,98,40],'Radhika':[70,80,90],'Alia':[40,30,60], 'Ronny':[60,40,80]} 
dict_avg={} # new dict to store average
for name, grades in school.items():
    total=0
    for i in grades:
        total=total+i
    avg=total/3 # avg of each student's grade
    dict_avg[name]=avg # put in new dictionary
dict_sort=sorted(dict_avg.items(), reverse=True) # sorting the new dictionary in descending order 
for i in range(3):
    print(dict_sort[i]) # prints top three students