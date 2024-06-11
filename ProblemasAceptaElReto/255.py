#recibe cadenas y hay que indicar la longitud de la subcadena palindroma mas larga

def solution(cad: str):
    res = 0
    l_act = 0
    for i in range(len(cad)):
        #primero contemos la subcadena formada por letras iguales
        l_act = 1
        k = 1
        while i+k<len(cad) and cad[i] == cad[i+k]:
            l_act+=1
            k+=1

        k-=1 #cuando sale del bucle de arriba la k ya esta en la siguiente letra a la subcadena de letras iguales
        j=1
        while i-j>=0 and i+k+j<len(cad):
        #vamos comprobando si podemos prolongar el palindromo
            if cad[i-j] == cad[i+k+j]:
                l_act+=2
                j+=1
            else: break

        if l_act>res:
            res = l_act
    print(res)

def main():
    while True:
        cad = str(input())
        if cad != "":
            solution(cad)
        else: break

if __name__ == "__main__":
    main()