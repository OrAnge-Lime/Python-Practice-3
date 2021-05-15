from math import pi


def find_farthest_orbit(list_of_orbits):
    for i in list_of_orbits:
        if i[0] == i[1]:
            list_of_orbits.remove(i)

    l = list(map(lambda x: x[0] * x[1] * pi, list_of_orbits))
    return list_of_orbits[l.index(max(l))]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
