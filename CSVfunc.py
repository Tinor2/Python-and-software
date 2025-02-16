#CSV functions
import csv
def csvTdict(filename, columnsToProcess = 1, valIntegers = False):
  with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile)
    data = {}
    for row in reader:
      key= row[0]
      key = key.lower()
      valueList = []
      for i in range(columnsToProcess):
        i+= 1
        if valIntegers:
          valueList.append(int(row[i]))
      if len(valueList) == 1:
        value = valueList[0]
      else:
        value = valueList
      data[key] = value
    return data
def csvTlist(filename):
  with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile)
    data = []
    for row in reader:
      key= row[0]
      key = key.lower()
      data.append(key)
    return data
def listTcsv(lists:list, filename):
   filename = filename+".csv"
   with open(filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(lists)
def dictTcsv(dictionary, filename):
   filename = filename+".csv"
   with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for key, value in dictionary.items():
      if isinstance(value, list):
        row = [key] + value
      else:
        row = [key, value]
      writer.writerow(row)
def gridTcsv(grid,filename):
  filename += ".csv"
  with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([grid])