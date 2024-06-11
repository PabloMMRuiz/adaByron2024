def lee():
    return input()

def solve(line: str):
    line = str.lower(line)
    line = str.replace(line, ' ', '')
    for i in range(len(line)):
        if line[i] != line[-(i+1)]:
            print("NO")
            return
    print("SI")

def main():
    line = lee()
    while line != "XXX":
        solve(line)
        line = lee()

if __name__ == "__main__":
    main()