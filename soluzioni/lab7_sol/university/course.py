class Course:

    def __init__(self, id, title, teacher):
        self._id = id
        self._title = title
        self._teacher = teacher
        self._students = []

    def get_title(self):
        return self._title

    def get_teacher(self):
        return self._teacher
    
    def get_id(self):
        return self._id

    def add_student(self, student):
        # aggiungo studente alla lista studenti
        self._students.append(student)
    
    def get_students(self):
        return self._students
    
    def __str__(self):
        # rappresentazione in stringa del corso
        return "{},{},{}".format(self._id, self._title, self._teacher)


    
