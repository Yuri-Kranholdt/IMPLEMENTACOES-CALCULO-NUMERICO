
class GaussJordan:
    def __init__(self, matrix):
        self.matrix = matrix
        self.max_i = len(matrix) - 1
        self.max_j = len(matrix[0]) - 1

    @staticmethod
    def mul_line(line, value):
        for i, element in enumerate(line):
            line[i] = element * value
        return line

    @staticmethod
    def subtract_lines(line1, line2):
        for i, element in enumerate(line2):
            line1[i] -= element
        return line1

    @staticmethod
    def show_matrix(matriz):
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                print(matriz[i][j], end=" ")
            print("\n")

    @staticmethod
    def check_zero_line(line):
        for j in range(len(line)):
            if line[j] != 0: return False
        return True

    def posto(self, matrix):
        # número de linhas não nulas da matriz
        counter = 0
        for i in range(len(matrix)):
            if not self.check_zero_line(matrix[i]): counter += 1
        return counter

    def check_zero_column(self, pivo_i, pivo_j):
        for i in range(pivo_i + 1, self.max_i+1):
            if self.matrix[i][pivo_j] != 0: return False
        return True

    def change_lines(self, pivo_i, pivo_j):
        for i in range(pivo_i + 1, self.max_i):
            if self.matrix[i][pivo_j] != 0:
                temp = self.matrix[pivo_i]
                self.matrix[pivo_i] = self.matrix[i]
                self.matrix[i] = temp
                if self.check_zero_column(pivo_i, pivo_j): return False
                return True

        return False  # não é possivel trocar linhas, passar para o proximo pivo

    def matrix_row_reduction(self):
        pivo_i = 0
        pivo_j = 0

        for i in range(self.max_i):
            pivo_value = self.matrix[pivo_i][pivo_j]

            for i_2 in range(pivo_i+1, self.max_i+1):
                if pivo_value == 0:
                    res = self.change_lines(pivo_i, pivo_j)
                    if not res: break
                    pivo_value = self.matrix[pivo_i][pivo_j]

                diag_inf_value = self.matrix[i_2][pivo_j]
                if diag_inf_value == 0: continue

                new_pivo_line = self.mul_line(self.matrix[pivo_i].copy(), diag_inf_value/pivo_value)
                self.matrix[i_2] = self.subtract_lines(self.matrix[i_2], new_pivo_line)

            pivo_i += 1
            pivo_j += 1

    def calculate_variables(self):
        # encontrar as variaveis de qualquer sistema quadrado
        result = []

        actual_var_i = self.max_i
        actual_var_j = self.max_j-1

        for i in range(self.max_i+1):
            temp = result.copy()
            line_result = self.matrix[actual_var_i][-1]
            if not temp:
                var_value = line_result / self.matrix[actual_var_i][actual_var_j]
                result.insert(0, var_value)
            else:
                for j in range(actual_var_j+1, self.max_j):
                    prev_var_value = temp.pop(0)
                    coefficient = self.matrix[actual_var_i][j]
                    line_result -= coefficient * prev_var_value

                var_value = line_result / self.matrix[actual_var_i][actual_var_j]
                result.insert(0, var_value)

            actual_var_i -= 1
            actual_var_j -= 1
        return result

    def rouche_coppeli(self):
        # matriz na forma escalonada

        coefficient_matrix = [line[:-1] for line in self.matrix]
        n_variables = len(coefficient_matrix[0])
        posto_a = self.posto(coefficient_matrix)
        posto_b = self.posto(self.matrix)

        if posto_a != posto_b:
            raise ValueError("Sistema não possui solução")

        elif posto_a == posto_b and posto_a == n_variables:
            return self.calculate_variables()

        raise ValueError("Sistema com infinitas soluções")

    def solve(self):
        self.matrix_row_reduction()
        self.show_matrix(self.matrix)
        return self.rouche_coppeli()


sis = [
    [2, 1, -1, 8],
    [1, 3, 2, 13],
    [3, -1, 1, 5]
]

print(GaussJordan(sis).solve())