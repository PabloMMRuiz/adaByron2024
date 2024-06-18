from collections import defaultdict
def lee_numero():
    return int(input())

def lee_numeros():
    return list(map(int, input().split()))

def solve(n:int,_noseusa:int, ls:list):
    ls = [1 if e >= n else 0 for e in ls]
    numPalmeras = 0
    i=j=0
    maxLen = 0
    numPalmeras+=ls[0]
    while i != len(ls):
        #fase de incremento
        while numPalmeras < 5 and j <len(ls)-1:
            j+=1
            numPalmeras+=ls[j]
            #Estoy cogiendo la ventana [], no [)
        #comparamos contra el maximo
        if j-i > maxLen:
            maxLen=j-i +1
        #fase de decrecimiento
        while numPalmeras >=5 and i < j:
            numPalmeras-=ls[i]
            i+=1
        if j == len(ls)-1:
            break
    print(maxLen)


def main():
    n = lee_numero()
    while n != 0:
        solve(lee_numero(), lee_numero(), lee_numeros())
        n -=1

if __name__ == "__main__":
    main()