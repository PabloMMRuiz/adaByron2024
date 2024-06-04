def lee_numero():
    return int(input())

def lee_numeros():
    return list(map(int, input().split()))

def solve(nMax: int, ls:list):
    #posibles precios distintos: hay que hacer todas las sumas posibles de hasta nMax monedas
    #RECURSIVOOOOO
    #Si esto no es muy eficiente (que no lo es): se puede añadir memoria
    resSet = set()
    solveRes(nMax, ls, resSet, 0)
    print(len(resSet))

def solveRes(nMax: int, ls: list, resSet: set, currSum: int):
    if nMax == 1:
        for e in ls:
            resSet.add(e+currSum)
    else:
        for e in ls + [0]: #para conseguir soluciones con menos de nMax monedas
            solveRes(nMax-1,ls,resSet,currSum+e)

def main():
    n = lee_numero()
    while n != 0:
        solve(lee_numeros()[1], lee_numeros())
        n-=1

if __name__ == "__main__":
    main()