
def ModifyName(userName):
    newName1 = userName.upper()
    newName2 = userName.lower()
    return newName1,newName2
    print("hello")
    print("hello")
    print("hello")
    print("hello")
    print("hello")
    print("hello")
    print("hello")

# name = input("Enter your name : ")
# print(ModifyName(name))
# nameUpper, nameLower = ModifyName(name)
# print(nameUpper)
# print(nameLower)

def checkLog(userLog):
    if userLog == 'admin':
        return userLog.upper()       
    
    elif userLog == 'user':
        return userLog.lower()
    else:
        return "Wrong login!!!"
    
print(checkLog('admin'))
print(checkLog('user'))
print(checkLog('student'))

def average(*args):
    print(args)
    summa = 0
    count = 0
    for num in args:
        summa += num
        count+=1
    return summa/count


numbers = [1,5,89,6,74,25,3,6]

print(average(1,5,89,6))
print(average(1,5,89,6,74,25,3,6))
print(average(*numbers))


def sayHello():
    print("Hello friend")
    sayHello()
    #test()

def test():
    print("Test function")

#sayHello()
#5! = 1*2*3*4*5
#8! = 1*2*3*4*5*6*7*8
factorial = 1
num = 5
for i in range(1,num+1):#1 2 3 4 5
    factorial*= i#1 * 1 = 1; 1*2 = 2; 2*3 = 6; 6*4=24; 24*5= 120
print(f"Factorial = {factorial}")

#5! --> return 5 * .....4!
#4! --> return 4 *....3!
#3! --> return 3 *......2!
#2! --> return 2 * ....1!
#1! --> return 1
#5*4*3*2*1*0*-1*-2*-3
def Factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * Factorial(num-1)
print(f"Factorial = {Factorial(5)}")

word = 'madam'
palindrom = word[::-1]
print(word)
print(palindrom)
if word == palindrom:
    print("Word is palindrom")
#madam -->  m == m .... a==a .....d  
#ada
#d ---> " "
def isPalindrom(word):
    if len(word) == 0:
        return True
    if word[0] == word[-1]:
        return isPalindrom(word[1:-1])
    else:
        return False
    
print(isPalindrom(word))

