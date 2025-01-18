
login = "admin"#initialization 
print(login)

login = "helen"# присвоєння
print(login)


a,b,c = 1,2,3 #------->
print(a)
print(b)
print(c)

d = e = f = 25 #<-----------------
print(d)
print(e)
print(f)

# binary operators (2) + - * / // % ** 5 + 6
# uno operators (1)  -5   +8

#logic operators ==, != , > , <, >= , <= 
print("1 == 1:", 1 == 1)   #True      
print("1 == 2:", 1 == 2)   #False    

print("1 != 1:", 1 != 1)    #False     

print("1 != 2:", 1 != 2)    #True     
print("1 > 1:", 1 > 1)      #False     
print("1 > 2:", 1 > 2)      #False       
print("2 > 1:", 2 > 1)      #True 
print("1 < 1:", 1 < 1)      #False 
print("1 < 2:", 1 < 2)      #True  
print("2 < 1:", 2 < 1)      #False  
print("1 >= 1:", 1 >= 1)    #True    
print("1 >= 2:", 1 >= 2)    #False   

print("2 >= 1:", 2 >= 1)   #True      
print("1 <= 1:", 1 <= 1)    #True     
print("1 <= 2:", 1 <= 2)    #True     
print("2 <= 1:", 2 <= 1)    #False     

print(bool(""))# False
print(bool(0))# False
print(bool(0.0))# False
print(bool(None))# False
print(bool(5))# True
print(bool(-5))# True
print(bool("Hello"))# True
print(bool(0.1))# True

# and 
competent = False
responsible = False
print(competent and responsible )
#True and True  = True
#False and True = False
#True and  False = False
#False and  False = False


#or 
competent = False
responsible = False
print(competent or responsible )
#True and True  = True
#False and True = True
#True and  False = True
#False and  False = False

#not 
competent = True
print(competent)
print(not competent)


age = int (input("Enter age : "))
print("Age = ", age)

#if age >= 18 and age <= 120:
if  18 <= age <= 120:
    print("Welcome to my Game!!!!")
else:
    print("Age is error")

day = int(input("Enter number of day [1-7] : "))

    
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")    
elif day == 7:
    print("Sunday")
else:
    print("Error number day ")


login = input("Enter login : ")
if login == "admin":
    password = input("Enter pasword : ")
    if password == "qwerty":
        print("Welcome !")
    else:
        print("Incorrect password")
elif login == "exit":
    print("Have a nice day! ")
else:
    print("Error login...")

 

a = 8
b = 7
c = 12

print(a,b,c)
print("a = ", a, "b = ", b, "c = ", c)
print("a = ", a,". ", "b = ", b,". ", "c = ", c,". ")
print("Numbers : a = {}. b = {}. c = {}.".format(a,b,c))
print("Numbers : a = {}. b = {}. c = {}.".format(b,a,c))
print("Numbers : a = {}. b = {}. c = {}.".format(c,b,a))
print(f"Numbers : a = {a}. b = {b}. c = {c}." )