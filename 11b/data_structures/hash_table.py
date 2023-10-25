class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    self.table[index][i] = (key, value)
                    break
            else:
                self.table[index].append((key, value))
        print(self.table)

    def search(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        raise KeyError(f'Key {key} not found')

    def delete(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    del self.table[index][i]
                    break
            else:
                raise KeyError(f'Key {key} not found')
        else:
            raise KeyError(f'Key {key} not found')


# Create a hash table with size 10
hash_table = HashTable(10)

# Insert some key-value pairs
hash_table.insert('apple', 5)
hash_table.insert('banana', 7)
hash_table.insert('cherry', 10)

# Search for a value
print(hash_table.search('banana'))  # Output: 7

# Delete a key-value pair
hash_table.delete('apple')

# Try to search for a deleted key
try:
    print(hash_table.search('apple'))
except KeyError as e:
    print(e)  # Output: "Key 'apple' not found"
