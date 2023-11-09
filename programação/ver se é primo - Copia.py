X = int(input("Digite um valor: "))
i = 1

while (X == 0 or X != 0):
    if (X != 0):
        while (i != X or X == 1):
            i = i + 1
            if (X % i == 0 and i != X and -i != X):
                print("{} dividido por {} é: ".format(X, i), X / i)
                X = int(input("Digite um valor: "))
                i = 1

            elif (i == X or -i == -X or -i == X or i == -X or X == 1 or X == -1):
                print("{} é um número primo.".format(X))
                X = int(input("Digite um valor: "))
                i = 1
                
    else:
        print("tem que ser diferente de 0")
        X = int(input("Digite um valor novamente: "))
