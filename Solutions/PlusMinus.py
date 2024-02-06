def plusMinus(arr):
    posVal=0
    negVal=0
    zeroVal=0
    for i in arr:
        if i>0:
            posVal+=1
        elif i<0:
            negVal+=1
        else:
            zeroVal+=1
    print(posVal/len(arr))
    print(negVal/len(arr))
    print(zeroVal/len(arr))