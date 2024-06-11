from collections import defaultdict
def lee_numero():
    return int(input())

def lee_numeros():
    return list(map(int, input().split()))

def solve(n:int, ls:list):
    #Hay hasta un millon de sacos, pero solo 20000 numeros posibles. Nos interesa mas separarlos por pesos que mirar mucho la lista
    currMax = 0
    weightDict = defaultdict(lambda :0)
    for e in ls:
        weightDict[e] +=1
        if weightDict[e]==2:
            currMax+=1
            weightDict[e]=0
        if currMax > n:
            break
    print(min(currMax, n))


def main():
    n = lee_numero()
    while n != 0:
        solve(lee_numeros()[0], lee_numeros())
        n -=1

if __name__ == "__main__":
    main()