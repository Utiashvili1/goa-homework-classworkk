#Inplict conversion (implicit Type castion) ეს არის ავტომატური გარდაქმნა რომელიც ხდება კომპილატორის ან interpertation მიერ. იგი ხდება მაშინ როცა მონაცემთა ტიპები თავსდება და რისკი მინემალური

#explicit converison (explicit type castion) ეს არის გარდაქმნა, რომელიც უნდა მოხდეს პროგრამისტის მიერ. იგი გამოიყენება მაშინ როცა მონაცემთა ტიპების ნაკლებად თავსდება და საჭირო განმარტება

num =int(input("enter number: "))

for i in range(0, num ):
    print(i)

num =int(input("enter number: "))

while num > 0:
    print(num)
    num += 1