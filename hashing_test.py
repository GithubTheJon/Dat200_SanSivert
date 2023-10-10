dict = {}

mydict = {
    1: "python", 
    2: "golang", 
    3: "C++",
    4: ["os", "java"]
}

print(mydict, "\n")
for i in mydict:
    print(mydict[i])
    
    

key = 1
if key in mydict:               # se if key is in dict
    print("\n", mydict[key])    # prints the data from key in dict
else:
    print("False")


del mydict[1]   # deletes the key

print(mydict)

# hash the keys to make an index??? 

stock_price = {
    "jan": 123,
    "feb": 234,
    "mar": 345,
    "apr": 456,
    "may": 567
}

print(stock_price["apr"])

# hashing, multiple values for a key using mod (%)

def ord(char):
    return char

def get_hash(key):
    hash = 0
    for char in key:
        hash += ord(char) 
    return hash % 10

get_hash("apr")