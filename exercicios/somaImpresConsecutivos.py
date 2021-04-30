m = int(input("digite o valor de m: "))
n = 1
inicio = 1
while n <= m:
    print("{}^3 = {}".format(n, inicio), end=" ")
    #print(inicio)
    i = 1
    while i+1 <= n:
        print("+",inicio + 2 * i, end=" ")
        i = i + 1
    inicio = inicio + 2 * n
    n = n + 1
    print("\n")
