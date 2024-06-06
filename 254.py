def lee_numero():
    return int(input())

def lee_numeros():
    return list(map(int, input().split()))

#Lo primero que se me ocurre es ordenar las dos listas y calcular la suma de diferencias. Se puede mejorar seguro
def solve(n: int, pers: list, esquis: list):
    pers.sort()
    esquis.sort()
    ac = 0
    for i in range(n):
        if (pers[i] < esquis[i]):
            ac += esquis[i] - pers[i]
        else:
            ac += pers[i] - esquis[i]
    print(ac)

def main():
    n = -1
    while(n != 0):
        n = lee_numero()
        pers = lee_numeros()
        esquis = lee_numeros()
        solve(n, pers, esquis)

if __name__ == "__main__":
    main()

