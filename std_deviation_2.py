import csv
import math

with open('/Users/prathamarora/Downloads/Python_Projects/Standard_deviation-master/solution/data3.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]
total = 0
length_of_data = len(data)

for i in data:
    total = total + int(i)
    
mean = total / length_of_data

squared_list = []
for i in data:
    d = int(i) - mean
    d = d**2
    squared_list.append(d)

Sum = 0

for i in squared_list:
    Sum = Sum + i

result = Sum / ( length_of_data - 1 )

std_deviation = math.sqrt(result)
print(f'Standard Deviation : {std_deviation}')