import csv

#create a CSV file
'''
nume=["nume","prenume","id"]
lista=[["dejanu","alex",1],["roby","roberto",2]]


f=open("date.csv","wb")
objCSV=csv.writer(f,delimiter=',',quotechar="'", quoting=csv.QUOTE_ALL)

objCSV.writerow(nume)
objCSV.writerows(lista)

f.close()
'''

#read a CSV file
f=open('pin.csv','rb')
#reader=csv.reader(f,delimiter=",",quotechar="'",quoting=True)
reader=csv.reader(f,delimiter=",",quoting=True)
lista=list(reader)
print(lista)
f.close()


#convert from text to csv
with open(sys.argv[1], 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('renameit.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('title', 'intro'))
        writer.writerows(lines)
