import csv
import sys
import re
from os.path import exists

source_file_path = 'AFTA-mal-url.csv';
buffer_file_path = 'AFTA-mal-url1.csv';
output_file_path = 'output/AFTA-mal-url.csv';
firepower_output_file = 'output/AFTA-mal-url.txt';
invalids_file_path = 'output/AFTA-mal-url-invalid.txt';

url_pattern = '^[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,256}\b([-a-zA-Z0-9()@:%_\+.~#?&\/\/=]*)$'
url_http_pattern = 'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,256}\b([-a-zA-Z0-9()@:%_\+.~#?&\/\/=]*)'

source_file_exists = exists(source_file_path)
#print(source_file_exists)

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

#print(headerLine)

rows = []
header = headerLine.split(',')

for row in dataLines:
    myrow = row.strip().split(',')
    rows.append(myrow)
    #print(myrow)


output = []
invalid = []
valid_count = 0
invalid_count = 0

print(rows[0][0])
print(re.fullmatch(url_pattern , rows[0][0]))

for rw in rows :
    url = rw[0]
    #print(url)
    if re.fullmatch(url_pattern , url) :
        valid_count = valid_count + 1
        output.append(rw)
        print(rw[0])
    else :
        #print(rw[0])
        invalid.append(rw)
        invalid_count = invalid_count + 1


print(valid_count)

