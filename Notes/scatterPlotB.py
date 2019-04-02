import csv
import matplotlib.pyplot as plt
import numpy as np

with open("data/World firearms murders and ownership - Sheet 1.tsv") as f:
    reader = csv.reader(f, delimiter="\t")
    data = list(reader)

print(data)
headers = data.pop(0)

print(headers)

homicide_per_100k = []
firearm_per_100 = []
comps = ["Australia", "Austria", "Belgium", "Canada", "Croatia", "Denmark", "England and Wales", "France", "Germany", "Iceland", "Ireland", "Italy", "India", "Japan", "Korea, South", "Singapore", "Spain", "Sweden", "Taiwan", "Switzerland", "United States", "Turkey"]
countries = []


for country in data:
    if country[0] in comps:
        try:
            homicides = float(country[5])
            firearms = float(country[-2])
            name = country[0]
            homicide_per_100k.append(homicides)
            firearm_per_100.append(firearms)
            countries.append(name)
        except ValueError:
            print(country[0], "had incomplete data")

print(countries)
print(homicide_per_100k)
print(firearm_per_100)

plt.figure(1, figsize=(12, 6))
plt.scatter(firearm_per_100, homicide_per_100k)

# best fit line
m, b = np.polyfit(firearm_per_100, homicide_per_100k, 1)
fit_x = [0, 100]
fit_y = [b, m * 100 + b]

plt.plot(fit_x, fit_y, color="red")
plt.title("Homicides vs. Gun Ownership by Country")
plt.xlabel("Firearms per 100 people")
plt.ylabel("Homicides by firearm per 100k people")

plt.annotate("My text", xy=(40, 2))

for i in range(len(countries)):
    plt.annotate(countries[i], xy=(firearm_per_100[i], homicide_per_100k[i]))

for i in countries:
    print(i)


plt.show()