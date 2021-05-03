import os
import csv


with open('data.csv', mode='a', newline='', encoding='utf-8') as csvf:
        csv_writer = csv.writer(csvf, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['id','text'])
# for file in os.listdir('_GA_Results'):
#     print(file)
for i in os.listdir('dataset'):
        with open('dataset/'+i,encoding="utf8") as f:
                
                lines=f.readlines()
                lines = map(lambda s: s.replace('\n', ''), lines)
                lines = filter(lambda s: s != '', lines)
                lines = list(lines)
                lines=lines[4:]
#print(lines)
        with open('data.csv', mode='a', newline='', encoding='utf-8') as csvf:
                csv_writer = csv.writer(csvf, delimiter=',',
                                        quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for i in range(len(lines)):
                        id=i
                        row=[id,lines[i]]
                        csv_writer.writerow(row)

