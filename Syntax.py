from sys import stdin
from linkedQFile import LinkedQ
from hashtable import Hashtable
from Stack import Stack
from molgrafik import *


class SyntaxError(Exception):  # Syntaxfel
    pass


class Ruta: #ruta klass
    def __init__(self, atom="()", num=1):
        self.atom = atom
        self.num = num
        self.next = None
        self.down = None


class Atom: #atom klass
    def __init__(self, namn, vikt):
        self.namn = namn
        self.vikt = vikt

    def __str__(self):
        return "{" + self.namn + " " + str(self.vikt) + "}"

    def getnamn(self):
        return self.namn

    def getvikt(self):
        return self.vikt


def read_formel(q):  # läs formel
    mol = read_molecule(q)
    mg = Molgrafik()
    mg.show(mol)
    weight(mol)


def read_molecule(q):  # molekyl funktion
    if q.peek == ")":
        return read_group(q)
    else:
        mol = read_group(q)
    if not q.isEmpty() and mol is not None:  # Så länga kön inte är tom och mol finns kallas molekyl funktion
        mol.next = read_molecule(q)
    elif not mol_stack.isEmpty() and mol is not None:  # Om hela molekylen är klar och det fortfarande finns paranteser kvar
        raise SyntaxError("Saknad högerparentes vid radslutet ")
    return mol


def read_group(q):  # group funktion
    rutan = Ruta()
    if q.peek().isalpha():  # Om atom
        rutan.atom = read_atom(q)
        if q.peek().isnumeric():
            rutan.num = read_num(q)
        return rutan

    if q.peek() == "(":  # Om vänster parantes
        q.dequeue()
        mol_stack.push(rutan)  # lägger in rutan objektet i stacken
        rutan.down = read_molecule(q)
        return rutan

    if q.peek() == ")" and (not mol_stack.isEmpty()):  # Om höger parantes
        tmp = mol_stack.pop()
        q.dequeue()
        if q.peek().isnumeric():
            tmp.num = read_num(q)  # lägger in num på rutan som var i stacken
            return None
        else:
            raise SyntaxError("Saknad siffra vid radslutet ")

    raise SyntaxError("Felaktig gruppstart vid radslutet ")  # Om inget uppnås är det fel


def read_atom(q):  # atom funktion
    atom = read_LETTER(q)
    if 97 <= ord(q.peek()) <= 122:  # tittar om nästa bokstav är liten
        atom += read_letter(q)
    try:
        if atomtable.search(atom) is not None:
            return atom
    except KeyError:
        raise SyntaxError("Okänd atom vid radslutet ")


def read_num(q):  # nummer funktion
    num_str = q.dequeue()
    if int(num_str) == 0 or (
            int(num_str) < 2 and not q.peek().isnumeric()):  # Om talet börjar med en 0 eller om talet är 1
        raise SyntaxError("För litet tal vid radslutet ")
    while q.peek().isnumeric():
        num_str += q.dequeue()
    return int(num_str)


def read_letter(q):  # funktion liten bokstav
    char = q.dequeue()

    if 97 <= ord(char) <= 122:  # a-z
        return char


def read_LETTER(q):  # funktion stor bokstav
    char = q.dequeue()
    if 65 <= ord(char) <= 90:  # A-Z
        return char
    raise SyntaxError("Saknad stor bokstav vid radslutet " + char)


def store_molecule(molecule):  # skapar linkedQ samt lägger in varje character i molekylen i kön
    q = LinkedQ()
    for char in molecule:
        q.enqueue(char)
    return q


def test_molecule(molecule):  # funktion för att testa om molekylen är riktig
    q = store_molecule(molecule)
    global mol_stack  # global stack som håller reda på variabler
    mol_stack = Stack()
    try:
        read_formel(q)
        return "Formeln är syntaktiskt korrekt"
    except SyntaxError as error:
        return str(error) + str(q)
    while not mol_stack.isEmpty():  # rensar stack efter varje molekyl
        mol_stack.pop()


