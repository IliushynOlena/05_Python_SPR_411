import json

def addNewUser():
    id = int(input("Enter id : "))
    name = input("Enter name : ")
    return {'id':id,'name':name}

def createList(number):
    users = []
    for i in range(number):
        users.append(addNewUser())
    return users

def printUsers(users):
    for i in range(len(users)):
        print(users[i])

def writeToFile(users):
    with open('users.json','w') as file:
        file.write(json.dumps(users))

def readUsers():
    with open('users.json','r') as file:
        return json.loads(file.read())
while True:
    choice = int(input('''
        1 - Create database
        2 - Add user
        3 - Delete user
        4 - Print all users
        5 - Sort users by name
        6 - Sort users by id
        7 - Sort users by price
        8 - Search users by name
                       
        0 - Exit  
        '''))
    if choice == 1:
        number = int(input("Enter number of users : "))
        users = createList(number)
        writeToFile(users)
    if choice == 0:
        print("Goodbye.....")
        break
    if choice == 4:
        users = readUsers()
        printUsers(users)
    if choice == 2:
        users = readUsers()
        users.append(addNewUser())
        writeToFile(users)
    if choice == 5:
        users = readUsers()
        printUsers(users)
        users.sort(key = lambda u:u['name'])
        printUsers(users)
