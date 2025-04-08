print("Welecome Marks Sheet")

print("Enter your total marks and check grade!")

marks = int(input("Enter your total marks(OUT OF 100):")) #yaha hamne User se input lya hai.
if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 50:
    print("D")
elif marks >= 40:
    print("E")
else:
    print("Fail")

