#Pegs puzzle problem
def possible_moves(board: str):
    """Return all possible moves given a board position."""
    index_X = findIndex(board,'X')
    possible_move = []
    strLen = len(board)
    for X in index_X:
        if (X+2 <strLen):
            if board[X+2]=='o':
                possible_move.append((X,'R'))
        if (X-2 >= 0):
            if board[X-2]=='o':
                possible_move.append((X,'L'))

    return possible_move

def apply_move(board: str, move:tuple):
    """Apply given Move to the board and return the new board."""
    x, direction = move;
    # print(x,direction)
    boardTemp = list(board)
    if direction == 'L':
        boardTemp[x-2] = 'X'
        boardTemp[x-1] = 'o'
        boardTemp[x] = 'o'
    if direction == 'R':
        boardTemp[x+2] = 'X'
        boardTemp[x+1] = 'o'
        boardTemp[x] = 'o'
    boardTemp = ''.join([str(elem) for elem in boardTemp])
    # print(str(boardTemp))
    return boardTemp

def is_win_board(board:str):
    """Defines whether a given board has reached the win condition."""
    print(board)
    boardTemp = list(board)
    return boardTemp.count("X") == 1


def findIndex(s:str, chr):
    index = []
    for i in range(len(s)):
        if s[i] == chr:
            index.append(i)
    return index

travesed = [] # To keep track of boards that are already checked and hence avoid infinite loop/recursion
def pegsSolution(board: str):
    """Return a list of moves that results in a board with a single peg."""
    if is_win_board(board):
        return []  # win condition
    travesed.append(board)
    for move in possible_moves(board):
        tempBoard = apply_move(board, move)
        if tempBoard not in travesed:
            solution = pegsSolution(tempBoard)
            if solution is not None:
                return [move] + solution
    return None  # lose condition



if __name__ == '__main__':
   gameBoard = 'XoXX' # should return [(3, 'L'), (0, 'R')]
   print(pegsSolution(gameBoard))
