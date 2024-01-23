def osszegzes():
    n = -1
    while n < 0:
        n = int(input("N = "))
    ossz = 0
    for i in range(n+1):
        ossz += i
    print(f"Az első {n} db természetes szám összege: {ossz}")


def eldontes():
    n = int(input("\nszám: "))
    prim = True

    if n < 2:
        prim = False
    else:
        i = 2
        while i <= n ** 0.5 and n % i != 0:
            i += 1
        prim = i > n**0.5

    if prim:
        print("Prím")
    else:
        print("Nem prím")

