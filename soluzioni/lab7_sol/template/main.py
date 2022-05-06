from university import *

def main():
    # R1
    print("-------- R1 --------")
    uni = University("PoliTo")
    uni.set_rector("Guido", "Saracco")
    print(uni.get_name())       # PoliTo
    print(uni.get_rector())     # Guido Saracco

    # R2
    print("-------- R2 --------")
    sid_1 = uni.add_student("Mario", "Rossi")
    sid_2 = uni.add_student("Enrico", "Bianchi")
    print(sid_1, sid_2)                 # 10000 10001
    print(uni.get_student_info(sid_1))  # 10000 Mario Rossi
    print(uni.get_student_info(sid_2))  # 10001 Enrico Bianchi

    # R3
    print("-------- R3 --------")
    cid_1 = uni.add_course("Algoritimi e Programmazione a Oggetti", "Filippo Ganino")
    cid_2 = uni.add_course("Informatica", "Filippo Gandino")
    print(cid_1, cid_2)                 # 10 11
    print(uni.get_course_info(cid_1))   # 10,Algoritimi e Programmazione a Oggetti,Filippo Ganino
    print(uni.get_course_info(cid_2))   # 11,Informatica,Filippo Gandino

    # R4
    print("-------- R4 --------")
    uni.register_to_course(sid_1, cid_1)
    uni.register_to_course(sid_2, cid_1)
    uni.register_to_course(sid_1, cid_2)

    print("Participanti corso {}:".format(cid_1))       # Participanti corso 10:
    print(uni.get_attendees(cid_1))                     # 10000 Mario Rossi
                                                        # 10001 Enrico Bianchi

    print("Participanti corso {}:".format(cid_2))       # Participanti corso 11:
    print(uni.get_attendees(cid_2))                     # 10000 Mario Rossi

    print("Piano studio studente {}:".format(sid_1))    # Piano studio studente 10000:
    print(uni.get_study_plan(sid_1))                    # ['10,Algoritimi e Programmazione a Oggetti,Filippo Ganino', '11,Informatica,Filippo Gandino']

    print("Piano studio studente {}:".format(sid_2))    # Piano studio studente 10001:
    print(uni.get_study_plan(sid_2))                    # ['10,Algoritimi e Programmazione a Oggetti,Filippo Ganino']


if __name__ == "__main__":
    main()




