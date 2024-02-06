def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_count = sum(s <= a + apple <= t for apple in apples)
    oranges_count = sum(s <= b + orange <= t for orange in oranges)
    print(apples_count)
    print(oranges_count)
