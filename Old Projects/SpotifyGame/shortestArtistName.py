import csv
def csv_to_dict(filename):
  with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile)
    data = {}
    for row in reader:
      key, value = row
      key = key.lower()
      data[key] = value
    return data
data = csv_to_dict("Artistrankings.csv")
memory = ["drake"]

for name in data:
    name = str(name)
    if len(name) < len(memory[0]):
        memory = [name]
    elif len(name) == len(memory[0]):
        memory.append(name)

print(memory)

