from linkedQFile import LinkedQ

class SyntaxError(Exception):
    pass

def read_molekyl(q):
    read_atom(q)
    if q.peek().isnumeric():
        read_num(q)

def read_atom(q):
    read_LETTER(q)
    if q.peek().isalpha():
        read_letter(q)

def read_num(q):
    num_str = q.dequeue()
    if int(num_str) == 0 or (int(num_str) < 2 and not q.peek().isnumeric()):
        raise SyntaxError("För litet tal vid radslutet ")

def read_letter(q):
    char = q.dequeue()
    if 97 <= ord(char) <= 122:
        return
    raise SyntaxError("Saknad liten bokstav vid radslutet ")

def read_LETTER(q):
    char = q.dequeue()
    if 65 <= ord(char) <= 90:
        return
    raise SyntaxError("Saknad stor bokstav vid radslutet ")

def store_molekyl(molekyl):
    q = LinkedQ()
    for char in molekyl:
        q.enqueue(char)
    return q

def test_molekyl(molekyl):
    q = store_molekyl(molekyl)
    try:
        read_molekyl(q)
        return "Syntax correct"
    except SyntaxError as error:
        return str(error) + str(q)


print(test_molekyl("HH12"))
