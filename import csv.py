import csv
value = [(5,6),(7,8),(9,10)]
with open('e:\python\sairam.csv','w') as out:
  csv_out = csv.writer(out)
  csv_out.writerow(['name','number'])
  for row in value:
      csv_out.writerow(row)