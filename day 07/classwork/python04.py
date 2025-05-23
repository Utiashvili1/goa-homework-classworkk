names = ""

for i in range(5):  
    name = input(f"{i+1}) შეიყვანე სახელი: ")  
    if i < 4:
        names += name + ", "  
    else:
        names += name  

print("შეყვანილი სახელები:", names)