import csv
import sys
import re
from os.path import exists
#  pip install tld
from tld import get_tld
from tld import *
from tld.utils import update_tld_names

#uncomment when you update and sync 
update_tld_names()


source_file_path = 'AFTA-mal-domain.csv'
buffer_file_path = 'AFTA-mal-domain1.csv'
output_file_path = 'output/AFTA-mal-domain.csv'
firepower_output_file = 'output/AFTA-mal-domain.txt'
invalid_file_path = 'output/AFTA-mal-domain-invalid.txt'

domain_pattern = '^[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,256}$'
url_pattern = '[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,256}\b([-a-zA-Z0-9()@:%_\+.~#?&\/\/=]*)'
url_http_pattern = 'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,256}\b([-a-zA-Z0-9()@:%_\+.~#?&\/\/=]*)'


source_file_exists = exists(source_file_path)

if source_file_exists == False :
    print ('AFTA file is not exists')

inputFile = open(source_file_path , 'rt')
data = inputFile.read()
data = data.replace('\"', '')
inputFile.close()
bufferFile = open(buffer_file_path,'wt' , newline='\n')
bufferFile.write(data)
bufferFile.close()

#csv.field_size_limit(sys.maxsize)
bufferFile = open(buffer_file_path , 'rt')
headerLine = bufferFile.readline().strip()
dataLines = bufferFile.readlines()


#headerLine.replace('\n', '')

rows = []
header = headerLine.split(',')

for row in dataLines:
    myrow = row.strip().split(',')
    rows.append(myrow)
    #print(myrow)

#print(header)
#for line in Lines:
#csvreader = csv.reader(bufferFile)
#header = []
#header = next(csvreader)
#print(header)
#print(rows)

output = []
invalid = []
valid_count = 0
invalid_count = 0

for rw in rows :
    domain = rw[0]
    if re.fullmatch(domain_pattern , domain):
        try:
            valid_count = valid_count + 1
            newRow = []
            #fld = ;
            newRow.append(get_fld( domain , fix_protocol=True))
            newRow.append(rw[1])
            newRow.append(rw[2])
            # print(newRow)
            # rw[0] = fld
            output.append( newRow )
        except:
            invalid.append(rw)
            invalid_count = invalid_count + 1
    else :
        #print(rw[0])
        invalid.append(rw)
        invalid_count = invalid_count + 1


print(valid_count)

with open(output_file_path, 'w', newline="") as output_file:
    csvwriter = csv.writer(output_file,lineterminator="\n") # 2. create a csvwriter object
    csvwriter.writerow(header) # 4. write the header
    csvwriter.writerows(output) # 5. write the rest of the data

output_file.close()


with open(firepower_output_file, 'w') as firepower_file:
    for ro in output:
        firepower_file.write(ro[0])
        firepower_file.write('\n')
    firepower_file.close()


with open(invalid_file_path, 'w') as invalid_file:
    for ro in invalid:
        invalid_file.write(ro[0])
        invalid_file.write('\n')
    invalid_file.close()