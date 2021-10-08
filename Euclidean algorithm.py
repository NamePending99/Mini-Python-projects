def gcd(a, b):
    while b != 0:
        g_b = b
        b = a % b
        a = g_b

    return a


numerator = int(input("Numerator: "))
denominator = int(input("Denominator: "))

print("Greateast commond divisor:", gcd(numerator, denominator))
