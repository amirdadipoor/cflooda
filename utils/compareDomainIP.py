import csv, json,base64
from os.path import exists
import os

csvfile="AFTA-mal-domain.csv"
jsonfile="AFTA-mal-domain.json"


csvFileExists = exists(csvfile)
jsonFileExists = exists(jsonfile)

if csvFileExists == False or jsonFileExists == False :
    print("input file not exists :(")
    exit
 

with open( csvfile , 'r') as fp:
    for count, line in enumerate(fp):
        pass
        
csvcount = count + 1
count = 0

with open( jsonfile , 'r') as fp:
    for count, line in enumerate(fp):
        pass

jsoncount = count + 1

compare = ( csvcount * 2 ) - 2 == jsoncount

print()
print('result for domain : \n')

print('Total json Lines', jsoncount )
print('Total csv Lines', csvcount  )
print('compare result', compare  )


#######################################################################


csvfile="AFTA-mal-ip.csv"
jsonfile="AFTA-mal-ip.json"


csvFileExists = exists(csvfile)
jsonFileExists = exists(jsonfile)

if csvFileExists == False or jsonFileExists == False :
    print("input file not exists :(")
    exit
 

with open( csvfile , 'r') as fp:
    for count, line in enumerate(fp):
        pass
        
csvcount = count + 1
count = 0

with open( jsonfile , 'r') as fp:
    for count, line in enumerate(fp):
        pass

jsoncount = count + 1

compare = ( csvcount * 2 ) - 2 == jsoncount

print()
print('result for ip : \n')

print('Total json Lines', jsoncount )
print('Total csv Lines', csvcount  )
print('compare result', compare  )

#print(count)

