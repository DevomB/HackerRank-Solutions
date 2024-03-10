def compareTriplets(a, b):
    aPoints = 0
    bPoints = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            aPoints += 1
        elif b[i] > a[i]:
            bPoints += 1
            
    return [aPoints,bPoints]