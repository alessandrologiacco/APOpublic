import unittest
from chess.board import Board, Piece, ChessException
from chess.manager import ChessManager
from chess.competition import Player


class TestR1(unittest.TestCase):

    def test_board(self):
        b = Board("board", 3)
        self.assertEqual(b.name, "board")
        self.assertEqual(b.dim, 3)

    def test_add_get_piece(self):
        b = Board("board", 7)
        b.add_piece(Piece.KING, 2, 5)
        b.add_piece(Piece.ROOK, 1, 1)
        b.add_piece(Piece.PAWN, 6, 4)
        b.add_piece(Piece.QUEEN, 2, 4)
        b.add_piece(Piece.KNIGHT, 3, 6)
        b.add_piece(Piece.PAWN, 0, 5)
        b.add_piece(Piece.BISHOP, 3, 3)

        self.assertEqual(Piece.KING, b.get_piece(2, 5))
        self.assertEqual(Piece.ROOK, b.get_piece(1, 1))
        self.assertEqual(Piece.PAWN, b.get_piece(6, 4))
        self.assertEqual(Piece.QUEEN, b.get_piece(2, 4))
        self.assertEqual(Piece.KNIGHT, b.get_piece(3, 6))
        self.assertEqual(Piece.PAWN, b.get_piece(0, 5))
        self.assertEqual(Piece.BISHOP, b.get_piece(3, 3))
        self.assertEqual(None, b.get_piece(2, 2))

    def test_add_piece_exception(self):
        b = Board("board", 3)
        self.assertRaises(ChessException, b.add_piece, Piece.BISHOP, 2, 3)

    def test_get_piece_exception(self):
        b = Board("board", 9)
        self.assertRaises(ChessException, b.get_piece, 9, 3)

    def test_remove_piece(self):
        b = Board("board", 3)
        self.assertEqual(None, b.get_piece(2, 2))
        b.add_piece(Piece.BISHOP, 2, 2)
        self.assertEqual(Piece.BISHOP, b.get_piece(2, 2))
        b.add_piece(None, 2, 2)
        self.assertEqual(None, b.get_piece(2, 2))


class TestR2(unittest.TestCase):

    @staticmethod
    def setup_board(name):
        b = Board(name, 7)
        b.add_piece(Piece.KING, 2, 5)
        b.add_piece(Piece.ROOK, 1, 1)
        b.add_piece(Piece.PAWN, 6, 4)
        b.add_piece(Piece.QUEEN, 2, 4)
        b.add_piece(Piece.KNIGHT, 3, 6)
        b.add_piece(Piece.PAWN, 0, 5)
        b.add_piece(Piece.BISHOP, 3, 3)
        return b

    def test_add_get_board(self):
        mg = ChessManager()
        b1 = Board("board_1", 3)
        b2 = Board("board_2", 5)
        b3 = TestR2.setup_board("board_3")
        mg.add_board(b1)
        mg.add_board(b2)
        mg.add_board(b3)
        self.assertEqual(b1, mg.get_board("board_1"))
        self.assertEqual(b2, mg.get_board("board_2"))
        self.assertEqual(b3, mg.get_board("board_3"))

    def test_add_get_player(self):
        mg = ChessManager()
        p1 = Player("Antonio", "Italian", 26)
        p2 = Player("Mohammad", "Iranian", 40)
        mg.add_player(p1)
        mg.add_player(p2)
        self.assertEqual(p1, mg.get_player("Antonio"))
        self.assertEqual(p2, mg.get_player("Mohammad"))

    def test_player_repr(self):
        p1 = Player("Enrico", "Italian", 22)
        self.assertEqual("Enrico,Italian,22", p1.__repr__())

    def test_get_boards_of_player(self):
        mg = ChessManager()

        b1 = Board("board_1", 3)
        b2 = Board("board_2", 5)
        b3 = TestR2.setup_board("board_3")
        mg.add_board(b1)
        mg.add_board(b2)
        mg.add_board(b3)

        mg.add_player(Player("Mohammad", "Iranian", 39))
        mg.add_player_to_board("Mohammad", "board_1")
        mg.add_player_to_board("Mohammad", "board_2")
        mg.add_player_to_board("Mohammad", "board_3")

        boards = mg.get_boards_of_player("Mohammad")
        self.assertEqual(3, len(boards))
        self.assertTrue(b1 in boards)
        self.assertTrue(b2 in boards)
        self.assertTrue(b3 in boards)

    def test_get_board_with_multiple_players(self):
        mg = ChessManager()

        b1 = Board("board_1", 3)
        b2 = Board("board_2", 5)
        b3 = TestR2.setup_board("board_3")
        mg.add_board(b1)
        mg.add_board(b2)
        mg.add_board(b3)

        mg.add_player(Player("Mohammad", "Iranian", 39))
        mg.add_player_to_board("Mohammad", "board_1")
        mg.add_player_to_board("Mohammad", "board_2")

        mg.add_player(Player("Antonio", "Italian", 25))
        mg.add_player_to_board("Antonio", "board_3")
        mg.add_player_to_board("Antonio", "board_2")

        boards = mg.get_boards_of_player("Mohammad")
        self.assertEqual(2, len(boards))
        self.assertTrue(b1 in boards)
        self.assertTrue(b2 in boards)

        boards = mg.get_boards_of_player("Antonio")
        self.assertEqual(2, len(boards))
        self.assertTrue(b2 in boards)
        self.assertTrue(b3 in boards)


