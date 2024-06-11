from collections import defaultdict
def lee_numero():
    return int(input())

def lee_numeros():
    return list(map(int, input().split()))

def solve(ls:list):
    innitSum = sum(ls)
    best = innitSum
    leftSum = 0
    rightSum = innitSum
    day = 0
    bestDay = 0
    while day < len(ls):
        leftSum+=ls[day]
        rightSum-=ls[day]
        if abs(rightSum-leftSum)<best:
            best = abs(rightSum-leftSum)
            bestDay=day+1
        day+=1
    if best == innitSum:
        print(0)
    else:
        print(bestDay)

def main():
    n = lee_numero()
    while n != 0:
        solve(lee_numeros())
        n=lee_numero()

if __name__ == "__main__":
    main()