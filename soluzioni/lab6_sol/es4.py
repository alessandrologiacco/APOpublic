class Matrix:
    
    def __init__(self, other = None):
        self._mat = other

    def row(self):
        return len(self._mat)

    def col(self):
        return len(self._mat[0])

    def _create_mat(row, col):
        return [[0]*col for i in range(row)]
    
    def __add__(self, other):
        sum_mat = Matrix._create_mat(self.row(), self.col())
        for i in range(self.row()):
            for j in range(self.col()):
                sum_mat[i][j] = self._mat[i][j] + other._mat[i][j]
        return Matrix(sum_mat)
    
    def __sub__(self, other):
        sum_mat = Matrix._create_mat(self.row(), self.col())
        for i in range(self.row()):
            for j in range(self.col()):
                sum_mat[i][j] = self._mat[i][j] - other._mat[i][j]
        return Matrix(sum_mat)

    def __mul__(self, other):        
        prod_mat = Matrix._create_mat(self.row(), other.col())
        for i in range(self.row()):
            for j in range(other.col()):
                for k in range(self.col()):
                    prod_mat[i][j] += self._mat[i][k] * other._mat[k][j]                    
        return Matrix(prod_mat)

    def __str__(self):
        mat_str = ""
        for i in range(self.row()):
            for j in range(self.col()):
                mat_str += "{:3} ".format(self._mat[i][j])
            mat_str += "\n"
        return mat_str[:-1]

    def __eq__(self, other):
        if self.row() != other.row() or self.col() != other.col():
            return False
        for i in range(self.row()):
            for j in range(self.col()):
                if self._mat[i][j] != other._mat[i][j]:
                    return False
        return True


if __name__ == "__main__":
    m1 = Matrix([
        [1, 2, 3],
        [4, 5, 6]
    ])
    m2 = Matrix([
        [6, 5, 4],
        [3, 2, 1]
    ])
    m3 = Matrix([
        [3, -1],
        [2, -1],
        [1, -1]
    ])
    print("m1:")
    print(m1)
    print("m2:")
    print(m2)
    print("m3:")
    print(m3)
    print("m1 + m2:")
    print(m1 + m2)
    print("m1 - m2:")
    print(m1 - m2)
    print("m1 * m3:")
    print(m1 * m3)
    print("m1 == m1")
    print(m1 == m1)
    print("m1 == m2")
    print(m1 == m2)
    print("m1 == m3")
    print(m1 == m3)
