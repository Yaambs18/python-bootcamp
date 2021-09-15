import csv

data = open('example.csv')
csv_data = csv.reader(data)
data_lines = list(csv_data)
print(data_lines[0])

for line in data_lines[:7]:
    print(line)

for line in data_lines[1:10]:
    print(line[3])

full_name = []

for line in data_lines[1:5]:
    full_name.append(line[1]+" "+line[2])
print(full_name)

# writing a file

file_to_output = open('to_save_file.csv','w',newline='')
csv_writer = csv.writer(file_to_output,delimiter=',')
csv_writer.writerow(['a','b','c'])
csv_writer.writerows([['1','2','3'],['4','5','6']])
file_to_output.close()

f = open('to_save_file.csv','a',newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(['new','new','new'])
f.close()
 