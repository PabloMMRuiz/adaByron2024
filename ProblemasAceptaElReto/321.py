from collections import defaultdict
def lee_numero():
    return int(input())

def lee_numeros():
    return list(map(int, input().split()))

def solve(bus:list):
    pisoArriba = bus[0]
    pisoAbajo = bus[1]
    n=pisoAbajo+pisoArriba
    inicio = n*(n+1) //2 +1 #el primer lugar lo ocupa el 0, que no es natural, de ahi el +1
    print(inicio+pisoArriba)

def main():
    n = lee_numero()
    while n != 0:
        solve(lee_numeros())
        n -=1

if __name__ == "__main__":
    main()