import matplotlib.pyplot as plt
import csv

x = []
y = []

with open("/home/miriam/Desktop/rssi12.csv", 'r') as csvfile:
    plots = csv.reader(csvfile)

    for row in plots:
        y.append(int(row[0]))
        x.append(row[1])

#plt.figure(figsize=(8,6))
plt.scatter(x,y, color="mediumpurple")
plt.title(" ")
plt.box(False)
plt.xticks([1,5,10,15,20,25,30])
plt.xlabel('time')
plt.ylabel('RSSI')
plt.show()
