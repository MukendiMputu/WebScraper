# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']
kinder_garden = dict.fromkeys(groups, None)
# your code here
group_counts = []
# for i in range(int(input())):
#    group_counts.append(int(input()))
#    kinder_garden[groups[i]] = group_counts[i]

print(kinder_garden.items())
