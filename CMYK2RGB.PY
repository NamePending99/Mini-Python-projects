def cmyk2rgb(C, M, Y, K):
    r = round(255 * (1-C) * (1-K))
    g = round(255 * (1-M) * (1-K))
    b = round(255 * (1-Y) * (1-K))

    return r, g, b


# Note: Values for C,M,Y,K has to be within [0,1]
print("Specify values for CMYK to be converted")
C = float(input("C: "))
M = float(input("M: "))
Y = float(input("Y: "))
K = float(input("K: "))

R, G, B = cmyk2rgb(C, M, Y, K)

print("RGB equivalent of input:", R, G, B)
