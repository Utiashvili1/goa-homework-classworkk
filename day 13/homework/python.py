Heart_size = int(input("semoiyvane seni wneva"))
puls_size = int(input("semoiyvane pulsis cema"))

if Heart_size > 140 or puls_size > 90:
    print("high Preassure")
elif Heart_size < 90 or puls_size < 60:
    print("low Preassure")
else:
    print("normal Preassuere")

# 2

weight = int(input("semoiyvanet tqveni wona"))
age = int(input("semoiyvanet tqveni asaki"))

if age < 10:
    if weight < 20:
        print("Low Weight")
    elif 20 < weight < 40:
        print("Normal Weight")
    else:
        print("High Weight")
elif 10 < age < 17:
    if weight < 40:
        print("Low Weight")
    elif  40 < weight < 65:
        print("Normal Weight")
    else:
        print("High Weight")
else:
    if weight < 50:
        print("Low Weight")
    elif 50 < weight < 90:
        print("Normal Weight") 
    else:
        print("High Weight")

# 3
age = int(input("semoiyvanet tqveni asaki"))
time = int(input("semoiyvanet droo"))

if age < 18 and time >= 22:
    print("droa dzilis")
elif age >= 60 and time >= 21:
    print("dasveneba rekomendebulia")
else:
    print("gaagrdzele aqtivoba")

# 4
age = int(input("semoiyvanet tqveni asaki "))
heart_size1 = int(input("semoiyvanet tqveni gulis cemaa"))

if age < 30 and heart_size1 < 140:
    print("segidlia meti ivarjisot")
elif age < 30 and heart_size1 > 170:
    print("dasveneba dagjirdebat")
else:
    print("aqtivobis done normaluria")

# 5
age = int(input("semoiyvanet asaki"))

if age <= 12:
    print("bevri vitaminiani sakvebi")
elif age >= 13 and age <= 25:
    print("energiis momcemi sakvebi")
elif age >= 26 and age <= 59:
    print("balansirebuli racioni")
elif age <= 60:
    print("dabalkaloriuli da msubuqi sakvebi")