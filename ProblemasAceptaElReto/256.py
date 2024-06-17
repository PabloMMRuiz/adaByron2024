def lee_linea():
    return list(input().split())

def solution(data: list):
    a = data[0]
    b = data[1]
    c = data[2]
    res = ""
    if (len(a) == len(b) and len(a) == len(c)):
        for i in range(len(a)):
            if(a[i] == b[i] or a[i] == c[i]):
                res+=(a[i])
            elif(b[i] == c[i]):
                res+=(b[i])
            else:
                res = "RUIDO COSMICO"
                break

    elif (len(a)>len(b)): #b es mas corto
        ins = False #no se ha insertado b
        for i in range(len(a)):
            if(a[i] == c[i]):
                res+=(a[i])
            elif(not ins):
                res+=(b)
                if res[i] != a[i] and res[i] != b[i]:
                    res = "RUIDO COSMICO"
                    break
                ins = True
            else:
                if res[i] != a[i] and res[i] != c[i]:
                    res = "RUIDO COSMICO"
                    break
            
    
    elif (len(a)>len(c)): #c es mas corto
        ins = False #no se ha insertado c
        for i in range(len(a)):
            if(a[i] == b[i]):
                res+=(a[i])
            elif(not ins):
                res+=(c)
                if res[i] != a[i] and res[i] != b[i]:
                    res = "RUIDO COSMICO"
                    break
                ins = True
            else:
                if res[i] != a[i] and res[i] != b[i]:
                    res = "RUIDO COSMICO"
                    break

    else: #a es mas corto
        ins = False #no se ha insertado a
        for i in range(len(b)):
            if(c[i] == b[i]):
                res+=(b[i])
            elif(not ins):
                res+=(a)
                if res[i] != a[i] and res[i] != b[i]:
                    res = "RUIDO COSMICO"
                    break
                ins = True
            else:
                if res[i] != c[i] and res[i] != b[i]:
                    res = "RUIDO COSMICO"
                    break
    
    print(res)

def main():
    while True:
        datos = lee_linea()
        if len(datos) == 3:
            solution(datos)
        else:
            break

if __name__ == "__main__":
    main()