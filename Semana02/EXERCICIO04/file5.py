#work with array
courses = ['History', 'Math', 'Physics','CompSci']
print (courses)
print (len(courses))
print (courses[0])
print (courses[-1])
print (courses[0:2])
print (courses[2:])

courses.append('Art')
print ('add no final: ', courses)

courses.insert(0, 'Art')
print('add na possição 0: ', courses)

courses_2 = ['Education']
courses_2.insert(0, courses)
print(courses_2)

courses.remove('Math')
print('remove especifico: ', courses)

popped=courses.pop()
print('item deletado: ', popped)
print(courses)

courses.reverse()
print('invertida: ',courses)

sorted_courses = sorted(courses)
print('embaralhado: ',sorted_courses)
nums = [1,5,2,4,3]
print(f'max: {max(nums)} min: {min(nums)} soma: {sum(nums)} ')

print(courses.index('Art'))
print('Art' in courses)

student = {'name' : 'luiz', 'age': 23,'courses': ['Math', 'CompSci']}
print(student['name'])
print(student.get('name'))
student['phone'] = '555'
student['name'] = 'jane'
print(student)
student.update ({'name': 'Jane', 'age':26, 'phone': '555-5555'})
print(student)
del student['age']
print(student)

age = student.pop('phone')
print(student)
print(age)

print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key, value)