# PLOTTING (with matplotlib)

import matplotlib.pyplot as plt
import random
import matplotlib.ticker as tkr

plt.figure(1)  # create a new window

plt.plot([1, 2, 4, 4])  # plots y against the index
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])  # plot(x_data, y_data)

plt.figure(2)  # makes a second window


x1 = [x for x in range(1, 101)]
y1 = [y ** 2 for y in x1]

plot1 = plt.plot(x1, y1)

x2 = [x for x in range(1, 101)]
y2 = [random.randrange(1000) for y in range(100)]

plot2 = plt.plot(x2, y2, color='green', marker='o', markersize=10, linestyle='--', alpha=0.5, label="PLOT2")



# title axes label unit numbers key
plt.xlabel('time (seconds)', color='red', fontsize=20)
plt.ylabel('excitement level (Yays!)')
plt.title('Example Plot')
plt.axis([0, 50, 0, 1000])  # [xmin, xmax, ymin, ymax]

#plt.show()


# Pretend I am starting a new file

import csv
import matplotlib.pyplot as plt

with open("data/Libraries_-_2018_Visitors_by_Location.csv") as f:
    reader = csv.reader(f)  # make a reader object to pull in the data
    data = list(reader)  # cast the reader as a list







header = data.pop(0)  # header info including months
print(header)
data.sort(key=lambda x: int(x[-1]))
print(data)
data.pop(-1)


library_names = [x[0] for x in data]
monthly_data = [x[1:-1] for x in data]
print(library_names)

lp_data = monthly_data[library_names.index('Lincoln Park')]
print(lp_data)

try:
    lp_data = [int(x) for x in lp_data]
except:
    print("couldn't convert the data val to int")

print(lp_data)

months = [x for x in header[1:-1]]


plt.figure(3, tight_layout=True)
plt.axis([0, 12, 0, 18000])
plt.plot(lp_data)
month_numbers = [x for x in range(12)]

plt.xticks(month_numbers, months, rotation=45)  # puts text on axis


# Let's plot every library YTD attendance as a bar graph
print("\n" * 10)

fig = plt.figure(4, tight_layout=True, figsize=(14, 6))

print(library_names)# x axis list is library names
library_numbers = [x for x in range(len(library_names))]
print(library_numbers)

try:
    library_ytd = [int(x[-1]) for x in data]# y axis list is the YTD
except:
    print("could not convert to int")

my_plot = plt.bar(library_numbers, library_ytd, 0.2, alpha=0.8, color='darkgreen', edgecolor='hotpink', facecolor='blue', label="Visitors")
plt.xticks(library_numbers, library_names, rotation=90, fontsize=8)

plt.ylabel("Total Visitors")
plt.title("Chicago Public Library Visitors (2018)", fontsize=30)

plt.legend()

axis = fig.gca()
axis.yaxis.set_major_formatter(tkr.FuncFormatter(lambda x, p: "{:.2e}".format(x)))

plt.show()




