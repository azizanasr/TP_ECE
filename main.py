#creation de la liste
#affectation
maListe1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(maListe1)
#boucle for
maListe2 = []
for i in range (14):
    maListe2.append(i)
print(maListe2)
#boucle While
maListe3 = []
i=0
while (i<14):
    maListe3.append(i)
    i=i+1
print(maListe3)
#liste de compréhension
maListe4 = [i for i in range(14)]
print(maListe4)
