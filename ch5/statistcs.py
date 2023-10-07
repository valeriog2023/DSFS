from matplotlib import pyplot as plt
from collections import Counter
# every entry is the number of friends a person has
# there are 204 values
# max value is 100 (present 1 time)
# min value is 1 (present 22 times)
num_friends = [100,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

friends_counts = Counter(num_friends)
max_friends = max(num_friends)
print(f"Max number of friends is {max_friends}")
xs = range(int(max_friends)+1)
ys = [friends_counts[i] for i in xs]
print("Counter used to count nunmber of friends:")
print(friends_counts)
plt.bar(xs,ys)
plt.xlabel("Number of friends")
plt.ylabel("Number of people")
plt.title("Histogram of friends count")
plt.axis([0,101,0,25])
plt.show()

#min/max value value 
# you can eiher use functions of sort the list and get first and last value
min_value = min(num_friends)
max_value = max(num_friends)
sorted_num_friends = sorted(num_friends)
assert min_value == sorted_num_friends[0]
assert max_value == sorted_num_friends[-1]