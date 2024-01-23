def find_cats(matrix):
    def dfs(i, j, cat_id):
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] != 1:
            return
        matrix[i][j] = cat_id
        # Exploring diagonally
        dfs(i-1, j-1, cat_id)
        dfs(i-1, j+1, cat_id)
        dfs(i+1, j-1, cat_id)
        dfs(i+1, j+1, cat_id)

    cat_id = 2  # Starting from 2 because 1 is used in the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                dfs(i, j, cat_id)
                cat_id += 1

    return cat_id - 2, matrix  # Subtract 2 to get the count (as we started from 2)

# Example input
input_matrix = []

with open('input.txt') as file:
    for line in file:
        input_matrix.append(list(map(int, line.split())))

cat_count, output_matrix = find_cats(input_matrix)

for ind_row in range(len(output_matrix)):
    for ind_col in range(len(output_matrix[0])):
        val = output_matrix[ind_row][ind_col]

        if val != 0:
            output_matrix[ind_row][ind_col] = val - 1

print(cat_count)

for row in output_matrix:
    print(' '.join(map(str, row)))

