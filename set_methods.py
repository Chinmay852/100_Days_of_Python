# s1 = {1,2,5,6}
# s2 = {3,6,7}
# print(s1.union(s2))
# s1.update(s2)
# s2.update(s1)
# print(s1,s2)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# intersection() only those values will pick those are common i.e. Tokyo Madrid
cities3 = cities.intersection(cities2)
print(cities3)
# symmetric_difference() only those values will show except of the common values i.e {'Delhi', 'Kabul', 'Seoul', 'Berlin'}
cities4 = cities.symmetric_difference(cities2) 
print(cities4)

cities = {"Tokyo1", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid2"}
# isdisjoint() Will Show True when No COMMON Matches in Sets
print(cities.isdisjoint(cities2))

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
# This output will Show False because no common value in first set
print(cities.issuperset(cities2))
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Berlin"}
# This output will Show True because common value is there in first set thus First Set is Superset of Second Set
print(cities.issuperset(cities2))
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Berlin"}
# This output will Show True because common value is there in second set thus Second Set is subset of First Set
print(cities2.issubset(cities))

# add("Mumbai") add value
# update(["Mumbai", "Kolkata"]) add one or more set
# remove() to remove specific value it will raise error
# discard() to remove specific value it will not raise error
# pop() last value will pop a random value and we dont know which value will get pop because sets are unordered
# del() delete entire set
# clear() delete the values within the set it will NOT delete the set