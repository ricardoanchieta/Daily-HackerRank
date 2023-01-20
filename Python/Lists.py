if __name__ == '__main__':
    N = int(input())

    myList = []
    
    for i in range(N):
        entrada = input()
        if("print" in entrada):
            print(myList)
        elif("insert" in entrada):
            elementos = entrada.split(" ")
            elmInserir = int(elementos[2])
            index = int(elementos[1])
            myList.insert(index,elmInserir)
        elif("remove" in entrada):
            elementos = entrada.split(" ")
            elmRemover = int(elementos[1])
            myList.remove(elmRemover)
        elif("append" in entrada):
            elementos = entrada.split(" ")
            elmAppend = int(elementos[1])
            myList.append(elmAppend)
        elif("sort" in entrada):
            myList.sort()
        elif("pop" in entrada):
            myList.pop()
        elif("reverse" in entrada):
            myList.reverse()
        
            