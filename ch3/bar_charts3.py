from collections import Counter
from matplotlib import pyplot as plt


mentions = [500, 505]
years = [2017, 2018]

plt.bar(years, mentions, 0.8)
plt.xticks(years)
plt.ylabel("# of times I heard someone say 'data science'")#

## if you don't do this, matplotlib will label the x-axis 0, 1
## and then add a +2.013e3 off in the corner (bad matplotlib!)
plt.ticklabel_format(useOffset=False) #nothing really changed here

## misleading y-axis only shows the part above 500
## first 2 is about x axis and second two about y axis
plt.axis([2016.5, 2018.5, 499, 506])
#plt.title("Look at the 'Huge' Increase!")
# restiring to normal azis
plt.axis([2016.5, 2018.5, 0, 550])
#

#plt.savefig('im/viz_misleading_y_axis.png')
#plt.gca().clear()#
#

fig1 = plt.gcf()
plt.show()

fig1.savefig('ch3/bar_charts3.png')
#plt.gca().clear()
