all_students = {"Student_1", "Student_2", "Student_3", "Student_4", "Student_5", 
"Student_6", "Student_7", "Student_8", "Student_9", "Student_10", "Student_11"} 
jee_students = {"Student_9", "Student_2", "Student_3", "Student_4", "Student_5"} 
cet_students = {"Student_5", "Student_9", "Student_2", "Student_7", "Student_3"} 
neet_students = {"Student_6", "Student_2", "Student_8", "Student_3", "Student_10"} 
print(all_students.intersection(jee_students)) 
print(all_students.union(jee_students)) 
print(all_students.intersection(cet_students)) 
print(all_students.difference(jee_students))
