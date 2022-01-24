import csv
import pandas 
file2 = 'Book1.csv'  #address of log file in csv format

file = "WhatsApp Chat with MIT BENGALURU.txt" # address of wahtsap log txt file

accept = open(file2,'w')
write = csv.writer(accept,lineterminator='\n') #csv writer object created
log = open(file,'r')
logs = log.readlines()


records = []


for i in logs:
    line = i
    if (line[0] in ('0','1','2','3','4','5','6','7','8','9')) and (line[2]=='/' and line[5]=='/'): #conditon for selecting only the records having dates and no other text
        lineli = line.split('-')
        part1 = lineli[0].strip() 
        part2 = lineli[1].strip()
        part1li = part1.split(',')
        part2li = part2.split(':')
        date = part1li[0].strip()
        time = part1li[1].strip()
        author = part2li[0].strip()
        rec = (date,time,author)
        records.append(rec)  #this will append all the individual values inside the records list variable
        write.writerow(rec) # entry of each and every record into the csv sheet

print("all records inserted")
    
accept.close()
log.close()


dates = []
for i in records:
    if i[0] not in dates:
        dates.append(i[0])

names = []
for i in records:
    if i[2] not in names:
        names.append(i[2])

final_log=[]

#DONOT REMOVE THE QUOTES PLEJ
"""
for i in records: 
    for j in dates:
        for k in names:
            count = 0 
            if i[0]==j and i[2]==k:
                count+=1
"""


for i in dates:
    date = []
    for j in names:
        count = 0
        for k in records:
            if k[0]==i and k[2]==j:
                count+=1
        name = (j,count)
        date.append(name)
    entry=(i,date)
    final_log.append(entry)


 
data = pandas.DataFrame() 
data['Date'] = final_log[0::3]
data['Date2'] = final_log[1::3]
data['Date3'] = final_log[2::3]
data.to_excel('report.xlsx', index = False) 

        
    
    
