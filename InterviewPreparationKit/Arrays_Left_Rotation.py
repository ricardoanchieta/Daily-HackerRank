""" Complete the function rotLeft in the editor below.

rotLeft has the following parameter(s):

int a[n]: the array to rotate
int d: the number of rotations

Returns

int a'[n]: the rotated array """

def rotLeft(a, d):
    lista = list(a)
    for roda in range(d):
        elmGirado = lista[0]
        lista.pop(0)
        lista.append(elmGirado)
    return lista
