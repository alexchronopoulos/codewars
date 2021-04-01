def test_rows(board):
	results = []
	for row in board:
		if ([1, 2, 3, 4, 5, 6, 7, 8 ,9] == sorted(row)):
			results.append(True)
		else:
			results.append(False)
	if False in results:
		return False
	else:
		return True

def test_columns(board):
	columnMatrix = []
	columnCounter = 0
	rowCounter = 0
	while rowCounter < 9:
		columnResults = []
		while columnCounter < 9:
			columnResults.append(board[columnCounter][rowCounter])
			columnCounter += 1
		columnMatrix.append(columnResults)
		columnCounter = 0
		rowCounter += 1
	return test_rows(columnMatrix)

def test_blocks(board):
	blocks = [row[0:3] for row in board]
	block1 = [row for row in blocks[0:3]]
	block1Row = [val for sublist in block1 for val in sublist]
	block2 = [row for row in blocks[3:6]]
	block2Row = [val for sublist in block2 for val in sublist]
	block3 = [row for row in blocks[6:9]]
	block3Row = [val for sublist in block3 for val in sublist]
	blockRows = [block1Row, block2Row, block3Row]
	return test_rows(blockRows)

def valid_solution(board):
	print(board)
	rowTest = test_rows(board)
	columnTest = test_columns(board)
	blockTest = test_blocks(board)
	if rowTest == True and columnTest == True and blockTest == True:
		return True
	else:
		return False

def test_answer():
    assert valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
						   [6, 7, 2, 1, 9, 5, 3, 4, 8],
						   [1, 9, 8, 3, 4, 2, 5, 6, 7],
						   [8, 5, 9, 7, 6, 1, 4, 2, 3],
						   [4, 2, 6, 8, 5, 3, 7, 9, 1],
						   [7, 1, 3, 9, 2, 4, 8, 5, 6],
						   [9, 6, 1, 5, 3, 7, 2, 8, 4],
						   [2, 8, 7, 4, 1, 9, 6, 3, 5],
						   [3, 4, 5, 2, 8, 6, 1, 7, 9]]) == True

    assert valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
						   [6, 7, 2, 1, 9, 0, 3, 4, 9],
						   [1, 0, 0, 3, 4, 2, 5, 6, 0],
						   [8, 5, 9, 7, 6, 1, 0, 2, 0],
						   [4, 2, 6, 8, 5, 3, 7, 9, 1],
						   [7, 1, 3, 9, 2, 4, 8, 5, 6],
						   [9, 0, 1, 5, 3, 7, 2, 1, 4],
						   [2, 8, 7, 4, 1, 9, 6, 3, 5],
						   [3, 0, 0, 4, 8, 1, 1, 7, 9]]) == False
						   
    assert valid_solution([[1, 3, 2, 5, 7, 9, 4, 6, 8], 
							[4, 9, 8, 2, 6, 1, 3, 7, 5], 
							[7, 5, 6, 3, 8, 4, 2, 1, 9], 
							[6, 4, 3, 1, 5, 8, 7, 9, 2], 
							[5, 2, 1, 7, 9, 3, 8, 4, 6], 
							[9, 8, 7, 4, 2, 6, 5, 3, 1], 
							[2, 1, 4, 9, 3, 5, 6, 8, 7], 
							[3, 6, 5, 8, 1, 7, 9, 2, 4], 
							[8, 7, 9, 6, 4, 2, 1, 3, 5]]) == False

    assert valid_solution([[1, 2, 3, 4, 5, 6, 7, 8, 9], 
							[2, 3, 4, 5, 6, 7, 8, 9, 1], 
							[3, 4, 5, 6, 7, 8, 9, 1, 2], 
							[4, 5, 6, 7, 8, 9, 1, 2, 3], 
							[5, 6, 7, 8, 9, 1, 2, 3, 4], 
							[6, 7, 8, 9, 1, 2, 3, 4, 5], 
							[7, 8, 9, 1, 2, 3, 4, 5, 6], 
							[8, 9, 1, 2, 3, 4, 5, 6, 7], 
							[9, 1, 2, 3, 4, 5, 6, 7, 8]]) == False

if __name__ == "__main__":
	test_answer()
