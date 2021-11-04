from math import sqrt


class Jeden:
    def __init__(self, number):
        self.number = number

    def policz(self):
        c = sqrt(self.number)
        return c


class Dwa:
    def __init__(self, number):
        self.number = number

    def policz(self):
        c = sqrt(self.number)
        return c


def policz_sumę(obj1, obj2):
    c = [obj1.policz(), obj2.policz()]
    return sum(c)


ab = Jeden(12)
bc = Dwa(16)
ac = Jeden(17)
ad = Jeden(29)
bb = Dwa(99)

lista = [ab, bc, ac, ad, bb]
i = 1
for a in lista[:-1]:
    # if i == len(lista):
    #     break
    b = lista[i]
    print(policz_sumę(a, b))
    i += 1
