print("Hello World")
counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == "Denver":
    print(counties[1])
counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Pasi is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")


counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict.keys():
    print(counties_dict[county])

for county, voters in counties_dict.items():
    print(county, voters)
