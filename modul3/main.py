
# n=3.5 edhe 65+ full scholership
# n = 3.5 edhe 50 = 60 gjsyme
# n = 3.5 edhe -50
# n= -3.5 hiq skollership
nota = 3.6
scori = 67
if nota >= 3.5 :
    if scori > 65 and scori < 100 :
        print("full scholership")
    elif scori <100 :
        print("Nope trying to cheat")
    elif scori <= 60 or scori >= 50 :
        print("half scholership")
    elif scori < 50 :
        print("quarter scholership")
else:
    print("no scholership")

