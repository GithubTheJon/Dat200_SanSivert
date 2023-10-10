class MyHashTable:
    def __init__(self):
        # 1. Create a list of size `list_size` with all values None
        self.max_size = 4096
        self.arr = [None for i in range(self.max_size)]
        self.keys = list()
        self.values = list()

    def get_hash(self, key):
        hash_sum = 0
        for char in key:
            hash_sum += ord(char)
        return hash_sum%self.max_size
        # write simple algorithm for hashing, which can convert strings into numeric list indices.
        # Iterate over the string, character by character Convert each character to a number using Python's built-in ord function.
        # Add the numbers for each character to obtain the hash for the entire string
        # Take the remainder of the result with the size of the data list
        # Variable to store the result (updated after each iteration)


    def get_index(self, key):
        # Take the remainder of the result with the size of the data list and return the index of the list
        pass

    def insert(self, key, value):
        # 1. Find the index for the key using get_index
        for i, existing_key in enumerate(self.keys):
            if existing_key == key:
                self.values[i] = value
                return
        # 2. Store the key-value pair at the right index
        self.keys.append(key)
        self.values.append(value)


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
    
    def __repr__(self) -> str:
        return f"{self.keys}"


def read_file(file):
    mydict = list()
    with open(file, 'r') as f:
        for line in f:
            try:
                tokens = line.split(',')
                phone = str(tokens[0])          # Skips the first information line and other irrelevancies
                name = str(tokens[1])           # --||--
                lastlocation = tokens[2]
                lastseen = tokens[3]
                state = tokens[4].strip("\n")   # gets rid of "\n" char
                mylist.append(f"{phone}, {name}, {lastlocation}, {lastseen}, {state}")
                # print(f"PhoneNr: {phone}, {name}, {lastlocation}, {lastseen}, {state}", end="")
            except ValueError:
                pass
    return mylist

if __name__ == "__main__":
    # read_file("Phonebook.csv")
    myHT = MyHashTable()
    mylist = read_file("Phonebook.csv")
    index = 0
    print(mylist[:2])
    for value in mylist:
        myHT.insert(index, value)
        index += 1
    
    # print(myHT)
    