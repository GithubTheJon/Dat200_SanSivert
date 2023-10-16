# Finnished?

class MyHashTable:
    def __init__(self):
        # 1. Create a list of size `list_size` with all values None
        self.max_size = 4096
        self.table = [None] * self.max_size

    def get_hash(self, key):
        # write simple algorithm for hashing, which can convert strings into numeric list indices.
        # Iterate over the string, character by character Convert each character to a number using Python's built-in ord function.
        # Add the numbers for each character to obtain the hash for the entire string
        # Take the remainder of the result with the size of the data list
        # Variable to store the result (updated after each iteration)
        hash_sum = 0
        for char in key:
            hash_sum += ord(char)
        return hash_sum % self.max_size    # needs to hash to the max_size

    def get_index(self, key):
        # Take the remainder of the result with the size of the data list and return the index of the list
        return self.get_hash(key)

    def insert(self, key, value):
        # 1. Find the index for the key using get_index
        index = self.get_index(key)
        if self.table[index] is None:
            self.table[index] = []
        # 2. Store the key-value pair at the right index
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def search(self, key):
        # 1. Find the index for the key using get_index
        index = self.get_index(key)
        if self.table[index] is None:
            return None
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def remove(self, key):
        index = self.get_hash(key)
        if self.table[index] is None:
            return
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                return
            
    def update(self, key, value):
        # 1. Find the index for the key using get_index
        index = self.get_index(key)
        if self.table[index] is None:
            self.table[index] = []
        # 2. Store the new key-value pair at the right index
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])
            
    def display_all(self):
        keys = []
        for index in range(self.max_size):
            if self.table[index] is not None:
                for pair in self.table[index]:
                    keys.append(pair[0])
        return keys
    
            
if __name__ == "__main__":
    myHT = MyHashTable()
    
    def read_file(file):
        mylist = list()
        l_count = 1
        with open(file, 'r') as f:
            for line in f:
                if l_count == 1:
                    pass
                else:
                    tokens = line.split(',')
                    phone = str(tokens[0])          # key
                    name = str(tokens[1])           # value
                    # lastlocation = tokens[2]
                    # lastseen = tokens[3]
                    # state = tokens[4].strip("\n")   # gets rid of "\n" char
                    # rest = f"{name}, {lastlocation}, {lastseen}, {state}"   # format of the value inserted
                    myHT.insert(phone, name)        # inserts the key with its value to MyHashTable
                l_count += 1
            
        return mylist
    
    read_file("Phonebook.csv")  
    
    print(myHT.display_all())   # displays all the keys
    phone_number_1 = '123456789'
    name_1 = 'UiS'
    myHT.insert(phone_number_1, name_1)

    phone_number_2 = '987654321'
    name_2 = 'NTNU'
    myHT.insert(phone_number_2, name_2)
    
    print(myHT.display_all())
    print(myHT.get_index(phone_number_1))
    print(myHT.get_index(phone_number_2), "\n")
    
    print(myHT.search("3354577686"))  # displays the value (name) from a valid key, else returns None
    print(myHT.get_index("3354577686"))
    
    # print(myHT.display_all())