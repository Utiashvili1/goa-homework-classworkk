for i in range(1, 101):
    if i % 2 == 0:
        print(f"{i} - luwi")
    else:
        print(f"{i} - kenti")

        
        number = int(input("enter number: "))

if number % 2 == 0:
    print("this number i luwi")
else:
    print("this nunder kenti")

    num1 = int(input("enter your first num: "))
num2 = int(input("enter your second num: "))

if num2 > num1:
    print("metia")
else:
    print("naklebi")

  

num1 = int(input("enter your first num: "))
num2 = int(input("enter your second num: "))

if num1 > num2:
    print("higer number:", num1)
elif num2 > num1:
    print("higer number:", num2)
else:
    print("both number are equal")