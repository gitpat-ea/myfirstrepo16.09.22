with open('input.txt','r') as pobed:
    max = -1
    estpobed = [0]*99
    schools = []
    for line in pobed:
        normline = line.rstrip().split()
        if int(normline[3]) > max:
            max = int(normline[3])
    with open('input.txt', 'r') as pobed:
        for line in pobed:
            normline = line.rstrip().split()
            if int(normline[3]) == max:
                if estpobed[int(normline[2])] == 0:
                    schools.append(int(normline[2]))
                    estpobed[int(normline[2])] += 1
        for school in schools:
            print(int(school), end = ' ')