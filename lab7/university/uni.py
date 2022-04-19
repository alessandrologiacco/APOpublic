from typing import List


class University:

    # R1
    def __init__(self, name: str) -> None:
        pass

    def get_name(self) -> str:
        pass

    def set_rector(self, name: str, surname: str) -> None:
        pass

    def get_rector(self) -> str:
        pass

    # R2
    def add_student(self, name: str, surname: str) -> int:
        pass

    def get_student_info(self, student_id: int) -> str:
        pass

    # R3
    def add_course(self, title: str, teacher: str) -> int:
        pass

    def get_course_info(self, course_id: int) -> str:
        pass

    # R4
    def register_to_course(self, student_id: int, course_id: int) -> None:
        pass

    def get_attendees(self, course_id: int) -> str:
        pass

    def get_study_plan(self, student_id: int) -> List[str]:
        pass
