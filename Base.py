from array import *
from Pieces import *
from BuildBoard import *
from CheckList import *

# Main File, this is the one to run to start a game

# Create pieces and add to list (Team, X Co-ordinate, Y Co-Ordinate, Board Notation, Piece Type, Piece In Play?)
pieceslist = [Pieces("Black", 1, 7, "bR ", "Rook", True), Pieces("Black", 2, 7, "bn ", "Knight", True),
              Pieces("Black", 3, 7, "bB ", "Bishop", True), Pieces("Black", 4, 7, "bQ ", "Queen", True),
              Pieces("Black", 5, 7, "bK ", "King", True), Pieces("Black", 6, 7, "bB ", "Bishop", True),
              Pieces("Black", 7, 7, "bn ", "Knight", True), Pieces("Black", 8, 7, "bR ", "Rook", True),
              Pieces("Black", 1, 6, "bP ", "Pawn", True), Pieces("Black", 2, 6, "bP ", "Pawn", True),
              Pieces("Black", 3, 6, "bP ", "Pawn", True), Pieces("Black", 4, 6, "bP ", "Pawn", True),
              Pieces("Black", 5, 6, "bP ", "Pawn", True), Pieces("Black", 6, 6, "bP ", "Pawn", True),
              Pieces("Black", 7, 6, "bP ", "Pawn", True), Pieces("Black", 8, 6, "bP ", "Pawn", True),
              Pieces("White", 1, 0, "wR ", "Rook", True), Pieces("White", 2, 0, "wn ", "Knight", True),
              Pieces("White", 3, 0, "wB ", "Bishop", True), Pieces("White", 4, 0, "wK ", "King", True),
              Pieces("White", 5, 0, "wQ ", "Queen", True), Pieces("White", 6, 0, "wB ", "Bishop", True),
              Pieces("White", 7, 0, "wn ", "Knight", True), Pieces("White", 8, 0, "wR ", "Rook", True),
              Pieces("White", 1, 6, "wP ", "Pawn", True), Pieces("White", 2, 1, "wP ", "Pawn", True),
              Pieces("White", 3, 1, "wP ", "Pawn", True), Pieces("White", 4, 1, "wP ", "Pawn", True),
              Pieces("White", 5, 1, "wP ", "Pawn", True), Pieces("White", 6, 1, "wP ", "Pawn", True),
              Pieces("White", 7, 1, "wP ", "Pawn", True), Pieces("White", 8, 1, "wP ", "Pawn", True)]

# This builds the board for the start of the game with all pieces in starting positions
buildboard(pieceslist)

# Create base variables
checkmate = False
player1inputx = ""
player1inputy = ""
player2inputx = ""
player2inputy = ""
player1inputnewy = ""
player1inputnewx = ""
currentplayer = ""

while checkmate is False and player1inputx != "Quit" and player2inputx != "Quit":
    player1ValidPiece = False
    player2ValidPiece = False
    # Player 1 start
    while player1ValidPiece is False:

        # selecting a piece to move
        player1inputx = input("White's turn, X coord: ")
        if player1inputx == "Quit":
            break

        player1inputx = int(player1inputx)
        player1inputy = input("Y coord: ")
        if player1inputy == "Quit":
            break
        player1inputy = int(player1inputy)

        # Check to see if piece selected is valid, ie is in play and correct team
        player1ValidPiece = checklist(pieceslist, player1inputx, player1inputy, "White")

        # If not valid then return to start of while statement and ask again
        if player1ValidPiece is False:
            print("Invalid Piece")
            break

        # Ask for new position for piece
        player1inputnewx = int(input("New X: "))
        player1inputnewy = int(input("New Y: "))

        # update pieces list after checking that the piece is allowed to move to that location.
        pieceslist = checklistdestination(pieceslist, player1inputx, player1inputy, player1inputnewx, player1inputnewy)

        # Rebuild board
        buildboard(pieceslist)

    # Player 2 Start
    while player2ValidPiece is False:

        # Selecting a piece to move
        player2inputx = input("Black's turn, X coord: ")
        if player2inputx == "Quit":
            break

        player2inputx = int(player2inputx)
        player2inputy = input("Y coord: ")
        if player2inputy == "Quit":
            break
        player2inputy = int(player2inputy)

        # Check to see if piece selected is valid, ie is in play and correct team
        player2ValidPiece = checklist(pieceslist, player2inputx, player2inputy, "Black")

        if player2ValidPiece is False:
            print("Invalid Piece")
            break

        # Ask for new position for piece
        player2inputnewx = int(input("New X: "))
        player2inputnewy = int(input("New Y: "))

        # update pieces list after checking that the piece is allowed to move to that location.
        pieceslist = checklistdestination(pieceslist, player2inputx, player2inputy, player2inputnewx, player2inputnewy)

        # Rebuild board
        buildboard(pieceslist)
