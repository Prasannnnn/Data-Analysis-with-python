a = ["un pera solla","uyire uyire","kadhaliya kadhaliye","Summer times sadness","Born to die"]
#+ve=     0                 1               2                   3                   4         #left to right is an positive
#-ve=     -5                -4              -3                  -2                  -1        #right to left is an negative
print(a)
#its is an ordered
print("the length of a is ",len(a))
#type
print("the type of data a is",type(a))
#positive index
print("positive index",a[4])
#negative index
print("negative index",a[-4])
#slicing
#left side starting 1 
#right side ending before position 1
print(a[1:5])
#negative slicing
print(a[-4:-1])
