# Dictonary has a pairs of key and value.
dict = {"Chintan": "Pizza", "Hemang": "Burger", "Sumit": "Burger"}
print(dict)
print(dict["Chintan"])
dict["Kevin"] = "Chinese"  # Add in last to dictionary
del dict["Hemang"]  # Delete dictionary
print(dict)
print(dict.get("Sumit"))  # It will gives a value of Key
print(dict.keys())  # It prints all keys from dictionary
print(dict.items())
