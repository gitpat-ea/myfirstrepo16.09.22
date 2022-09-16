with open('input.txt','r') as tekst:
    spisok = tekst.read()
    for el in range(len(spisok)-1):
        print(spisok[len(spisok)-2-el], end = '')