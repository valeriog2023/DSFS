from matplotlib import pyplot as plt

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

plt.bar(range(len(movies)), num_oscars)

plt.title("My fabourite movies")
plt.ylabel("# of Academy Awards")

# label x-axis with movie names at bar centers
plt.xticks(range(len(movies)), movies)

fig1 = plt.gcf()
plt.show()
fig1.savefig("ch3/bar_chart.png")
