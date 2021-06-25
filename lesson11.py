class Fraction:

    def __init__(self, tu = 0, mau = 1):
        self.tu_so = tu
        self.mau_so = mau

    def show(self):
        print(f'Phân số: {self.tu_so}/ {self.mau_so}')

ps1 = Fraction(2, 5)
ps1.show()
print(ps1.tu_so)
print(ps1.mau_so)

