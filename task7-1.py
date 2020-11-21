class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        matrix = '\n'.join([' '.join([str(num) for num in row]) for row in self.matrix])
        return f"{matrix}\n"

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] += other.matrix[i][j]
        return Matrix.__str__(self)


m1 = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

m2 = Matrix([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

print(m1)
print(m2)

print(m1 + m2, end='')
