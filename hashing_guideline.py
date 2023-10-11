# A guideline to how it should work with some testing code (not completed and should not be)

class MyHashTable:
    def __init__(self):
        # 1. Create a list of size `list_size` with all values None
        self.max_size = 4096
        self.arr = [None for i in range(self.max_size)]

    def get_hash(self, key):    # finished
        return hash(key)%self.max_size
        '''
        hash_sum = 0
        for char in key:
            hash_sum += ord(char)
        return hash_sum%self.max_size
        '''
        # write simple algorithm for hashing, which can convert strings into numeric list indices.
        # Iterate over the string, character by character Convert each character to a number using Python's built-in ord function.
        # Add the numbers for each character to obtain the hash for the entire string
        # Take the remainder of the result with the size of the data list
        # Variable to store the result (updated after each iteration)


    def get_index(self, key):   # finished
        # Take the remainder of the result with the size of the data list and return the index of the list
        return self.get_hash(key)

    def insert(self, key, value):
        # 1. Find the index for the key using get_index
        # 2. Store the key-value pair at the right index
        
        index = self.get_hash(key)
        if self.arr[index] is None:
            self.arr[index] = []
        for pair in self.arr[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.arr[index].append([key, value])


    def search(self, key):
        # 1. Find the index for the key using get_index
        for i, existing_key in enumerate(self.keys):
            # 2. Retrieve the data stored at the index
            if existing_key == key:
                return self.values[i]
        # 3. Return the value if found, else return None
        return None     # key not found

    def update(self, key, value):
        # 1. Find the index for the key using get_index


        # 2. Store the new key-value pair at the right index
        pass

    def display_all(self):
        # 1. Extract the key from each key-value pair
        pass


if __name__ == "__main__":
    myHT = MyHashTable()
    
    def read_file(file):
        mylist = list()
        with open(file, 'r') as f:
            for line in f:
                try:
                    tokens = line.split(',')
                    phone = int(tokens[0])          # Skips the first information line and other irrelevancies
                    name = str(tokens[1])           # --||--
                    lastlocation = tokens[2]
                    lastseen = tokens[3]
                    state = tokens[4].strip("\n")   # gets rid of "\n" char
                    rest = f"{name}, {lastlocation}, {lastseen}, {state}"
                    myHT.insert(phone, rest)
                    
                    # print(f"PhoneNr: {phone}, {name}, {lastlocation}, {lastseen}, {state}", end="")
                except ValueError:
                    pass
        return mylist
    
    read_file("Phonebook.csv")
    print(myHT.display_all)
    