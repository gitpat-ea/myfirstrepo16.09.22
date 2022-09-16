with open('input.txt','r') as pobed:
    max9 = -1
    max10 = -1
    max11 = -1
    for line in pobed:
        normline = line.rstrip().split()
        if int(normline[2]) == 9:
            if int(normline[3]) > max9:
                max9 = int(normline[3])
        elif int(normline[2]) == 10:
            if int(normline[3]) > max10:
                max10 = int(normline[3])
        elif int(normline[2]) == 11:
            if int(normline[3]) > max11:
                max11 = int(normline[3])
    print(max9,max10,max11)