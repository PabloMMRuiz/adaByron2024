#Este es el primero graciosillo
#Esto huele a grafo dirigido, pero dijkstra me parece to feo.
def lee_numero():
    return int(input())

def lee_numeros():
    return list(map(int, input().split()))

def solve(n:int, k:int, serpientes: list, escaleras:list):
    meta = n*n
    currPos = (1, 0) #posicion, numero de tiradas
    visited = set()
    pile = [currPos]
    while len(pile)>0:
        currPos = pile.pop(0)
        for tirada in range(1, k+1):
            alcanzada = currPos[0]+tirada
            if alcanzada >= meta:
                print(currPos[1]+1)
                return
            for sStart, sEnd in serpientes: #Hay formas mas eficientes de hacer esto
                if sStart == alcanzada:
                    alcanzada = sEnd
                    break
            for eStart, eEnd in escaleras:
                if eStart == alcanzada:
                    alcanzada = eEnd
                    break
            if alcanzada not in visited:
                pile.append((alcanzada, currPos[1]+1))
                visited.add(alcanzada)
            


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