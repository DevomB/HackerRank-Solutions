def diagonalDifference(arr):
    matrix_len = len(arr[0])
    left_diagonal_sum = sum(arr[i][i] for i in range(matrix_len))
    right_diagonal_sum = sum(arr[i][matrix_len - (i + 1)] for i in range(matrix_len))

    return abs(left_diagonal_sum - right_diagonal_sum)
