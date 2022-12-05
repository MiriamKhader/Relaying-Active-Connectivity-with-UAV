import matplotlib.pyplot as plt
import csv

x = []
y = []

with open("/home/miriam/Relaying-Active-Connectivity-with-UAV/rssi3_flying_lp1_lp3.csv", 'r') as csvfile:
    plots = csv.reader(csvfile)

    for row in plots:
        y.append(int(row[0]))
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


plt.box(None)
plt.scatter(x,y, color="mediumpurple")
plt.plot(x,y)
plt.axvspan(-2, 50, facecolor='orchid', alpha = 0.5, label="initial")
plt.axvspan(50, 60, facecolor='coral', alpha = 0.35, label="Flying")
#plt.axvspan(82, 190, facecolor='aquamarine', alpha = 0.5, label="Crashing")

plt.title("RSSI between two stationary launchpads")
plt.legend(facecolor="white")
plt.xlabel('Time')
plt.ylabel('RSSI')
plt.show()
