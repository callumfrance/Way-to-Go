from GeoUtils import GeoUtils
import data

distance = list()
ascent = list()
descent = list()

y = data.theStroll_location_updates.split("\n")
prez = list()

cumulative_dist = 0.0
cumulative_asc = 0.0
cumulative_desc = 0.0

def vertical(a, b):
    if a > b:
        descent.append(a-b)
    else:
        ascent.append(b-a)


for x in y:
    z = x.split(",")
    z[0] = float(z[0])
    z[1] = float(z[1])
    z[2] = float(z[2])
    if len(prez) is not 0:
        distance.append(GeoUtils.calcMetresDistance(z[0], z[1], prez[0], prez[1]))
        vertical(prez[2], z[2])
        del prez[:]
    prez.append(z[0])
    prez.append(z[1])
    prez.append(z[2])

print(str(distance)) # correct
print(str(ascent))
print(str(descent))

for i in distance:
    cumulative_dist += i
for i in ascent:
    cumulative_asc += i
for i in descent:
    cumulative_desc += i

print("\n" + str(cumulative_dist)) # correct
print(str(cumulative_asc))
print(str(cumulative_desc))

"""
[173.0691572791559, 381.60992832227765, 650.7826657823673, 1408.3951963185798, 297.4337884860034, 204.60858378587457, 721.9119892441123, 293.1319610674382]
[0.0, 0.6000000000000014, 1.4299999999999997, 1.7899999999999991, 0.28000000000000114]
[0.7999999999999972, 0.5, 0.5]

4130.943270285809
4.100000000000001
1.7999999999999972
"""

print(str(cumulative_dist - 173.1)) # gives 3957.8
# program outputs this on first iter 3874.2

#3746.61 on second iter
