import unittest
from university import University


class TestR1(unittest.TestCase):

    def test_constructor(self):
        u = University("PoliMi")
        self.assertEqual(u.get_name(), "PoliMi")

    def test_rector(self):
        u = University("PoliMi")
        u.set_rector("Ferruccio", "Resta")
        self.assertEqual(u.get_rector(), "Ferruccio Resta")


class TestR2(unittest.TestCase):

    def setUp(self):
        self._uni = University("Politecnico")

    def test_add_student(self):
        sid = self._uni.add_student("Pietro", "Chiavassa")
        self.assertEqual(sid, 10000)

    def test_add_multiple_students(self):
        sid_1 = self._uni.add_student("Pietro", "Chiavassa")
        sid_2 = self._uni.add_student("Edoardo", "Giusto")
        self.assertEqual(sid_1, 10000)
        self.assertEqual(sid_2, 10001)

    def test_student_info(self):
        self._uni.add_student("Pietro", "Chiavassa")
        self.assertEqual(self._uni.get_student_info(10000), "10000 Pietro Chiavassa")


class TestR3(unittest.TestCase):

    def setUp(self):
        self._uni = University("Politecnico")

    def test_add_course(self):
        cid = self._uni.add_course("Programmazione", "Bartolomeo Montrucchio")
        self.assertEqual(cid, 10)

    def test_add_multiple_courses(self):
        cid_1 = self._uni.add_course("Programmazione", "Bartolomeo Montrucchio")
        cid_2 = self._uni.add_course("Algoritmi", "Filippo Gandino")
        self.assertEqual(cid_1, 10)
        self.assertEqual(cid_2, 11)

    def test_course_info(self):
        cid_1 = self._uni.add_course("Programmazione", "Bartolomeo Montrucchio")
        self.assertEqual(self._uni.get_course_info(10), "10,Programmazione,Bartolomeo Montrucchio")


class TestR4(unittest.TestCase):

    def setUp(self):
        self._uni = University("Politecnico")
        self._uni.add_course("Programmazione", "Bartolomeo Montrucchio")
        self._uni.add_course("Algoritmi", "Filippo Gandino")

        self._uni.add_student("Pietro", "Chiavassa")
        self._uni.add_student("Edoardo", "Giusto")

    def test_get_attendees(self):
        self._uni.register_to_course(10000, 10)
        self.assertEqual(self._uni.get_attendees(10), "10000 Pietro Chiavassa")

    def test_get_small_study_plan(self):
        self._uni.register_to_course(10000, 10)
        self.assertEqual(self._uni.get_study_plan(10000), ["10,Programmazione,Bartolomeo Montrucchio"])

    def test_get_multiple_attendees(self):
        self._uni.register_to_course(10000, 10)
        self._uni.register_to_course(10001, 10)
        self.assertEqual(self._uni.get_attendees(10), "10000 Pietro Chiavassa\n10001 Edoardo Giusto")

    def test_get_study_plan(self):
        self._uni.register_to_course(10000, 10)
        self._uni.register_to_course(10000, 11)
        self.assertEqual(self._uni.get_study_plan(10000), ["10,Programmazione,Bartolomeo Montrucchio", "11,Algoritmi,Filippo Gandino"])













