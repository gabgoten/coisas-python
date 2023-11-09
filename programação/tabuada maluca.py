X = int(input("coloque um número: "))
i = 0
A = 1

while (X == 0 or X != 0):
    while ( i < 10 ):
        print("{} X {} = ".format(X, A), X * A)
        A = A + 1
        i = i + 1

    X = int(input("Coloque um número: "))
    i = 0
    A = 1
