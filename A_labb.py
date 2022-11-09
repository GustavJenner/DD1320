import timeit
import sys

def expr(string, weightDict):#funktion som går igenom strängen och räknar djupet samt kallar vikt funktion
    string += "*"#slut markering
    index = 0
    while index in range(len(string)-1):
        flag = False #håller koll om loopen är på siffra
        num_string = ""
        if string[index] == "[":
            weightDict["depth"] += 1
        if string[index] == "]":
            weightDict["depth"] -= 1
        while string[index].isnumeric(): #loop för nummer
            flag = True
            num_string += string[index]
            index += 1 #för varje siffra ökas index med +1 (alltså för nummer)
        if not flag: #Om inte en siffra så öker indexet med +1
            index += 1
        if num_string != "":
            weight(num_string,weightDict)


def weight(num_string, weightDict): #lägger in vikten på rätt plats i dictionariet
    key = int(num_string) * 2 ** weightDict["depth"] # nyckel = vikt*2^D
    weightDict["tot_num"] += 1
    weightDict.setdefault(key, 0)
    weightDict[key] += 1
    if weightDict[key] >= weightDict["max_freq"]: #håller reda på högsta frekvensen
        weightDict["max_freq"] = weightDict[key]


def reset_dict(): #funktionen skapar och retunerar ett nytt dictonary med startvärden
    weightDict = {"max_freq": 0,#max frekvens
                  "depth": -1,#djup
                  "tot_num": 0#totalt antal vikter
                  }
    return weightDict

def solve(string): #tar in jämvikts strängen och retunerar svaret
    weightDict = reset_dict() # återställer dictionariet
    expr(string, weightDict)
    return weightDict["tot_num"] - weightDict["max_freq"]

def main():# main
    n_tests = int(next(sys.stdin))
    for _ in range(n_tests):
        string = next(sys.stdin)
        print(solve(string))

def time():
    line_list = []
    with open("Time_A", "r", encoding="utf-8") as file: #öppnar filen Time_A
        for line in file:
            line_list.append(line)
    return line_list
listop = time()
def testA():
    for line in listop:
        solve(line)

print(timeit.timeit(stmt = lambda: testA(), number = 100000))







#%%
