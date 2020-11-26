class Complex:
    real_part: int
    complex_part: int

    def __init__(self, real_part, complex_part):
        self.real_part = real_part
        self.complex_part = complex_part

    def __str__(self):
        if self.complex_part > 0:
            return f"{self.real_part}+{self.complex_part}i"
        else:
            return f"{self.real_part}{self.complex_part}i"

    def __add__(self, other):
        rp = self.real_part + other.real_part
        cp = self.complex_part + other.complex_part
        return Complex(rp, cp)

    def __mul__(self, other):
        rp = self.real_part * other.real_part
        cp = self.complex_part * other.complex_part
        return Complex(rp, cp)


z1 = Complex(-3, 4)
z2 = Complex(4, -3)

print(z1)
print(z2)
print(z1 + z2)
print(z1 * z2)
