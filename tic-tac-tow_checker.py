import pdb

def check_winning_row(board):
    for row in board:
        print(f'row: {row}')
        if 0 not in set(row):
            if 1 in set(row) and 2 not in set(row):
                return 1
            if 2 in set(row) and 1 not in set(row):
                return 2
    if 0 in [item for lists in board for item in lists]:
        return -1
    else:
        return 0 

def check_winning_column(board):
    columns = list(zip(*board))
    print(columns)
    return check_winning_row(columns)
  
def check_winning_diagonal(board):
    diagonal1 = [board[0][0], board[1][1], board[2][2]]
    diagonal2 = [board[0][2], board[1][1], board[2][0]]
    # If neither diagonal is a win, we should return -1
    placeholder = [0, 0, 0]
    return check_winning_row([diagonal1, diagonal2])

def is_solved(board):
    print(f'board: {board}')
    check1 = check_winning_row(board)
    print(f'check1: {check1}')
    check2 = check_winning_column(board)
    print(f'check2: {check2}')
    check3 = check_winning_diagonal(board)
    print(f'check3: {check3}')
    results = [check1, check2, check3]
    return max(results) 

def test_answer():
    assert is_solved(
			# not yet finished
			[[0, 0, 1],
			 [0, 1, 2],
			 [2, 1, 0]]
	) == -1
    assert is_solved(
		# winning row
		[[1, 1, 1],
		 [0, 2, 2],
		[0, 0, 0]]
	) == 1

    assert is_solved(
		# winning column
		 [[2, 1, 2],
		  [2, 1, 1],
		  [1, 1, 2]]
	) == 1
    assert is_solved(
		# draw
		[[2, 1, 2],
		 [2, 1, 1],
		 [1, 2, 1]]
	) == 0
    assert is_solved(
            # winning diagonal
            [[1,2,0],
              [0,1,2], 
              [0,0,1]]
    ) == 1
    assert is_solved(
        # winning row
        [[2,1,1],
          [0,1,1],
          [2,2,2]]
    ) == 2

if __name__ == "__main__":
	test_answer()
