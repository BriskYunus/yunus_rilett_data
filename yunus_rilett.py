import csv
import numpy as np
import matplotlib.pyplot as plt

categories = []
men = []
women = []
goldbefore2000 = []
goldafter2000 = []
silverbefore2000 = []
silverafter2000 = []
bronzebefore2000 = []
bronzeafter2000 = []
chinaGold = []
usaGold = []
chinaSilver = []
usaSilver = []
chinaBronze = []
usaBronze = []


with open('data/medal_data.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0:
            print('pushing categories into seperate array')
            categories.append(row)
            line_count += 1
        else:
            yearData = row[0]
            countryData = row[4]
            sportData = row[5]
            medalData = row[7]

            if countryData == "USA":
                if sportData == "Men":
                    men.append(sportData)
                else:
                    women.append(sportData)
                
                if medalData == "Gold":
                    if int(yearData) < 2000:
                        goldbefore2000.append(medalData)
                    else:
                        goldafter2000.append(medalData)

                if medalData == "Silver":
                    if int(yearData) < 2000:
                        silverbefore2000.append(medalData)
                    else:
                        silverafter2000.append(medalData)

                if medalData == "Bronze":
                    if int(yearData) < 2000:
                        bronzebefore2000.append(medalData)
                    else:
                        bronzeafter2000.append(medalData)


            if medalData == "Gold":
                if countryData == "CHN":
                    chinaGold.append(medalData)
                if countryData == "USA":
                    usaGold.append(medalData)

            if medalData == "Silver":
                if countryData == "CHN":
                    chinaSilver.append(medalData)
                if countryData == "USA":
                    usaSilver.append(medalData)

            if medalData == "Bronze":
                if countryData == "CHN":
                    chinaBronze.append(medalData)
                if countryData == "USA":
                    usaBronze.append(medalData)
            
            line_count += 1

print('processed', line_count, 'lines of data')
#print(categories)
print("CHN Gold before and after")
goldbefore = goldbefore2000.count("Gold")
print(goldbefore)
goldafter = goldafter2000.count("Gold")
print(goldafter)

print("CHN Silver before and after")
silverbefore = silverbefore2000.count("Silver")
print(silverbefore)
silverafter = silverafter2000.count("Silver")
print(silverafter)

print("CHN Bronze before and after")
bronzebefore = bronzebefore2000.count("Bronze")
print(bronzebefore)
bronzeafter = bronzeafter2000.count("Bronze")
print(bronzeafter)

print("Men vs Women")
print(men.count("Men"))
print(women.count("Women"))

print("CHN vs USA Gold")
print(chinaGold.count("Gold"))
print(usaGold.count("Gold"))

print("CHN vs USA Silver")
print(chinaSilver.count("Silver"))
print(usaSilver.count("Silver"))

print("CHN vs USA Bronze")
print(chinaBronze.count("Bronze"))
print(usaBronze.count("Bronze"))


totalGold = goldafter2000.count("Gold") + goldbefore2000.count("Gold")

totalSilver = silverafter2000.count("Silver") + silverbefore2000.count("Silver")
totalBronze = bronzeafter2000.count("Bronze") + bronzebefore2000.count("Bronze")


print("USA Men vs Women in Olympics Ice Hockey %")
totalMetal = men.count("Men") + women.count("Women")
men_percent = men.count("Men") / totalMetal * 100
print(men_percent)
women_percent = 100 - men_percent
print(women_percent)

print("CHN vs USA Gold %")
totalG = chinaGold.count("Gold") + usaGold.count("Gold")
chinaGold_percent = chinaGold.count("Gold") / totalG * 100
print(chinaGold_percent)
usaGold_percent = 100 - chinaGold_percent
print(usaGold_percent)

print("CHN vs USA Silver %")
totalS = chinaSilver.count("Silver") + usaSilver.count("Silver")
chinaSilver_percent = chinaSilver.count("Silver") / totalS * 100
print(chinaSilver_percent)
usaSilver_percent = 100 - chinaSilver_percent
print(usaSilver_percent)

print("CHN vs USA Bronze %")
totalB = chinaBronze.count("Bronze") + usaBronze.count("Bronze")
chinaBronze_percent = chinaBronze.count("Bronze") / totalB * 100
print(chinaBronze_percent)
usaBronze_percent = 100 - chinaBronze_percent
print(usaBronze_percent)


np_medal = 3
before = (bronzebefore, silverbefore, goldbefore)
after = (bronzeafter, silverafter, goldafter)
fig, ax = plt.subplots()
index = np.arange(np_medal)
bar_width = 0.35
opacity = 0.4
error_config = {"ecolor": "0.3"}
rects1 = ax.bar(index, before, bar_width,
                alpha=opacity, color="slategray",
                error_kw=error_config,
                label="Before")

rects2 = ax.bar(index + bar_width, after, bar_width,
                alpha=opacity, color="maroon", 
                error_kw=error_config,
                label="After")

ax.set_xlabel("Medals")
ax.set_ylabel("# of Medals")
ax.set_title("China Medals Before and After 2000")
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(("Bronze", "Silver", "Gold"))
ax.legend()

fig.tight_layout()
plt.show()


labels = "Men", "Women"
sizes = [men_percent, women_percent]
colors = ["skyblue", "violet"]

plt.pie(sizes, colors=colors, autopct='%1.1f%%', shadow=False, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("USA Men vs Women in Olympics Hockey")
plt.xlabel("Total Men: 167 Total Women: 102")
plt.show()


labels = "China", "USA"
sizes = [chinaGold_percent, usaGold_percent]
colors = ["red", "blue"]

plt.pie(sizes, colors=colors, autopct='%1.1f%%', shadow=False, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("China vs USA Gold Medals")
plt.xlabel("Total China: 315 Total USA: 167")
plt.show()


labels = "China", "USA"
sizes = [chinaSilver_percent, usaSilver_percent]
colors = ["red", "blue"]

plt.pie(sizes, colors=colors, autopct='%1.1f%%', shadow=False, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("China vs USA Silver Medals")
plt.xlabel("Total China: 203 Total USA: 319")
plt.show()


labels = "China", "USA"
sizes = [chinaBronze_percent, usaBronze_percent]
colors = ["red", "blue"]

plt.pie(sizes, colors=colors, autopct='%1.1f%%', shadow=False, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("China vs USA Bronze Medals")
plt.xlabel("Total China: 107 Total USA: 167")
plt.show()
