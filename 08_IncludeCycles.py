

#print("*"*10)
for i in range(10):
    for j in range(10):#i = 0; i < 10; i +=1
        print(" *", end=" ")
    print()

print("Continue.........")

for i in range(1,10+1):#i = 1; i < 11; i +=1
    for j in range(1,10+1):#j = 1; j < 11; j +=1
        print(f" {i} * {j} = {i*j}")
    print()


floor = 1
energy = 70
print(f"I am on the {floor} floor")

while floor != 5:
    step = 0
    if floor == 3:
        print("I will take an elevator")
        break
    while step != 20:
        step+=1 
        energy -=1
        if energy == 0:
            print("I am tired. I will rest a little....")
            energy += 70
    floor+=1
    print(f"Now I am on the {floor} floor")
