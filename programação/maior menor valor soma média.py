X = int(input("Digite um número maior que 0, ou digite 0 para parar: "))
totalvalor = 0
totalsoma = 0
totalmedia = 0
maior = X
menor = X

while (X > 0):
    totalvalor = totalvalor + 1
    totalsoma = totalsoma + X
    totalmedia = totalmedia + X
    
    if (X > maior):
        maior = X

    if (X <= menor):
        menor = X
    
    X = int(input("Digite um número maior que 0, ou digite 0 para parar: "))

print("O maior número digitado é: ", maior)
print("O menor número digitado é: ", menor)
print("O total de valores digitados é: ", totalvalor)
print("A soma total dos valores digitados é: ", totalsoma)
print("A média total dos valores digitados é: ", totalmedia / totalvalor)

    

    
