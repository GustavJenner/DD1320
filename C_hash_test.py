import random
import zlib
import matplotlib.pyplot as plt


# Funktion som retunerar lista med alla nycklar (26^3)
def All_keys():
    keys_list = []
    for i in range(0, 26):
        for j in range(0, 26):
            for k in range(0, 26):
                key = create_key(i, j, k)
                keys_list.append(key)
    return keys_list


# funktion som ger nyckel på tre bokstäver där invärdena representerar vilken bokstav
def create_key(first, second, third):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"
        , "U", "V", "W", "X", "Y", "Z"]
    return alphabet[first] + alphabet[second] + alphabet[third]


# Retunerar lista med krockar för olika index
def Collision_test(hash, space):
    collision_list = create_zero_list(space)
    keys_list = All_keys()
    for key in keys_list:
        index = hash(key, space)
        collision_list[index] += 1
    return collision_list


# Retunerar lista med speciferad längd fylld med nollor
def create_zero_list(length):
    zero_list = [0] * length
    zero_list.append(0)
    return zero_list


# Den egna hashfunktionen, inparametrar är nyckeln och modulo gränsen
def own_hash(key, space=4294967295):
    hash_value = 0
    for i, ele in enumerate(key):
        hash_value += 8 ** (i + 1) * ord(ele)  # tar 8^i*ord(bokstav)
    hash_value *= hash_value  # kvadrerar värdet
    return hash_value % space


# Adler32 hashfunktion
def adler32_function(key, space=None):
    s = key.encode("ascii")  # göra om till bit tal
    hash_value = zlib.adler32(s)
    if space is None:
        return hash_value
    return hash_value % space  # Modulo gräns


# retunerar medelvärde "distansen" för en nyckel
def avalanche_key(hash, key):
    ref = hash(key)  # referens hash
    dist = 0
    key_list = list(key)
    # tar absolut beloppet av skillnaden mellan hashvärdena
    for i in range(0, 3):
        y = key_list.copy()
        y[i] = chr(ord(y[i]) + 1)
        dist += abs(ref - hash(y[0] + y[1] + y[2]))
        y[i] = chr(ord(y[i]) - 2)
        dist += abs(ref - hash(y[0] + y[1] + y[2]))
    return dist / 6  # medelvärdet


# retunerar medelvärde distansen för summan av nycklar
def avalanche_effect(hash):
    keys_list = All_keys()
    tot_dist = 0
    for key in keys_list:
        tot_dist += avalanche_key(hash, key)
    return tot_dist / (len(keys_list))  # medelvärde


Index_length = 100
list1 = Collision_test(adler32_function, Index_length)
print(avalanche_effect(own_hash))
plt.stem(list1, label="Adler32")
plt.xlabel("Index")
plt.ylabel("Kollisioner")
plt.legend(loc="upper left")
plt.savefig("figures/collision_adler32_max")
plt.show()


# funktion som retunerar lista med hashvärde for olika slumpade nycklar med ökadlängd
def length_test(hash, end_length):
    length_list = []
    for i in range(0, end_length + 1):
        length_list.append(hash(random_string(i)))  # lägger till hashvärde för slumpad nyckel med längd i
    return length_list


# funktion som genererar slumpmässig nyckel där inparametern är längden på nyckeln
def random_string(len):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"
        , "U", "V", "W", "X", "Y", "Z"]
    string = ""
    for i in range(0, len + 1):
        string += alphabet[random.randrange(0, 26)]
    return string


poop = 100
number = 100000

# y1 = time_complexity(adler32_function,number,end_length)
# y2 = time_complexity(own_hash,number,end_length)
y3 = length_test(adler32_function, 100)
y4 = length_test(own_hash, 100)
# plt.plot(y1)
# plt.plot(y2)
plt.plot(y4, label="Egen hash")
plt.xlabel("Nyckellängd")
plt.ylabel("Hashvärde")
plt.legend(loc="upper left")
plt.savefig("figures/length_plot_own.png")
plt.show()

plt.plot(y3, label="Adler32")
plt.xlabel("Nyckellängd")
plt.ylabel("Hashvärde")
plt.legend(loc="upper left")
plt.savefig("figures/length_plot_adler32.png")
plt.show()


