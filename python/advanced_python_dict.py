import csv
from operator import itemgetter

faculty_dict = {}
professor_dict = {}

with open('faculty.csv', 'rb') as f:
    faculty = csv.reader(f)
#    header = faculty.next()
    for name, degree, title, email in faculty:
        first = name.split()[0]
        last = name.split()[-1]
        faculty_dict[last] = [degree, title, email]
        professor_dict[first, last] = [degree, title, email]  
        
#Q6.
print
count = 0
for i in faculty_dict:
    count += 1
    if count < 4:
        print str(i)+': '+str(faculty_dict[i])
print
#Q7.
count = 0
for i in professor_dict:
    count += 1
    if count < 4:
        print str(i)+': '+str(professor_dict[i])
print
#Q8. 
count = 0
for k in sorted(professor_dict.keys(), key=itemgetter(1)):
    count += 1
    if count < 4:
        print str(k)+': '+str(professor_dict[k])
 
