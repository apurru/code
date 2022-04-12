symbols = ['s', 'e', 'l', ' ', 'h', 'a']

S = symbols
Destination = "he sees a see"

word1 = (list((h for h in S if h.__contains__("h")))+list((e for e in S if e.__contains__("e"))))
he = ''.join(list(word1))

word2 = (list((s for s in S if s.__contains__("s")))+list((e for e in S if e.__contains__("e")))+list(filter(lambda e: 'e' in e, S))+list(filter(lambda s: 's' in s, S)))
sees = ''.join(list(word2))

word3 = list(filter(lambda a: 'a' in a, S))
a = ''.join(list(word3))

word4 = (list(word2))
see = (''.join(word4))[:-1]

space = " "
print( he + space + sees + space + a + space + see)
