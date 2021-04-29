import csv

with open('C:/Users/sravy/White Hat Jr/C 104- Mean, Median, Mode/SOCR-HeightWeight.csv', newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data = []

#Sorting the data to get the height of people
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))

n = len(new_data)
new_data.sort()

#Using floor division to get the nearest whole number
#Floor division is shown by //
if(n % 2 == 0):
    #Getting the first number
    median1 = float(new_data[n//2])
    median2 = float(new_data[n//2 - 1])
    #Getting mean of those numbers
    median = (median1 + median2)/2
else:
    median = new_data[n//2]
    print(n)

print("Median is " + str(median))