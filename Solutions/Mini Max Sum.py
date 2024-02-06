def miniMaxSum(arr):
    arraySorted = sorted(arr)
    maxNum = arraySorted[1] + arraySorted[2] + arraySorted[3] + arraySorted[4]
    minNum = arraySorted[0] + arraySorted[1] + arraySorted[2] + arraySorted[3]
    print(str(minNum) + " " + str(maxNum))
