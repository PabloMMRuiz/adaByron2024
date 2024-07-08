def lee_numeros():
    return list(map(int, input().split()))

def solve(start, end):
    #cuantos digitos hay hasta x?
    start=start-1
    l1 = len(str(start))
    l2 = len(str(end))
    #Casi que meto el calculo ya hecho, no?
    precalcs = {1: 0, 2: 9, 3: 189, 4: 2889, 5:3889, 6: 488889, 7: 5888890}
    ndigs = 0
    if l2 == 1:
        ndigs = end-start
    else:
        if l1 == 1:
            ndigs = precalcs[l2]+l2*(1+end-10**(l2-1)) - start
        else:
            ndigs = precalcs[l2]+l2*(1+end-10**(l2-1)) - (precalcs[l1]+l1*(1+start-10**(l1-1)))
    reach = ndigs/2
    acum = 0
    for e in range(start+1, end+1):
        acum+=len(str(e))
        if acum > reach:
            print(e-1)
            break
        if acum == int(reach):
            print(e)
            break
    return
def main():
    n1, n2 = lee_numeros()
    while n1 != 0:
        solve(n1, n2)
        n1, n2 = lee_numeros()

if __name__ == "__main__":
    main()