A = 0
while (A == 0):
    X = int(input("Digite quantos números serão lidos: "))
    if (X <= 0):
        print("o total de números lídos tem que ser maior que 0")
    else:
        A = A + 1
C = 0
while (C == 0):
    Y = int(input("Digite o número: "))
    if (Y <= 0):
        print("o número tem que ser maior que 0")
    else:
        C = C + 1
maior = Y
menor = Y
i = 1
B = 1

while (i < X):

    i = i + 1

    B = B - 1
            
    if (Y > maior):
        maior = Y

    if (Y <= menor):
        menor = Y

    while (B == 0):
        Y = int(input("Digite o número: "))
        if (Y <= 0):
            print("o número tem que ser maior que 0")
        else:
            B = B + 1        

if (Y > maior):
    maior = Y

print("O maior número digitado é: ", maior)
print("O menor número digitado é: ", menor)



    