class TestR3(unittest.TestCase):

    @staticmethod
    def add_players(mg):
        mg.add_player(Player("Mohammad", "Iranian", 39))
        mg.add_player(Player("Antonio", "Italian", 25))
        mg.add_player(Player("Edoardo", "Italian", 29))

    def test_create_tournament(self):
        mg = ChessManager()
        mg.create_tournament("Regionali Lombardia")
        self.assertRaises(ChessException, mg.create_tournament, "Regionali Lombardia")

    def test_add_player_score(self):
        mg = ChessManager()
        TestR3.add_players(mg)

        mg.create_tournament("Nazionali Firenze")
        mg.add_player_score("Nazionali Firenze", "Antonio", 77)
        mg.add_player_score("Nazionali Firenze", "Mohammad", 33)

        self.assertRaises(ChessException, mg.add_player_score, "Nazionali Firenze", "Pietro", 21)

    def test_get_leading_player(self):
        mg = ChessManager()
        TestR3.add_players(mg)
        mg.create_tournament("Nazionali Firenze")
        mg.add_player_score("Nazionali Firenze", "Antonio", 77)
        mg.add_player_score("Nazionali Firenze", "Edoardo", 99)
        mg.add_player_score("Nazionali Firenze", "Mohammad", 33)
        self.assertEqual("Edoardo:99", mg.get_leading_player("Nazionali Firenze"))

    def test_get_leading_player_of_empty_tournament(self):
        mg = ChessManager()
        TestR3.add_players(mg)
        mg.create_tournament("Nazionali Firenze")
        self.assertEqual(None, mg.get_leading_player("Nazionali Firenze"))
        mg.add_player_score("Nazionali Firenze", "Mohammad", 21)
        self.assertEqual("Mohammad:21", mg.get_leading_player("Nazionali Firenze"))


class TestR5(unittest.TestCase):

    def test_board5(self):
        mg = ChessManager()
        b = mg.fill_queens("b", 5)
        self._check_configuration(b)

    def test_board8(self):
        mg = ChessManager()
        b = mg.fill_queens("b", 5)
        self._check_configuration(b)

    def test_Board10(self):
        mg = ChessManager()
        b = mg.fill_queens("b", 5)
        self._check_configuration(b)

    def _check_configuration(self, b):
        count_tot = 0
        for i in range(b.dim):
            count_row = 0
            count_col = 0
            for j in range(b.dim):
                if (b.get_piece(i, j) is not None) and (b.get_piece(i, j) == Piece.QUEEN):
                    count_tot += 1
                    count_row += 1
                if (b.get_piece(j, i) is not None) and (b.get_piece(j, i) == Piece.QUEEN):
                    count_col += 1
            if count_row > 1 or count_col > 1:
                self.fail("Duplicated element in row or column")
        if count_tot != b.dim:
            self.fail("Not the right number of queens")

        # controllo in diagonale
        for i in range(b.dim):
            count = [0, 0, 0, 0]
            for j in range(b.dim - i):
                if (b.get_piece(i+j, j) is not None) and (b.get_piece(i+j, j) == Piece.QUEEN):
                    count[0] += 1

                if (b.get_piece(j, i+j) is not None) and (b.get_piece(j, i+j) == Piece.QUEEN):
                    count[1] += 1

                if (b.get_piece(i+j, b.dim-j-1) is not None) and (b.get_piece(i+j, b.dim-j-1) == Piece.QUEEN):
                    count[2] += 1

                if (b.get_piece(j, b.dim-i-j-1) is not None) and (b.get_piece(j, b.dim-i-j-1) == Piece.QUEEN):
                    count[3] += 1

            if count[0] > 1 or count[1] > 1 or count[2] > 1 or count[3] > 1:
                self.fail("Duplicated elements on diagonals")