# %%
import random
import zlib
import matplotlib.pyplot as plt
def own_hash(key, space=4294967295):
    hash_value = 0
    for i, ele in enumerate(key):
        hash_value += 8 ** (i + 1) * ord(ele)  # tar 8^i*ord(bokstav)
    hash_value *= hash_value  # kvadrerar värdet
    return hash_value % space
#Logic gate: XOR
def XOR_Gate(A, B):
    C = int(A) ^ int(B)
    return C
#Logic gate: NOT
def NOT_Gate(A):
    return 1-int(A)
#Logic gate: XAND
def XAND_Gate(A, B):
    XOR = XOR_Gate(A,B)
    C = NOT_Gate(XOR)
    return C

#Räknar ut hamminavståndet mellan två tal och retunerar sedan procenten lika bitar
def hamming_distance(num_1, num_2):
    count = 0
    x = format(num_1, "b")
    y = format(num_2, "b")

    if len(x) < len(y):# lägger på 0 talen har olika längder
        x = "0"*(len(y)-len(x)) + x

    elif len(y) < len(x):
        y = "0"*(len(x)-len(y)) + y

    for bit in range(len(x)):
        count += XAND_Gate(x[bit],y[bit])
    return count/len(x)
#tar in binärt tal, retunerar lista med binäratal med ett hammingavstånd på 1 från orginal talet
#Dvs om invärdet är "000" blir ut listan "100","010","001"
def bit_change(num):
    key = list(num)
    change_list = []
    for bit in range(len(key)):
        tmp = key.copy()
        tmp[bit] = str(NOT_Gate(tmp[bit]))
        x = "".join(tmp)
        change_list.append(x)

    return change_list

#Räknar den genomsnittliga lavineffekten för en nyckel
def avalanche(key, hash):
    orig = hash(key)
    change_list = bit_change(ASCII_to_binary(key))
    bit_flip = []
    for num in range(len(change_list)):
        key_b = binary_to_ASCII(change_list[num])
        tmp = hamming_distance(hash(key_b),orig)
        bit_flip.append(tmp)
    return sum(bit_flip)/len(bit_flip)

#tar in binärt tal och retunerar ASCII värdet
def binary_to_ASCII(bin_num):
    tmp3 = ""
    u = int(len(bin_num)/7)
    for i in range(u):

        tmp = bin_num[i*7:(i+1)*7]
        tmp2 = int(tmp,2)
        tmp3 += chr(tmp2)
    return tmp3
#tar in ASCII värde och retunerar binärt tal
def ASCII_to_binary(string):
    bin_str = ""
    for chr in string:
        num = ord(chr)
        bin_str += format(num,"b")

    return str(bin_str)

# Adler32 hashfunktion
def adler32_function(key, space=None):
    s = key.encode("ascii")  # göra om till bit tal
    hash_value = zlib.adler32(s)
    if space is None:
        return hash_value
    return hash_value % space  # Modulo gräns

# funktion som genererar slumpmässig nyckel där inparametern är längden på nyckeln
def random_string(len):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"
        , "U", "V", "W", "X", "Y", "Z"]
    string = ""
    for i in range(0, len + 1):
        string += alphabet[random.randrange(0, 26)]
    return string
def length_test(hash, end_length):
    length_list = []

    for i in range(0, end_length):
        x = 0
        for _ in range(100):
            x += avalanche(random_string(i),hash)
        length_list.append(x/100)  # lägger till hashvärde för slumpad nyckel med längd i
    return length_list
#print(avalanche_effect(own_hash))
#print(avalanche_effect(adler32_function))
def Avalanche_effect(hash):
    g = 0
    for j in range(10000):
        g += avalanche(random_string(5),hash)

    return g/10000


y2 = length_test(own_hash,50)
plt.plot(y2, label="Egen hash")
plt.xlabel("Nyckellängd")
plt.ylabel("Procent oförändrade bitar")
plt.legend()
plt.savefig("figures/lavinelengthown.png")


# %%
# Pie chart, where the slices will be ordered and plotted counter-clockwise:




