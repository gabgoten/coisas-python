X = int(input("Coloque o valor mínimo: "))
Y = int(input("Coloque o valor máximo: "))
i = 0

if (X <= Y):
    while ( X <= Y ):

        if ( X % 5 == 0):
            print("{} divido por 5 é: ".format(X), X / 5)

        X = X + 1
else:
    print("erro, o máximo é menor que o mínimo.")
