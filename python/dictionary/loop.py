a={
    "name" : "Prasanna",
    "age" : 22,
    "College" : "Sathyabama",
    "State":"Pondicherry"
}
for x in a:
    print("the for loop",x)

for y in a:
    print(a[y])

for z in a.values():
  print("getting the values ",z)

for i in a.keys():
  print("Getting the Keys",i)

for j, k in a.items():
  print("Getting the items",j,":",k)