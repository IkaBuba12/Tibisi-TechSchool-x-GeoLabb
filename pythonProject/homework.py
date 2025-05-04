from operator import truediv

var1 = 51
var2 = 51.5
var3 = "both"
var4 = ["elem1", "elem5", "elem9"]
var5 = (10, True, 20, "red")
var6 = {"grass": "green"}

######### ამის ქვემოთ არაფერი შეცვალოთ ########

print(type(var1) == int)
print(type(var2) == float)
print(var1 > 50)
print(var1 <= var2)

print(type(var3) == str)
print(var3[2:4] == "th")

print(type(var4) == list)
print(var4[2] == 'elem9')
print(var4[1:3] == ['elem5', 'elem9'])

print(type(var5) == tuple)
print(var5[3] == "red")

print(type(var6) == dict)
print(var6["grass"] == "green")