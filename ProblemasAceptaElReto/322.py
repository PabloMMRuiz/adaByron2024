def resSolve(palabra, i, j, memoria):
    if (i, j) in memoria:
        return memoria[(i, j)]
    if i == j:
        memoria[(i, j)] = palabra[i]
        return palabra[i]
    if i == j-1:
        return 2*palabra[i] if palabra[i]==palabra[j] else palabra[j]
    if palabra[i]==palabra[j]:
        memoria[(i, j)] = palabra[i]+resSolve(palabra, i+1, j-1, memoria)+palabra[j]
    else:
        matarIzq = resSolve(palabra, i+1, j, memoria)
        matarDer = resSolve(palabra, i, j-1, memoria)
        if len(matarIzq)>=len(matarDer):
            memoria[(i,j)] = matarIzq
        else:
            memoria[(i,j)] = matarDer
    return memoria[(i,j)]

def solve(palabra:str):
    memoria={}
    resSolve(palabra, 0, len(palabra)-1, memoria)
    print(memoria[(0, len(palabra)-1)])


def main():
    palabra = input()
    while palabra:
        solve(palabra)
        palabra=input()

if __name__ == "__main__":
    main()