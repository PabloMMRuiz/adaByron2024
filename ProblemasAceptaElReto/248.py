def lee_numero():
    return int(input())

def lee_numeros():
    return list(map(int, input().split()))

def solve(ls:list):
    ls = ls+ls #No tiene sentido pegarla mas de dos veces por que el ciclo es neto negativo
    curr = best = 0
    for e in ls:
        curr = max(curr+e, 0)
        best=max(best, curr)
    print(best)

def main():
    n = lee_numero()
    while n != 0:
        solve(lee_numeros())
        n = lee_numero()

if __name__ == "__main__":
    main()