# indexing

a ="hello world"
# extract letter o in positive indexing as well as negative indexing
print(a[4])
print(a[-7])


#slicing
s = "welcome to python"
#positive indexing extract python
print(len(s))
print(s[11:17:1])    #by using si,ei,up
print(s[11::1])   #by using si and updation
print(s[11:]) #by using only si
#extract only welcome
print(s[:8:1]) # using only end index and updation
print(s[:8:])  # using only end index
print(s[::]) #all default values
#extract alternate character
print(s[::2])
#negative indexing to extract python
print(s[-6::])
#negative indexing to extract python in reverse like "nohtyp"
print(s[-1:-7:-1])

#using postive as well as negative indexing
#extract python
print(s[0:-10:1])


a =['1','2']
b ='-'
s = (b.join(a))
print(type(s))

print("123abc".isalnum())
print("123".isalnum())

a =[1,2,3]
print(list(a))