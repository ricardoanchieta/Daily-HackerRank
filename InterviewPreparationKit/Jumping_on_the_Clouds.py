
def jumpingOnClouds(c):
    aux = 0
    stepCount = 0
    while(aux != len(c) -1 ):
        
        if(len(c) >= 3):
            oneFoward = c[aux + 1]
            try:
                twoFoward = c[aux + 2] 
            except:
                aux = aux + 1
                stepCount = stepCount + 1
                continue

            if(oneFoward == 0 and twoFoward == 0):
                aux = aux + 2
                stepCount = stepCount + 1
            elif(oneFoward == 0 and twoFoward ==1):
                aux = aux + 1
                stepCount = stepCount + 1
            elif(oneFoward == 1 and twoFoward == 0):
                aux = aux + 2
                stepCount = stepCount + 1
        else:
            return 1;
    return stepCount
