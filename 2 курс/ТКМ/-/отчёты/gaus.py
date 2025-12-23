import numpy as np

class GaussianEliminationSolver:
    """
    Решение системы линейных алгебраических уравнений (СЛАУ) методом Гаусса.
    """
    def __init__(self, matrix_and_size):
        self.coefficient_matrix = matrix_and_size[0]
        self.number_of_equations = matrix_and_size[1]

    def classic_elimination(self):
        """
        Классический метод Гаусса для решения СЛАУ.
        """
        print('Классический метод.')
        augmented_matrix = np.copy(self.coefficient_matrix)
        for pivot_row in range(0, self.number_of_equations - 1):
            for column_index in range(self.number_of_equations, pivot_row - 1, -1):
                augmented_matrix[pivot_row, column_index] /= augmented_matrix[pivot_row, pivot_row]
                for elimination_row in range(pivot_row + 1, self.number_of_equations):
                    augmented_matrix[elimination_row, column_index] -= augmented_matrix[pivot_row, column_index] * augmented_matrix[elimination_row, pivot_row]
        print(f'Преобразованная матрица: \n {augmented_matrix} \n')
        solution_vector = [0 for _ in range(self.number_of_equations)]
        solution_vector[self.number_of_equations - 1] = augmented_matrix[self.number_of_equations - 1, self.number_of_equations] / augmented_matrix[self.number_of_equations - 1, self.number_of_equations - 1]
        for row_index in range(self.number_of_equations - 2, -1, -1):
            sum_of_products = 0
            for column_index in range(row_index + 1, self.number_of_equations):
                sum_of_products += augmented_matrix[row_index, column_index] * solution_vector[column_index]
            solution_vector[row_index] = augmented_matrix[row_index, self.number_of_equations] - sum_of_products
        rounded_solution = [round(value, 3) for value in solution_vector]
        print(f'Результат: \n {rounded_solution} \n')
        return rounded_solution

    def optimal_elimination(self):
        """
        Метод оптимального исключения Гаусса.
        """
        print('Метод оптимального исключения Гаусса.')
        augmented_matrix = np.copy(self.coefficient_matrix)
        for pivot_row in range(0, self.number_of_equations - 1):
            for elimination_row in range(pivot_row + 1, self.number_of_equations):
                elimination_factor = augmented_matrix[elimination_row, pivot_row] / augmented_matrix[pivot_row, pivot_row]
                for column_index in range(pivot_row, self.number_of_equations + 1):
                    augmented_matrix[elimination_row, column_index] -= elimination_factor * augmented_matrix[pivot_row, column_index]
        print(f'Преобразованная матрица: \n {augmented_matrix} \n')
        solution_vector = [0 for _ in range(self.number_of_equations)]
        solution_vector[self.number_of_equations - 1] = augmented_matrix[self.number_of_equations - 1, self.number_of_equations] / augmented_matrix[self.number_of_equations - 1, self.number_of_equations - 1]
        for row_index in range(self.number_of_equations - 2, -1, -1):
            sum_of_products = 0
            for column_index in range(row_index + 1, self.number_of_equations):
                sum_of_products += augmented_matrix[row_index, column_index] * solution_vector[column_index]
            solution_vector[row_index] = (augmented_matrix[row_index, self.number_of_equations] - sum_of_products) / augmented_matrix[row_index, row_index]
        rounded_solution = [round(value, 3) for value in solution_vector]
        print(f'Результат: \n {rounded_solution} \n')
        return rounded_solution

    def jordan_elimination(self):
        """
        Метод Гаусса-Жордана.
        """
        print('Метод Гаусса-Жордана.')
        augmented_matrix = np.copy(self.coefficient_matrix)
        for pivot_row in range(0, self.number_of_equations):
            for elimination_row in range(0, self.number_of_equations):
                if pivot_row == elimination_row:
                    continue
                else:
                    elimination_factor = augmented_matrix[elimination_row, pivot_row] / augmented_matrix[pivot_row, pivot_row]
                    for column_index in range(pivot_row, self.number_of_equations + 1):
                        augmented_matrix[elimination_row, column_index] -= elimination_factor * augmented_matrix[pivot_row, column_index]
        print(f'Преобразованная матрица: \n {augmented_matrix} \n')
        solution_vector = [0 for _ in range(self.number_of_equations)]
        for row_index in range(0, self.number_of_equations):
            solution_vector[row_index] = augmented_matrix[row_index, self.number_of_equations] / augmented_matrix[row_index, row_index]
        rounded_solution = [round(value, 3) for value in solution_vector]
        print(f'Результат: \n {rounded_solution} \n')
        return rounded_solution
