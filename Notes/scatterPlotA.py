import csv
import matplotlib.pyplot as plt
import numpy as np

with open("data/World firearms murders and ownership - Sheet 1.tsv") as f:
    reader = csv.reader(f, delimiter="\t")
    data = list(reader)

print(data)

header = data.pop(0)
print(header)

# make a scatter of firearms_per_100 vs homicides_100k

homicide_100k = []
firearms_100 = []
countries = ["United States", "New Zealand", "Canada", "Mexico", "South Korea", "Japan", "England and Wales", "Netherlands", "France", "South Africa", "Nigeria", "Belgium", "Germany", "Taiwan", "Singapore", "Hungary", "Denmark", "Finland", "Spain", "Iceland", "Switzerland"]

for country in data:
    if country[0] in countries:
        try:
            homicides = float(country[5])
            firearms = float(country[-2])
            name = country[0]
            homicide_100k.append(homicides)
            firearms_100.append(firearms)
            countries.append(name)
        except:
            print(country[0], "data is inadequate")

print(homicide_100k)
print(firearms_100)
print(countries)

plt.figure(1)
plt.scatter(firearms_100, homicide_100k)
plt.ylabel("homicides per 100k population")
plt.xlabel("firearms per 100 people")

# make a best fit line
m, b = np.polyfit(firearms_100, homicide_100k, 1)

fit_x = [0, 100]
fit_y = [b, 100 * m]

plt.plot(fit_x, fit_y)

plt.show()