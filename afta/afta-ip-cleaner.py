import csv
from os.path import exists
import re

source_file_path = "./AFTA-mal-ip.csv";
buffer_file_path = "AFTA-mal-ip1.csv";
destination_file_path = "./output/AFTA-mal-ip.csv"
fw_destination_file_path = "./output/AFTA-FW-mal-ip.txt"


file_exists = exists(source_file_path);
ip_pattern = "(?<![0-9])(?:(?:[0-1]?[0-9]{1,2}|2[0-4][0-9]|25[0-5])[.](?:[0-1]?[0-9]{1,2}|2[0-4][0-9]|25[0-5])[.](?:[0-1]?[0-9]{1,2}|2[0-4][0-9]|25[0-5])[.](?:[0-1]?[0-9]{1,2}|2[0-4][0-9]|25[0-5]))(?![0-9])";

if (file_exists == False):
    print("Source File is Not Exists ");
    exit();

# type(file)

#
#bufferFile = open(buffer_file_path, "w")

#for line in text:
#    print(line)
    #line = line.replace(',"', ',')
#    bufferFile.writelines(line)

#bufferFile.close()


text = open(source_file_path , "r")
text = ''.join([i for i in text])
text = text.replace(',"', ',')
x = open(buffer_file_path, "w")
x.writelines(text)
x.close()

source_file = open(buffer_file_path)
csvreader = csv.reader(source_file)
header = []
header = next(csvreader)

rows = []
ipclean = []
for row in csvreader:
    rows.append(row)

valid_count = 0;
invalid_count = 0;

for row in rows:
    ip = row[0]
    reason = row[1]
    refrence = row[2]

    ip_match = re.fullmatch(ip_pattern, ip)
    if (ip_match):
        valid_count = valid_count + 1
        valid_array = [ip, reason, refrence];

        ipclean.append(valid_array)
        print(valid_array)
        # print('\n')
    else:
        invalid_count = invalid_count + 1
        # print(ip)

    # if '\"' in refrence :
    #    print(refrence)

# print(ipclean[len(ipclean)-1]);
print(valid_count)

with open(destination_file_path, 'w', newline="" , encoding='utf-8') as output_file:
    csvwriter = csv.writer(output_file , lineterminator='\n') # 2. create a csvwriter object
    csvwriter.writerow(header) # 4. write the header
    csvwriter.writerows(ipclean) # 5. write the rest of the data
    output_file.close()

fw_output_file = open(fw_destination_file_path, "w" , newline="" )
for row in ipclean :
    fw_output_file.write(row[0] + '\n')

fw_output_file.close()



