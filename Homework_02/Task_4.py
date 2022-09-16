with open('input.txt','r') as tekst:
    spisok = tekst.readlines()
    for el in range(len(spisok)):
        print(spisok[len(spisok)-1-el])