""" Task

Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function. """

def is_leap(year):
    leap = False
    
    fistCondition = year%4 == 0
    secondCondition = year%100 ==  0
    thirdCondition = year%400 == 0

    if(fistCondition and not secondCondition):
        leap = True
    elif(fistCondition and secondCondition and thirdCondition):
        leap = True
    else:
        leap = False

    return leap

year = int(input())
print(is_leap(year))