if __name__ == '__main__':
    x = int(input())
    listaX = [ num for num in range(x+1) ]
    y = int(input())
    listaY = [ num for num in range(y+1) ]
    z = int(input())
    listaZ = [ num for num in range(z+1) ]
    n = int(input())

    result = [[i,j,k] for i in listaX for j in listaY for k in listaZ if i+j+k != n]
    print(result)