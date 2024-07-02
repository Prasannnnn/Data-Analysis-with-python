a = ["Pulsar","Rajoot","Royal Enfield","RX 100","MT","Ronin","Apache"]
# a.remove("Ronin")
# a.pop(3)
# #del a
# print(a)
# b = ["1","Raj","Royal ","RX ","MT","Roni","Apa"]
# b.remove("Raj")
# print(b)
b = ["1","Raj","Royal ","RX ","MT","Roni","Apa"]
a.extend(b)
print(a)
print(len(a))
a.remove("Raj")
a.pop(5)
print(a)