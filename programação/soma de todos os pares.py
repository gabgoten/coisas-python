X = int(input("Digite um número maior ou igual que 100: "))
i = 0
total = 1
A = 0

while (X >= 100 and i <= X):
    if (i % 2 == 0):
        print(i)
        total = total + i
    i = i + 1

print("a soma de todos os números pares de 1 até {} é: ".format(X), total)


    

    
