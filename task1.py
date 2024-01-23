with open('input.txt') as file:
    n, t = file.readline().split()
    n = int(n)
    t = int(t)
    mas = sorted(list(map(int, file.readline().split())))
    c = 0
    for num in mas:
        if t - num >= 0:
            c += 1
            t -= num
        else:
            break
    print(c)