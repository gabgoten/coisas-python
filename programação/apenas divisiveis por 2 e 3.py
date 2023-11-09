X = int(input("Digite um valor diferente de 0, ou 0 para parar: "))
i = 0
A = 0
L1 = []
L2 = []

while (X != 0):

    if (X % 2 == 0):
        X2 = X / 2
        L1.append("{} dividido por 2 é {}".format(X, X2))

    if (X % 3 == 0):
        X3 = X / 3
        L2.append("{} dividido por 3 é {}".format(X, X3))

    X = int(input("Digite um valor diferente de 0, ou 0 para parar: "))


print("Os números digitados que podem ser divididos por 2 são: ".format(X))
for N in L1:
    print(N)
print("Os números digitados que podem ser divididos por 3 são: ".format(X))
for N in L2:
    print(N)
