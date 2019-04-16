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
countries = ["United States", "New Zealand", "Canada", "South Korea", "Japan", "England and Wales", "Netherlands", "France", "Nigeria", "Belgium", "Germany", "Taiwan", "Singapore", "Hungary", "Denmark", "Finland", "Spain", "Iceland", "Switzerland"]
countries_label = []

for country in data:
    if country[0] in countries:
        try:
            homicides = float(country[5])
            firearms = float(country[-2])
            name = country[0]
            homicide_100k.append(homicides)
            firearms_100.append(firearms)
            countries_label.append(name)
        except:
            print(country[0], "data is inadequate")

print(homicide_100k)
print(firearms_100)
print(countries)

plt.figure(1, figsize=(12, 6))
plt.scatter(firearms_100, homicide_100k)
plt.ylabel("homicides per 100k population")
plt.xlabel("firearms per 100 people")
plt.title("Homicides vs. Gun Ownership by Country")

# make a best fit line
m, b = np.polyfit(firearms_100, homicide_100k, 1)

fit_x = [0, 100]
fit_y = [b, 100 * m + b]

plt.annotate("My Text", xy=(40, 2))

print(len(firearms_100), len(homicide_100k), len(countries))

for i in range(len(countries_label)):
    plt.annotate(countries_label[i], xy=(firearms_100[i], homicide_100k[i]), arrowprops={width:10})


plt.plot(fit_x, fit_y, color="red")

plt.show()