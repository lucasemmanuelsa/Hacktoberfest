#https://codeforces.com/contest/1809/problem/A
n = int(input())

for p in range(n):

    lista = input()

    entrada = []

    for i in lista:
        entrada.append(int(i))

    maior = entrada[0]
    
    for j in entrada:
        if(j > maior):
            maior = j

    frequencia = []
    for k in range(maior + 1):
        frequencia.append(0)

    for m in entrada:
        frequencia[m] += 1

    num2 = frequencia.count(2)
    if(4 in frequencia):
        print(-1)
    elif 3 in frequencia:
        print(6)
    elif(2 in frequencia):
        print(4)
    else:
        print(4)