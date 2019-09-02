import chess
import chess.svg


moves = ["e4", "e5", "Qh5", "Nc6", "Bc4", "Nf6", "Qxf7"]

board = chess.Board()
image = chess.svg.board(board=board)
with open('board-0.svg', 'w') as f:
    f.write(image)

for i, move in enumerate(moves):
    board.push_san(move)
    image = chess.svg.board(board=board, lastmove=board.peek())
    with open('board-{}.svg'.format(i+1), 'w') as f:
        f.write(image)
