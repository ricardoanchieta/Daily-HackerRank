if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    
    ganhador = max(arr)
    numGanhadores = arr.count(ganhador)
    
    for x in range(numGanhadores):
        arr.remove(ganhador)

    vice = max(arr)
    print(vice)