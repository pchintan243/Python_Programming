car = ["Bugatti", "Chiron", "Veyron", "Ferrari", "Mercedes", "Lamborghini"]
print(car)
sort = [34, 67, 23, 34, 12, 78]
# List is mutable means it can be change
# sort.sort()       #ascending order
# sort.reverse()    #descending order
print(sort)
print(sort[1:4])
print(sort[:5])
print(sort[0:])
print(sort[::1])
print(sort[::2])
sort.append(45)  # It will insert the value at the end
sort.insert(3,
            80)  # If you insert the number at particular position...first write index then comma and then value which you want to insert
print(sort)

# Tupple is immutable it means value can not be change or modify it.
tupple = (1, 6, 9, 3, 5)
print(tupple)
a = 9
b = 1
a, b = b, a  # For swapping two variable
print(a, b)
