for x in range (0,2):
    for y in range (0,2):
        for z in range (0,2):
            a = not (x or y or z)
            b = not x and not y and not z
            if a == b:
                print(x, y, z)
