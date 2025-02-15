
print("Hello")

# num1 = None
# num2 = None

# while num1== None or num2 ==None:
#     try:
#         num1 = int(input("Enter first number : "))
#         num2 = int(input("Enter second number : "))
#         print(f"Num = {num1/num2}")
    
#     except ValueError:
#         print("Value Error. Incorrect number ")
#     except ZeroDivisionError:
#         print("division by zero")
#     except Exception:
#         print("Error")




try:
    age = int(input("Enter age : "))
    #close file
    if age < 0 :
        #print("Incorrect age")
        #raise --> throw
        raise Exception("Age < 0")
      #close file
    if age > 125:        
        raise Exception("Age > 125") 
      #close file
except ValueError:
    print("Value Error. Incorrect number ")
      #close file
except Exception as ex:
        print(ex)
        print(f"Type exeption : {type(ex).__name__}")
          #close file
else:
    print("Work, when don*t worked any except")
    print(F"Continue......{age}")
      #close file
finally:
    print("Work always.....")
      #close file
     



print("Continue......")
print("Continue......")
print("Continue......")
print("Continue......")
print("Continue......")
try:
    colors = ['red','white','blue','yellow','green']#0....4
    index = int(input("Enter index of element : "))
    print(colors[index])
except ValueError:
    print("Value Error. Incorrect number ")
except IndexError:
    print("list index out of range")