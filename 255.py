def solve(line):
    maxLentgh = 0
    #ideas: abrir palindromo centrado en cada letra
    #memoria para lo anterior: si encontramos un palindromo x largo ya sabemos lo que pasa a sus lados
    #y tambien empezamos a comprobar palindromia a partir de centro + x y luego hacia dentro
    #sliding window? suena muy ineficiente
def main():
    line = input()
    while line:
        solve(line)
        line = input()

if __name__ == "__main__":
    main()