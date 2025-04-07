import math

a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
if a + b <=c or a+c<= b or c+b<= a:
    print("Not a triangle, try again")
    a = int(input("Enter side a: "))
    b = int(input("Enter side b: "))
    c = int(input("Enter side c: "))
def cosine_rule(a, b, c):
    x = (a**2) + (b**2) - (c**2)
    y = x/(2*a*b)
    z = math.acos(y)
    answer = (z * 180) / math.pi
    return f"Angle C is {answer} degrees"




print(cosine_rule(a, b, c))
#cosC = a**2 + b**2 - c**2