X = int(input("Digite um número: "))
i = 0
F1 = 0
F2 = 1
L = [F1, F1 + F2]
A = 0

while (X == 0 or X != 0):
    while (i < X):

        F1 = F1 + F2
        F2 = F1 + F2
        
        L.append(F1)
        L.append(F2)

        i = i + 1

    if (X <= 0):
        print("não tem né doido")

    else:
        print("os {} primeiros termos na sequência de Fibonacci são: ".format(X))
        while (A < X):
            print(L[A])
            A = A + 1

    X = int(input("Digite um número: "))
    i = 0
    F1 = 0
    F2 = 1
    L = [F1, F1 + F2]
    A = 0
    
