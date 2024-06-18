from collections import deque
def lee_nums():
    return list(map(int, input().split()))


def solve(line: list):
    start = line[0]
    end = line[1]
    queue = deque()
    queue.append((start,0))
    visited = set()
    visited.add(start)
    while queue:
        current = queue.popleft()
        pasos = current[1]
        current = current[0]
        if current==end:
            print(pasos)
            return
        else:
            #Las tres operaciones nos dan 3 nuevos nodos
            suma = current+1 % 10000
            multi = current*2 % 10000
            divi = current//3
            if suma not in visited:
                visited.add(suma)
                queue.append((suma, pasos+1))
            if multi not in visited:
                visited.add(multi)
                queue.append((multi, pasos+1))
            if divi not in visited:
                visited.add(divi)
                queue.append((divi, pasos+1))
    

def main():
    line = lee_nums()
    while line:
        solve(line)
        line = lee_nums()

if __name__ == "__main__":
    main()