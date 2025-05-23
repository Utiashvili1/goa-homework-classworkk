name=str(input("enter your name"))
for i in range(11):
    print(name)


    
for i in range(5): #ეს არის თავი
    print("ricxvi:",i) #ეს არის ტანი

    num = int(input("Enter number: "))

for i in range(0, num):
    print(i)



names = ""

for i in range(5):  
    name = input(f"{i+1}) შეიყვანე სახელი: ")  
    if i < 4:
        names += name + ", "  
    else:
        names += name  

print("შეყვანილი სახელები:", names)