def lee_numero():
    return int(input())

def lee_numeros():
    return list(map(int, input().split()))

def solve(n, permu):
    iter = 1
    fin = list(range(1,n+1))
    curr = permu
    while curr != fin:
        iter+=1
        temp = [curr[e-1] for e in permu]
        curr = temp
    return iter
def main():
    n = lee_numero()
    permu = lee_numeros()
    while n!= 0:
        solve(n, permu)
        n = lee_numero()
        permu = lee_numeros()
        

if __name__ == "__main__":
    main()