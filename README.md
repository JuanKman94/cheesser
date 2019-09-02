# Chesser

## Interesting Packages

* [ ] python-chess (PP)
* [ ] chesstab (PP)
* [ ] chess_py (pygotham talk) (both)
* [ ] PySimpleGUI (JC)
* [ ] pgn-read (JC)


## python-chess

To see a simple demo:

- Create a Python virtual environment
- Install python-chess
- Run python-chess.py
- Visit python-chess.html

Eight SVG images are created: the initial board plus seven moves until
the end of the game.  The initial and final squares of each move are
highlighted. The parameter coordinates=False can be added to
chess.svg.board to hide the a...h and 1...8 labels around the board.

The game is the Scholar's mate that is shown in the Introduction of
the python-chess documentation.

The seventh image, without the last move squares hightlighted, can be
used as a learning exercise: show the image to a student and ask them
to define what move should the white team do to win the game.

Next steps are:

* [ ] read a PGN file
* [ ] show the SVG images in a tkinter application
