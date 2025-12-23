import tabulate


def triangular_fact_method(A,B):
    row = 4
    column = 4
    L = [[0 for i in range(column)] for i in range(row)]
    U = [[0 for i in range(column)] for i in range(row)]
    Z = [[0] for i in range(row)]
    X = [[0] for i in range(row)]
    for i in range(row):
        U[i][i] = 1
        L[i][0] = A[i][0]
        for j in range(i, column):
            sum0 = sum([L[j][s] * U[s][i] for s in range(0, j)])  # range from index 0
            L[j][i] = round(A[j][i] - sum0,2)
        for j in range(i + 1, column):
            sum1 = sum([L[i][s] * U[s][j] for s in range(i)])  # range from index 0
            U[i][j] = round((A[i][j] - sum1) / L[i][i],2)

    Z[0][0] = B[0][0]/L[0][0]
    for i in range(1, row):
        sum3 = sum([L[i][k] * Z[k][0] for k in range(i)])
        Z[i][0] = round((B[i][0] - sum3) / L[i][i], 2)

    X[3][0] = Z[3][0]
    for i in range(row-2, -1, -1):
        sum4 = sum([U[i][j]*X[j][0] for j in range(i+1,row)])
        #print(sum4)
        X[i][0] = Z[i][0] - sum4
    print('Нижняя матрица:\n', tabulate.tabulate(L))
    print('Верхняя матрица:\n', tabulate.tabulate(U))
    print('Матрица Z:\n', tabulate.tabulate(Z))
    print('Матрица X:\n', tabulate.tabulate(X))
    return(X)


def squart_method(A,B):
    column = row = 4
    R = [[0 for i in range(column)] for i in range(row)]
    Z = [[0] for i in range(row)]
    X = [[0] for i in range(row)]
    R[0][0] = A[0][0] ** 0.5
    for i in range(row):
        R[0][i] = A[0][i]/R[0][0]
    for i in range(1, row):
        for j in range(i, row):
            if i == j:
                sum0 = sum([R[k][i] * R[k][i] for k in range(row)])
                R[i][i] = (A[i][i] - sum0) ** 0.5
            else:
                sum1 = sum(R[k][i] * R[k][j] for k in range(row))
                R[i][j] = (A[i][j] - sum1) / R[i][i]
    print('Матрица R:\n', tabulate.tabulate(R))
    for i in range(row):
        sum2 = sum(R[k][i]*Z[k][0] for k in range(i))
        Z[i][0] = (B[i][0]-sum2)/R[i][i]
    print('Матрица Z:\n', tabulate.tabulate(Z))

    X[3][0] = Z[3][0]/R[3][3]
    for i in range(row - 2, -1, -1):
        sum3 = sum([R[i][j] * X[j][0] for j in range(i + 1, row)])
        # print(sum4)
        X[i][0] = (Z[i][0] - sum3)/R[i][i]

    print('Матрица X:\n', tabulate.tabulate(X))


if __name__ == '__main__':
    matrix_a = [[5, 7, 6, 5], [7, 10, 8, 7],
                  [6, 8, 10, 9], [5, 7, 9, 10]]
    print('Матрица A:\n', tabulate.tabulate(matrix_a))
    matrix_b = [[23], [32], [33], [31]]
    print('Матрица B:\n', tabulate.tabulate(matrix_b))

    print('Метод Краута')
    matrix_x_1 = triangular_fact_method(matrix_a, matrix_b)

    print('\n')

    print('Метод Холецкого')
    squart_method(matrix_a, matrix_b)



