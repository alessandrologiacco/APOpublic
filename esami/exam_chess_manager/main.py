from chess.board import Board, Piece, ChessException
from chess.manager import ChessManager
from chess.competition import Player


def main():
    # R1
    print("------------ R1 --------------")
    b1 = Board("b1", 5)
    print(b1.name)  # b1
    print(b1.dim)  # 5

    b1.add_piece(Piece.ROOK, 0, 0)
    b1.add_piece(Piece.KING, 4, 4)
    b1.add_piece(Piece.BISHOP, 2, 3)
    b1.add_piece(Piece.PAWN, 3, 0)

    print(b1.get_piece(0, 0))   # ROOK
    print(b1.get_piece(4, 4))   # KING
    print(b1.get_piece(2, 3))   # BISHOP
    print(b1.get_piece(3, 0))   # PAWN
    print(b1.get_piece(1, 1))   # None

    b1.add_piece(None, 0, 0)
    print(b1.get_piece(0, 0))  # None

    try:
        b1.add_piece(Piece.ROOK, 5, 5)
        print("Undetected wrong insert position")
    except ChessException:
        print("Exception correctly identified")  # Exception correctly identified

    try:
        b1.get_piece(5, 5)
        print("Undetected wrong lookup position")
    except ChessException:
        print("Exception correctly identified")  # Exception correctly identified

    # R2
    print("------------ R2 --------------")
    mg = ChessManager()

    mg.add_board(Board("b2", 2))
    mg.add_board(Board("b3", 3))
    mg.add_board(Board("b4", 4))
    out = mg.get_board("b2")
    print(out.name)  # b2

    mg.add_player(Player("Edoardo", "Italian", 30))
    print(mg.get_player("Edoardo"))  # Edoardo, Italian, 29

    mg.add_player_to_board("Edoardo", "b2")
    mg.add_player_to_board("Edoardo", "b4")
    boards = mg.get_boards_of_player("Edoardo")
    print([b.name for b in boards])  # ['b2', 'b4']

    # R3
    print("-------------- R3 ---------------")
    mg.add_player(Player("Gustavo", "Colombian", 36))
    mg.add_player(Player("Pietro", "Italian", 25))

    mg.create_tournament("Regionali Torino")
    mg.create_tournament("Nazionali Roma")
    mg.add_player_score("Regionali Torino", "Edoardo", 33)
    mg.add_player_score("Regionali Torino", "Gustavo", 55)
    mg.add_player_score("Regionali Torino", "Pietro", 11)
    print(mg.get_leading_player("Regionali Torino"))    # Gustavo:55
    print(mg.get_leading_player("Nazionali Roma"))  # None

    try:
        mg.create_tournament("Nazionali Roma")
        print("Failed to detect duplicated tournament")
    except ChessException:
        print("Duplicated tournament correctly identified")  # Duplicated tournament correctly identified

    try:
        mg.add_player_score("Nazionali Roma", "Filippo", 99)
        print("Failed to detect non existent player")
    except ChessException:
        print("Non-existent player correctly detected")  # Non-existent player correctly detected

    # R5
    print("-------------- R5 ---------------");
    print_board(mg.fill_queens("bq", 10))  # controllare correttezza


# FUNZIONE DI SUPPORTO PER STAMPARE LA BOARD
def print_board(b: Board) -> None:
    if not b:
        print(b)
        return
    for i in range(b.dim):
        for j in range(b.dim):
            print("{: >7}".format(b.get_piece(i, j) if b.get_piece(i, j) is not None else "None"), end="")
        print("")


if __name__ == "__main__":
    main()
