from maths import Maths
solve = Maths()
d = input("Will you like to perform (M)aths or (P)hysics?: ")
if d.upper() =="M":

    g = input("Do you want to (a)dd, (s)ubtract, (d)ivide, (m)ultiply?, (e)area of sqaure:  ")
    if g.upper() == "A":
        x = int(input("type first number: "))
        y = int(input("second number: "))
        print(solve.add(x, y))
    elif g.upper() == "S":
        x = int(input("type first number: "))
        y = int(input("second number: "))
        print(solve.sub(x, y))
    elif g.upper() == "D":
        x = int(input("type first number: "))
        y = int(input("second number: "))
        print(solve.div(x, y))
    elif g.upper() == "M":
        x = int(input("type first number: "))
        y = int(input("second number: "))
        print(solve.mul(x, y))
    elif g.upper() == "E":
        x = int(input("length: "))
        y = int(input("breadth: "))
        print(solve.exp(x, y))



