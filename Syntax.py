from linkedQFile import LinkedQ
from sys import stdin


class SyntaxError(Exception): #Syntaxfel
    pass


def read_molecule(q): #molekyl funktion
    read_atom(q)
    if q.peek().isnumeric():
        read_num(q)


def read_atom(q): #atom funktion
    read_LETTER(q)
    if q.peek().isalpha(): #retunerar true om stor bokstav
        read_letter(q)


def read_num(q):#nummer funktion
    num_str = q.dequeue()
    if int(num_str) == 0 or (int(num_str) < 2 and not q.peek().isnumeric()): #Om talet börjar med en 0 eller om talet är 1
        raise SyntaxError("För litet tal vid radslutet ")


def read_letter(q): #funktion liten bokstav
    char = q.dequeue()
    if 97 <= ord(char) <= 122: #a-z
        return
    raise SyntaxError("Saknad liten bokstav vid radslutet " + char)


def read_LETTER(q):#funktion stor bokstav
    char = q.dequeue()
    if 65 <= ord(char) <= 90:#A-Z
        return
    raise SyntaxError("Saknad stor bokstav vid radslutet " + char)


def store_molecule(molecule):#skapar linkedQ samt lägger in varje character i molekylen i kön
    q = LinkedQ()
    for char in molecule:
        q.enqueue(char)
    return q


def test_molecule(molecule): #funktion för att testa om molekylen är riktig
    q = store_molecule(molecule)
    try:
        read_molecule(q)
        return "Formeln är syntaktiskt korrekt"
    except SyntaxError as error:
        return str(error) + str(q)


def main(): #main
    for line in stdin:
        line = line.strip()
        molecule = line
        if molecule == "#":
            break
        print(test_molecule(molecule))

def try_molecule():
    test = input("skriv molekyl")
    print(test_molecule(test))

if __name__ == "__main__":
    main()
# %%
