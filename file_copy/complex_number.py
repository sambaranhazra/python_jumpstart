class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __repr__(self):
        operator = '+' if self.imaginary >= 0 else '-'
        return f"{self.real} {operator} {abs(self.imaginary)}i"

    def __add__(self, other):
        if not isinstance(other, Complex):
            raise TypeError("Complex number can be added")
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        if not isinstance(other, Complex):
            raise TypeError("Complex number can be added")
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def __neg__(self):
        return Complex(-self.real, -self.imaginary)


def main():
    c = Complex(2, 3)
    d = Complex(3, -2)
    print(c)
    print(d)
    print(c + d)
    print(-c - (-d))


if __name__ == '__main__':
    main()
