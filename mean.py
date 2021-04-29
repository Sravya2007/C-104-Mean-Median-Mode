#List of elements to calculate mean
import csv

with open('C:/Users/sravy/White Hat Jr/C 104- Mean, Median, Mode/SOCR-HeightWeight.csv', newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data = []

#Sorting data to get the height of people
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))

#Getting the mean
n = len(new_data)
total = 0

for x in new_data:
    total += x

mean = total / n
print("Mean / Average is: " + str(mean))