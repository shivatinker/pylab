class DecimalFraction:
    def __init__(self, num_str, man=0, ex=0, sign="+"):
        if num_str == "":
            self.man = str(man).replace(".", "")
            add = 0
            for i in str(man):
                if i == ".":
                    break
                add += 1
            self.ex = ex + add
            self.sign = sign
        else:
            self.ex = 1
            tmp = 1
            for i in num_str:
                if i == '0':
                    tmp += 1
                    self.ex -= 1
            if num_str[0] == '-':
                self.sign = "-"
            else:
                self.sign = "+"

                self.man = num_str[tmp:]

    def printstr(self):
        if self.sign == "-":
            print("-0.", end='')
        else:
            print("0.", end='')
        print(self.man, end='')
        print("E", end='')
        if self.ex > 0:
            print("+", end='')
        print(self.ex, end='')

    def __lt__(self, otherFraction):
        if self.sign == "-" and otherFraction.sign == "+":
            return True
        if self.ex < otherFraction.ex:
            return True
        if self.ex == otherFraction.ex and int(self.man) < int(otherFraction.man):
            return True

    def __eq__(self, otherFraction):
        if self.sign == otherFraction.sign and self.ex == otherFraction.ex and self.man == otherFraction.man:
            return True
        return False

    def __le__(self, otherFraction):
        if self.__lt__(otherFraction) or self.__eq__(otherFraction):
            return True
        return False


a = DecimalFraction("", 2.31, -7, "+")
b = DecimalFraction("0.000000231")
c = DecimalFraction("0.00001")

a.printstr()
print()
b.printstr()
print()
c.printstr()
print()

print(a == b)
print(a >= c)
print(a <= c)
