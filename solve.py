from maths import Maths

solve = Maths()

from phy import Physics


d = input("Will you like to perform (M)aths or (P)hysics?: ")
if d.upper() == "M":

    g = input("Do you want to (a)dd, (s)ubtract, (d)ivide, (m)ultiply?, (e)area of sqaure:  ")
    if g.upper() == "A":
        solve = Maths()
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



elif d.upper() == "P":
    solve = Physics()
    g = input("Do you want to calculate (m)ass, (v)elocity, (d)istance, (s)peed, (f)orce:  ")
    if g.upper() == "M":
        x = int(input("type Force: "))
        y = int(input("Acceleration: "))
        print(solve.mass(x, y))
    elif g.upper() == "V":
        x = int(input("type displacement: "))
        y = int(input("time: "))
        print(solve.velocity(x, y))
    elif g.upper() == "D":
        x = int(input("type Speed: "))
        y = int(input("Time: "))
        print(solve.distance(x, y))
    elif g.upper() == "S":
        x = int(input("type distance: "))
        y = int(input("type time: "))
        print(solve.speed(x, y))
    elif g.upper() == "F":
        x = int(input("mass: "))
        y = int(input("acceleration: "))
        print(solve.force(x, y))
