import random
import string

def datos_entrada():
    n = random.randint(1,20)
    s = ""
    largo_s = random.randint(2,4)
    for a in range(largo_s):
        s = s + random.choice("abcadefaghiaaaa")
    print (n, s)
    return [n, s]

datos = datos_entrada()

def repeatedString(s, n):
    largo_s = len(s)
    string = ""
    while len(string)+largo_s-1 < n:
        string = string + s
    string = string + s[0:n - len(string)]
    return string.count("a")



resultado = repeatedString("a",1000000000000)
print (resultado)