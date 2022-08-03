dict = {"Chintan": "Pizza", "Hemang": "Burger", "Sumit": "Burger"}
print(dict)
print(dict["Chintan"])
dict["Kevin"] = "Chinese"   #add in last to dictionary
del dict["Hemang"]          #delete dictonary
print(dict)
print(dict.get("Sumit"))
print(dict.keys())
print(dict.items())

