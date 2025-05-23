num = 1
while num<10:
    print(num)
    num +=1

num = 10
while num>1:
    print(num)
    num -=1
#while loop გამოგვიტანს შედეგს იქამდე სანამ პირობა სრულდება

correct_password = "python123"

while True:
    user_input = input("Enter password: ")
    if user_input == correct_password:
        print("Correct Password")
        break
    else:
        print("Incorect Password, Try Again")

sum=0
num = int(input("enter a number"))

while num > 3:
    sum += num
    num -= 1

print(sum)
