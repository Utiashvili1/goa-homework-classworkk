n = int(input("shemoiyvane n "))
for i in range(0, n + 1):
    print(i)


age = int(input("seiyvane sheni asaki "))
has_student_card = input("studentis barati tu gaq?")

if age <18 or has_student_card.lower() == "ki":
    print("danazogi ")
elif age >= 60 and has_student_card.lower() == "ara":
    print("fazdakleba gaq ogond pensioneri")
else:
    print("fazdakleba")

    num1 = int(input("semoiyvane pirveli ricxvi"))
num2 = int(input("meore ricxvi semoiyvane"))

if num1 > 0 and num2 > 0:
    print("yvela dadebiti")
elif(num1 > 0 and num2 <= 0) or (num2 > 0 and num1 <= 0):
    print("dadebiti")
else:
    print("araa dadebiti")



num1 = int(input("sheiyvane ricxvi"))
num2 = int(input("sheiyvane meore ricxvi"))
operacia = input("sheiyvane sxva operaciebi rogoricaa: (+, -, *, /)")

if operacia == "+":
    print(num1 + num2)
elif operacia == "-":
    print(num1 - num2)
elif operacia == "*":
    print(num1 * num2)
elif operacia == "/":
    if num2  != 0:
        print(num1 / num2)
    else:
        print("araa swori")
else:
    print("araa swori")





a = 1
b = 0
c = 0

result_0 = (a and not b) or (b and not a)
result_1 = (b and c) and (a or b)
result_2 = (a and not c) or (b and not a) or (b and not c)

print("Result 0:",result_0)
print("Result 1:",result_1)
print("Reslut 2:",result_2)