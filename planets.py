# Exercise to practice with lists
planet_list = ["Mercury", "Mars"]
print("Original list of planets ", planet_list)
planet_list.append("Jupiter")
planet_list.append("Saturn")
print("Additional planets ", planet_list)
planet_list.extend(["Uranus", "Neptune"])
print("Adding two of the last planets ", planet_list)
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
print("Inserting Venus and Earth ", planet_list)
planet_list.append("Pluto")
print("And last but not least, adding pluto ", planet_list)
rocky_planets = planet_list[0:4]
print ("Rocky Planets ", rocky_planets)
del planet_list[8]
print(planet_list)