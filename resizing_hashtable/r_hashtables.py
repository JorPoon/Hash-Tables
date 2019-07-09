

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.storage = [None] * capacity
        


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hashed = 5381

    for i in range(len(string)):
        hashed = ((hashed << 5) + hashed) + ord(string[i])
    
    return hashed % max


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    hash_table.count += 1

    if hash_table.count >= hash_table.capacity:
        hash_table_resize(hash_table)
    # index = hashed % hash_table.capacity
    index = hash(key, hash_table.capacity)
    # print(hashed)
    # print(index)
    new_Pair = LinkedPair(key, value)
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
        last_node.next = new_Pair
    else:
        hash_table.storage[index] = new_Pair
    


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


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    new_capacity = hash_table.capacity * 2
    new_storage = [None] * new_capacity

    for i in range(hash_table.count):
        # new_storage[i] = hash(hash_table.storage[i], new_capacity)
        print(hash_table.storage[i])
        new_storage[i] = hash_table.storage[i]
    
    hash_table.capacity = new_capacity
    hash_table.storage = new_storage

    return hash_table



def Testing():
    ht = HashTable(2)

    # hash_table_insert(ht, "line_1", "Tiny hash table")
    # hash_table_insert(ht, "line_2", "Filled beyond capacity")
    # hash_table_insert(ht, "line_3", "Linked list saves the day!")
    hash_table_insert(ht, "key-0", "val-0")
    hash_table_insert(ht, "key-1", "val-1")
    # hash_table_insert(ht, "key-2", "val-2")
    # hash_table_insert(ht, "key-3", "val-3")
    # hash_table_insert(ht, "key-4", "val-4")
    # hash_table_insert(ht, "key-5", "val-5")
    # hash_table_insert(ht, "key-6", "val-6")
    # hash_table_insert(ht, "key-7", "val-7")
    # hash_table_insert(ht, "key-8", "val-8")
    # hash_table_insert(ht, "key-9", "val-9")

    print(hash_table_retrieve(ht, "key-0"))
    

    # print(hash_table_retrieve(ht, "line_1"))
    # print(hash_table_retrieve(ht, "line_2"))
    # print(hash_table_retrieve(ht, "line_3"))

    # old_capacity = len(ht.storage)
    # ht = hash_table_resize(ht)
    # new_capacity = len(ht.storage)

    # print("Resized hash table from " + str(old_capacity)
    #       + " to " + str(new_capacity) + ".")


Testing()
