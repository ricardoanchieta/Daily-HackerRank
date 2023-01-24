
def swap(arr, num, index):
    aux = arr[num-1]
    arr[num-1] = arr[index]
    arr[index] = aux

def minimumSwaps(arr):
    swapsCount = 0
    for index in range(len(arr)):
        num = arr[index]
        while(num != index +1):
            swap(arr,num,index)
            num = arr[index]
            swapsCount = swapsCount + 1
    return swapsCount