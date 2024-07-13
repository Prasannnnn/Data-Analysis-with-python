''' Get the key of a minimum value from the following dictionary 
Given: 
sample_dict = { 
'Physics': 82, 
'Math': 65, 
'history': 75 
} 
Expected output: 
Math '''
sample_dict = { 
'Physics': 82, 
'Math': 65, 
'history': 75 
} 
min_key = min(sample_dict,key=sample_dict.get)
print(min_key)