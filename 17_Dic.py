name = "Olena"
surname = "Ilushun"
group = "SPR411"
phone = "38097745456"

student1 = ["Olena","Ilushun","SPR411","38097745456"]

#dictionary
 
student = {
# key : value
#key : string, number
#value : any data type
    'name':"Olena",
    'surname':'Iliusyn',
    'group':'SPR411',
    'phone':'38097745456',
    'rating':10.3,
    'birthday':'01.01.2000'
}

print(student)
print(student['name'])
print(student['birthday'])

#get all keys
for key in student.keys():
    print(f"Key : {key}. Value : {student[key]}")

#get all values:
for value in student.values():
    print(value)

#get all keys and value
for key, value in student.items():
    print(f"{key} --> {value}")

print(student.keys())
print(student.values())
print(student.items())


print(student)
del student['rating']
print(student)
student.pop('surname')
print(student)
student.popitem()
print(student)
#add new key and value
student['email'] = 'lena@gmail.com'
print(student)
#change value by key
student['email'] = 'super_puper@gmail.com'
print(student)
print("---------------------------------------------------------------------------")

group = [
    {'name':"Olena",'surname':'Iliusyn','group':'SPR411','phone':'38097745456','rating':10.3,'birthday':'01.01.2003'},
    {'name':"Mukola",'surname':'Iliusyn2','group':'SPR411','phone':'38056456756','rating':7,'birthday':'01.01.2007'},
    {'name':"Oleg",'surname':'Iliusyn3','group':'SPR411','phone':'38097676766','rating':4.2,'birthday':'01.01.1999'},
    {'name':"Iruna",'surname':'Iliusyn4','group':'SPR411','phone':'3809774576766','rating':11.9,'birthday':'01.01.2007'},
    {'name':"Yana",'surname':'Iliusyn5','group':'SPR411','phone':'380977456776','rating':9.8,'birthday':'01.01.2006',
     'marks':[11,12,10,9,8,4]}

]
print(group[2])
print(group[0])
print(group[4])

print(group[2]["group"])
print(group[0]["phone"])
print(group[4]["birthday"])
print(group[4]['marks'][2])
print("Mark student Yana : ", end='')
for mark in group[4]['marks']:
    print(mark, end=" ")

print()


import json
student_write = {
    'name':"Olena",
    'surname':'Iliusyn',
    'group':'SPR411',
    'phone':'38097745456',
    'rating':10.3,
    'birthday':'01.01.2000'
}
# print(f"Tyoe of object : {type(str(student_write))}")
# with open('./16_Files/student.txt','w') as file:
#     file.write(str(student_write))

print(f"Type of object : {type(student_write)}")
print(student_write)
byte_object = json.dumps(student_write)
print(f"Type of object : {type(byte_object)}")
print(byte_object)
with open('./16_Files/student.txt','w') as file:
    file.write(byte_object)
new_obj = json.loads(byte_object)
print(f"Type of object : {type(new_obj)}")
print(new_obj['name'])

with open('./16_Files/student.txt','r') as file:
    info = file.read()
    print(info)
    info = json.loads(info)
    print(info['name'])