import csv

x = []
with open("/home/miriam/Relaying-Active-Connectivity-with-UAV/rssi5_constantReading.csv", 'r') as csvfile:
    data = csv.reader(csvfile)

    for row in data:
        x.append(int(row[1]))

    count = 0
    for i in range(1, len(x)):
        x[i] += 60*count
        if x[i] < x[i-1]:
            count += 1
            x[i] += 60

    sub = x[0]
    for i in range(len(x)):
        x[i] -= sub

print(x)