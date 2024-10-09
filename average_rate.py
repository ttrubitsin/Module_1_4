
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny','Bilbo','Steve','Khendrik','Aaron'}
students_list = list(students)
students_list.sort()
print(students_list)

avg_aaron_rate = sum(grades[0])/len(grades[0])
avg_bilbo_rate = sum(grades[1])/len(grades[1])
avg_johnny_rate = sum(grades[2])/len(grades[2])
avg_khendrik_rate = round(sum(grades[3])/len(grades[3]),2)
avg_steve_rate = sum(grades[4])/len(grades[4])


dict_student = dict()
dict_student.update({students_list[0]:avg_aaron_rate,
                     students_list[1]:avg_bilbo_rate,
                     students_list[2]:avg_johnny_rate,
                     students_list[3]:avg_khendrik_rate,
                     students_list[4]:avg_steve_rate})

print("Average_grades:", dict_student)