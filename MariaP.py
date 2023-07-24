def sum1(*args):
    total = 0
    for x in args:
        total += float(x)
    print("Сума:", total)