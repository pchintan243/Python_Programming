car = ["Bugatti", "Chiron", "Veyron", "Ferrari", "Mercedes", "Lamborghini"]
print(car)
sort = [34, 67, 23, 34, 12, 78]
#lists mutable hoy means change kari sakay value
#sort.sort()       #ascending order
#sort.reverse()    #descending order
print(sort)
print(sort[1:4])
print(sort[:5])
print(sort[0:])
print(sort[::1])
print(sort[::2])
sort.append(45)    #last ma value insert karse
sort.insert(3, 80) #particular position ma insert karva mate.. first index lakhvani pachi number
print(sort)


#tupple immutable hoy means change thay nahi
#tupple
tupple = (1, 6, 9, 3, 5)
print(tupple)

a = 9
b = 1
a, b = b, a
print(a,b)