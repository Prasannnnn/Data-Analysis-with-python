# a = ("Apple","Orange","Mango","Kiwi")
# b = list(a)
# print(type(b))

a = ("Apple","Orange","Mango","PineApple","Apple","GreenApple")
print(a)
b = list(a)
b[4]="Kiw"
b[1:4] = "Dragon Fruit","Nava","Avacoda"
b.insert(0,"Lemon")
b.append("Orange")
c = ("Guvav","Mongo")
b.extend(c)

a = tuple(b)

for x in a:
    print(x)

y = 0
while y < range(len(b)):
    print(b[y])
    y += 1

print(a)

