with open('input.txt','r') as pobed:
    participants = []
    names = []
    table = []
    for line in pobed:
        normline = line.rstrip().split()
        participants.append(normline)
    #print(participants)
    for person in participants:
        names.append(person[0])
    names.sort()
    #print(names)
    for i in range(len(names)):
        for j in range(len(names)):
            if names[i] == participants[j][0]:
                table.append(participants[j])
    for i in range(len(table)):
        print(table[i][0],table[i][1],table[i][3])