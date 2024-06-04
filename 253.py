#Este es el primero graciosillo
#Esto huele a grafo dirigido, pero dijkstra me parece to feo.
def lee_numero():
    return int(input())

def lee_numeros():
    return list(map(int, input().split()))

def solve(n:int, k:int, serpientes: list, escaleras:list):
#Vamos a utilizar una implementacion de disktra rarilla: voy a intentar avanzar siempre todo lo que pueda hacia delante
#Que tampoco tiene mucho sentido avanzar menos
    meta = n*n
    currPos = 1
    print(solveRes(meta,k, currPos, 0, serpientes, escaleras))
#Pues si que tiene sentido avanzar menos, tocate un pie. Putas escaleras...
def solveRes(meta: int, k:int, currPos: int, numTiradas: int, serpientes: list, escaleras: list):
    if(meta-currPos <= k):
        return numTiradas +1
    else:
        bestPos = currPos
        for e in range(1,k+1):
            alcanzada = currPos+e
            for sStart, _sEnd in serpientes:
                if sStart == alcanzada:
                    alcanzada = -10
                    break
            for eStart, eEnd in escaleras:
                if eStart == alcanzada:
                    alcanzada = eEnd
                    break
            if alcanzada > bestPos:
                bestPos= alcanzada
                if bestPos >= meta:
                    return numTiradas+1
        print(bestPos)
        return solveRes(meta, k, bestPos, numTiradas+1, serpientes, escaleras)
def main():
    info = lee_numeros()
    n = info[0]
    k = info[1]
    serpientes = []
    for e in range(info[2]):
        serpientes.append(lee_numeros())
    escaleras = []
    for e in range(info[3]):
        escaleras.append(lee_numeros())
    lee_numeros()
    solve(n, k, serpientes, escaleras)

if __name__ == "__main__":
    main()