def atom_list():  # tagen från hashtest
    """Skapar och returnerar en lista med Atom-objekt"""
    atomdata = "H  1.00794;\
    He 4.002602;\
    Li 6.941;\
    Be 9.012182;\
    B  10.811;\
    C  12.0107;\
    N  14.0067;\
    O  15.9994;\
    F  18.9984032;\
    Ne 20.1797;\
    Na 22.98976928;\
    Mg 24.3050;\
    Al 26.9815386;\
    Si 28.0855;\
    P  30.973762;\
    S  32.065;\
    Cl 35.453;\
    K  39.0983;\
    Ar 39.948;\
    Ca 40.078;\
    Sc 44.955912;\
    Ti 47.867;\
    V  50.9415;\
    Cr 51.9961;\
    Mn 54.938045;\
    Fe 55.845;\
    Ni 58.6934;\
    Co 58.933195;\
    Cu 63.546;\
    Zn 65.38;\
    Ga 69.723;\
    Ge 72.64;\
    As 74.92160;\
    Se 78.96;\
    Br 79.904;\
    Kr 83.798;\
    Rb 85.4678;\
    Sr 87.62;\
    Y  88.90585;\
    Zr 91.224;\
    Nb 92.90638;\
    Mo 95.96;\
    Tc 98;\
    Ru 101.07;\
    Rh 102.90550;\
    Pd 106.42;\
    Ag 107.8682;\
    Cd 112.411;\
    In 114.818;\
    Sn 118.710;\
    Sb 121.760;\
    I  126.90447;\
    Te 127.60;\
    Xe 131.293;\
    Cs 132.9054519;\
    Ba 137.327;\
    La 138.90547;\
    Ce 140.116;\
    Pr 140.90765;\
    Nd 144.242;\
    Pm 145;\
    Sm 150.36;\
    Eu 151.964;\
    Gd 157.25;\
    Tb 158.92535;\
    Dy 162.500;\
    Ho 164.93032;\
    Er 167.259;\
    Tm 168.93421;\
    Yb 173.054;\
    Lu 174.9668;\
    Hf 178.49;\
    Ta 180.94788;\
    W  183.84;\
    Re 186.207;\
    Os 190.23;\
    Ir 192.217;\
    Pt 195.084;\
    Au 196.966569;\
    Hg 200.59;\
    Tl 204.3833;\
    Pb 207.2;\
    Bi 208.98040;\
    Po 209;\
    At 210;\
    Rn 222;\
    Fr 223;\
    Ra 226;\
    Ac 227;\
    Pa 231.03588;\
    Th 232.03806;\
    Np 237;\
    U  238.02891;\
    Am 243;\
    Pu 244;\
    Cm 247;\
    Bk 247;\
    Cf 251;\
    Es 252;\
    Fm 257;\
    Md 258;\
    No 259;\
    Lr 262;\
    Rf 265;\
    Db 268;\
    Hs 270;\
    Sg 271;\
    Bh 272;\
    Mt 276;\
    Rg 280;\
    Ds 281;\
    Cn 285"
    atomlista = []
    lista = atomdata.split(";")
    for namn_vikt in lista:
        namn, vikt = namn_vikt.split()
        atom = Atom(namn, float(vikt))
        atomlista.append(atom)
    return atomlista


def create_hashtable(atomlista):  # tagen från hashtest
    """Lagrar atomlistans element i en hashtabell"""
    antalElement = len(atomlista)
    hashtabell = Hashtable(antalElement)
    for atom in atomlista:
        hashtabell.store(atom.namn, atom.vikt)
    return hashtabell


atomtable = create_hashtable(atom_list())


def weight(mol):  # printar vikten
    mol_weight = help_weight(mol)
    print("Vikt: " + str(mol_weight))


def help_weight(mol):  # hjälp funktion till weight
    if mol.atom == "()":
        atom_weight = help_weight(mol.down) * mol.num
    else:
        atom_weight = float(atomtable.search(mol.atom)) * mol.num
    if mol.next is not None:
        atom_weight += help_weight(mol.next)

    return atom_weight


def main():  # main
    for line in stdin:
        line = line.strip()
        molecule = line
        if molecule == "#":
            break
        print(test_molecule(molecule))


print(test_molecule("Si(C3(COOH)2)4(H2O)7"))


