with open('input.txt','r') as pobed:
    s9 = 0
    s10 = 0
    s11 = 0
    c9 = 0
    c10 = 0
    c11 = 0
    for line in pobed:
        normline = line.rstrip().split()
        if int(normline[2]) == 9:
            s9 += int(normline[3])
            c9+=1
        elif int(normline[2]) == 10:
            s10 += int(normline[3])
            c10+=1
        elif int(normline[2]) == 11:
            s11 += int(normline[3])
            c11+=1
    print(s9/c9,s10/c10,s11/c11)