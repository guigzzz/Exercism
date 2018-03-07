

move = {
    'r': lambda x, y: (x, y + 1), 
    'd': lambda x, y: (x + 1, y), 
    'l': lambda x, y: (x, y - 1), 
    'u': lambda x, y: (x - 1, y)
}

nxt = {'r': 'd', 'd': 'l',
       'l': 'u', 'u': 'r'}

def spiral(size):

    if not size: return []

    matrix = [[0] * size for _ in range(size)]

    for j in range(size):
        matrix[0][j] = j + 1
        matrix[j][-1] = size + j

    x, y = size - 1, size - 1
    direction = 'l'
    
    for i in range(2 * size - 1, size ** 2 + 1):
        matrix[x][y] = i

        dx, dy = move[direction](x, y)
        if matrix[dx][dy] > 0:
            direction = nxt[direction]

        x, y = move[direction](x, y)

    return matrix
