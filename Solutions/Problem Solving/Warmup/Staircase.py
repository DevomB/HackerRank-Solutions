def staircase(n):
    for i in range(n):
        whiteSpace = ' ' * (n - (i+1))
        hashSpace = '#' * (i+1)
        print(whiteSpace+hashSpace)
