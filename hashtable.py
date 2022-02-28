class DictHash:
    def __init__(self):
        self._dict = {}

    def store(self, key, data):
        self._dict[key] = data

    def search(self, key):
        return self._dict[key]

    def __getitem__(self, key):
        return self.search(key)

    def __contains__(self, item):
        return item in self._dict.values()


class HashNode:
    def __init__(self, key = " ", data = None, next = None):
        self.key = key
        self.data = data
        self.next = next


class Hashtable:


    def __init__(self, size):
        self._table = [None] * 2 * size


    def store(self, key, data):
        if self._table[self.hashfunction(key)] is None:
            self._table[self.hashfunction(key)] = HashNode(key, data)
        else:
            help_store(self._table[self.hashfunction(key)], HashNode(key, data))



    def search(self, key):
        if self._table[self.hashfunction(key)] is None:
            raise KeyError

        elif self._table[self.hashfunction(key)].key == key:
            return self._table[self.hashfunction(key)].data
        else:
            return help_search(self._table[self.hashfunction(key)], key)


    def hashfunction(self, key):
        hash_value = 0
        for i, ele in enumerate(key):
            hash_value += 8 ** i * ord(ele)
        hash_value *= hash_value
        return hash_value % len(self._table)


def help_store(current_node, insert_node):
    if current_node.key == insert_node.key and insert_node.data is not None:
        current_node.data = insert_node.data

    elif current_node.next is None:
        current_node.next = insert_node
    else:
        help_store(current_node.next, insert_node)


def help_search(current_node, key):
    if current_node.next is None:
        raise KeyError
    elif current_node.next.key == key:
        return current_node.next.data
    else:
        return help_search(current_node.next, key)



# %%


# %%
