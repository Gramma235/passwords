from collections import Counter
with open('pwd.txt') as f:
    dataList = [ line.split(';') for line in f ]

passList = [item for sublist in dataList for item in sublist]
del passList[0]

for i in range(len(passList)):
    try:
        if passList[i][-1]!='n':
            del passList[i]
    except IndexError:
        pass


for i in range(len(passList)):
    try:
        passList[i]=passList[i][0:-1]
    except IndexError:
        pass

passOften = Counter(passList).most_common(10)
passwords=[]
for i in range(10):
    passwords.append(passOften[i])
for i in range(10):
    print(i+1,'. ',passwords[i][0],' (',passwords[i][1],' раз)',sep='')




