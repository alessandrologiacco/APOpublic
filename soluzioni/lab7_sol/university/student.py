class Student:

    def __init__(self, id, name, surname):
        self._id = id
        self._name = name
        self._surname = surname
        self._courses = []

    def get_name(self):
        return self._name

    def get_surname(self):
        return self._surname
    
    def get_id(self):
        return self._id

    def add_course(self, course):
        # aggiungo corso alla lista corsi
        self._courses.append(course)
    
    def get_courses(self):
        return self._courses

    def __str__(self):
        # rappresentazione in stringa dello studente
        return "{} {} {}".format(self._id, self._name, self._surname)
