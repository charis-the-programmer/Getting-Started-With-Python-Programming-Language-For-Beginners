## Try/Except Structure

str1 = "Hello John"
try:
    str2 = int(str1)
except: 
    str2 = -1
print("First ", str2)
str1 = "123"
try:
    str2 = int(str1)
except: 
    str2 = -1
print("Second ", str2)
