# Set takes only unique value
# Set automatically sorting value
s = set([1, 4, 9, 3, 4])
print(type(s))
print(s)
s.add(5)
s.add(9)  # It will not insert 9 because 9 is already there in set
s.remove(4)
print(s)
