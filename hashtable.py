#DictHash Klass
class DictHash:
    def __init__(self): #init metod för DictHash
        self._dict = {}

    def store(self, key, data): #store metod
        self._dict[key] = data

    def search(self, key):#search metod
        return self._dict[key]

    def __getitem__(self, key):#getitem retunerar search
        return self.search(key)

    def __contains__(self, item): #contains
        return item in self._dict.values()

#HashNode Klass
class HashNode:
    def __init__(self, key=" ", data=None): #Init metod med 3 attribute nyckel, data och en pekare för krocklista
        self.key = key
        self.data = data
        self.next = None

#Hashtable klass
class Hashtable:

    def __init__(self, size):# Init metod för Hashtable
        self._table = [None] * 2 * size #dubbla storleken på listan för att minska risken för krock

    def store(self, key, data):#Store metod
        if self._table[self.hashfunction(key)] is None: #lägger in om ingen krock
            self._table[self.hashfunction(key)] = HashNode(key, data)
        else:
            help_store(self._table[self.hashfunction(key)], HashNode(key, data))#kallar hjälpfunktion om det blir krock

    def search(self, key):#Search metod
        if self._table[self.hashfunction(key)] is None: #Om nyckeln inte finns
            raise KeyError

        elif self._table[self.hashfunction(key)].key == key:#Om nyckel finns på första position
            return self._table[self.hashfunction(key)].data
        else:
            return help_search(self._table[self.hashfunction(key)], key) #kallar hjälp funktion,hitta i krocklista

    def hashfunction(self, key):#Hash metod
        hash_value = 0
        for i, ele in enumerate(key):
            hash_value += 8 ** i * ord(ele) #tar 8^i*ord(bokstav)
        hash_value *= hash_value #kvadrerar värdet
        return hash_value % len(self._table)#retunerar mod av längden av listan så indexet blir rätt


def help_store(current_node, insert_node): #rekursivt lägger värdet på rättplats
    if current_node.key == insert_node.key and insert_node.data is not None:
        current_node.data = insert_node.data

    elif current_node.next is None:
        current_node.next = insert_node
    else:
        help_store(current_node.next, insert_node)


def help_search(current_node, key):#rekursivt söker igenom krocklistan
    if current_node.next is None:#Om hela krocklistan söks igenom finns inte nyckeln
        raise KeyError
    elif current_node.next.key == key: #nyckeln hittades
        return current_node.next.data
    else:
        return help_search(current_node.next, key)



# %%


# %%
