def lee_numero():
    return int(input())

def lee_numeros():
    return list(map(int, input().split()))

def solve(ls:list):
    ant = ls[0]
    for e in ls[1:]:
        if e <= ant:
            print("NO")
            return
        else:
            ant = e
    print("SI")

def main():
    n = lee_numero()
    while n != 0:
        solve(lee_numeros())
        n = lee_numero()

if __name__ == "__main__":
    main()
