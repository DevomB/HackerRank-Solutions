def birthday(s, d, m):
    numberMatch  = 0
    for i in range(len(s) - m + 1):
        if sum(s[i:i+m]) == d:
            numberMatch += 1
    return numberMatch