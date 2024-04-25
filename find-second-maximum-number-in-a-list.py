if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    x  = set(arr)
    print(list(x)[-2])
