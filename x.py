import csv
with open('pelis.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    data={}
    for row in spamreader:
        print row
        data[row[0]]=row[6]
    print data
