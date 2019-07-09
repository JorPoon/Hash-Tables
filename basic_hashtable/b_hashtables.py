

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.storage = [None] * capacity
        


# '''
# Fill this in.
# Research and implement the djb2 hash function
#def hash(string, max):
# '''
def hash(string, max):

    hashed = 5381
    for i in range(len(string)):
        hashed = ((hashed << 5) + hashed) + ord(string[i])
    
    return hashed % max

# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    hash_table.count += 1
    # index = hashed % hash_table.capacity
    index = hash(key, hash_table.capacity)
    # print(hashed)
    # print(index)
    new_Pair = Pair(key, value)
    # print(new_Pair.key, new_Pair.value)
    node = hash_table.storage[index]

    if node:
        last_node = None
        while node:
            if node.key == key:
                node.value = value
                print('You replaced the value!')
                return
            last_node = node
            node = node.next
        last_node.next = new_Pair
    else:
        hash_table.storage[index] = new_Pair
    # print(index)
    # print(index % hash_table.capacity)
    # node = hash_table.table[index]
    # if node == None:
    #     hash_table.table[index] = Pair(key, value)
    #     print(hash_table.table[index])
    #     return
    # prev = node
    # while node is not None:
    #     prev = node
    #     node = node.next
    # prev.next = Pair(key, value)
    



# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    hash_table.count -= 1
    index = hash(key, hash_table.capacity)

    node = hash_table.storage[index]
    if node:
        last_node = None
        while node:
            if node.key == key:
                if last_node:
                    last_node.next = node.next
                else:
                    hash_table.storage[index] = node.next
            last_node = node
            node = node.next
    else:
        print("There's nothing there!")
    


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)

    node = hash_table.storage[index]
    if node:
        last_node = None
        while node:
            if node.key == key:
                return node.value
            node = node.next
    return None


def Testing():
    ht = BasicHashTable(16)
    print(ht.storage)

    hash_table_insert(ht, "line", "Here today...\n")
    print(ht.storage[13].value)

    hash_table_remove(ht, "line")
    print(ht.storage[13])



    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
