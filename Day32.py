# Set Methods

# s1 = {1, 2, 3, 4, 5}
# s2 = {4, 5, 6, 7, 8}
# print(s1.union(s2))
# s1.update(s2)
# print(s1)
# print(s1.intersection(s2))
# print(s1.difference(s2))

# cities1={"tokyo","new york","berlin"}
# cities2={"berlin","london","tokyo"}
# cities2.intersection_update(cities1)
# print(cities2)

# AUB - AnB
# cities1={"tokyo","madrid","delhi","berlin"}
# cities2={"tokyo","Seoul","Kabul","madrid"}
# cities3 = cities1.symmetric_difference(cities2)
# print(cities3)

# difference A-B
# cities1={"tokyo","madrid","delhi","berlin"}
# cities2={"Seoul","Kabul","delhi"}
# cities3 = cities1.difference(cities2)
# print(cities3)

#isdisjoint
#Matches a set to another entirely different set which donot have any similarity
# city1={"tokyo1","madrid1","delhi","berlin"}
# city2={"Seoul","Kabul","tokyo","madrid"}
# print(city1.isdisjoint(city2))

#Superset
#checks weather elements of second set are present in the first set
city1={"tokyo","madrid","delhi","berlin"}
city2={"Seoul","Kabul","tokyo","madrid"}
print(city2.issuperset(city1))
city3={"tokyo","madrid","delhi"}
print(city1.issuperset(city3))