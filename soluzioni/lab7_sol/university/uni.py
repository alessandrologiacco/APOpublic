from typing import List
from university.student import Student
from university.course import Course


class University:

    # R1
    def __init__(self, name: str) -> None:
        # proprietà dell'università
        self._name = name
        self._rector_name = None
        self._rector_surname = None

        # contatori per identificativi
        self._student_id_counter = 10000
        self._course_id_counter = 10

        # collezioni
        self._students = {}
        self._courses = {}

    def get_name(self) -> str:
        return self._name

    def set_rector(self, name: str, surname: str) -> None:
        self._rector_name = name
        self._rector_surname = surname

    def get_rector(self) -> str:
        # stringa con nome e cognome rettore
        return "{} {}".format(self._rector_name, self._rector_surname)

    # R2
    def add_student(self, name: str, surname: str) -> int:
        # uso valore contatore per numero matricola
        new_id = self._student_id_counter
        # creo un nuovo studente e lo aggiungo al dizionario studenti
        self._students[new_id] = Student(new_id, name, surname)
        # incremento contatore numero matricola
        self._student_id_counter += 1
        return new_id        

    def get_student_info(self, student_id: int) -> str:
        # ottengo studente dal dizionario tramite identificativo e restituisco rappresentazione in stringa (__str__)
        return str(self._students[student_id])    

    # R3
    def add_course(self, title: str, teacher: str) -> int:
        # uso valore contatore per codice corso
        new_id = self._course_id_counter
        # credo un nuovo corso e lo aggiunto al dizionario corsi
        self._courses[new_id] = Course(new_id, title, teacher)
        # incremento contatore codice corso
        self._course_id_counter += 1
        return new_id

    def get_course_info(self, course_id: int) -> str:
        # ottengo corso dal dizionario tramite identificativo e restituisco rappresentazione in stringa (__str__)
        return str(self._courses[course_id])

    # R4
    def register_to_course(self, student_id: int, course_id: int) -> None:
        # ottengo oggetti studente e corso dai dizionari tramite identificativi
        student = self._students[student_id]
        course = self._courses[course_id]
        # aggiungo corso allo studente
        student.add_course(course)
        # aggiungo studente al corso
        course.add_student(student)        

    def get_attendees(self, course_id: int) -> str:
        # ottengo corso dal dizionario e la sua lista studenti (get_students())
        # creo lista con rappresentazione in stringa di ogni studente nella lista restituita da get_students()
        # unisco elementi lista aggiungendo tramite a-capo
        return "\n".join([str(s) for s in self._courses[course_id].get_students()])

    def get_study_plan(self, student_id: int) -> List[str]:
        # ottengo studente dal dizionario e la sua lista corsi (get_courses())
        # creo lista con rappresentazione in stringa di ogni corso nella lista restituita da get_courses()
        return [str(s) for s in self._students[student_id].get_courses()]
