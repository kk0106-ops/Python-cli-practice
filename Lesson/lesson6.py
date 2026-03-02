class Student:
    def __init__(self, name, math, japanese,
                english, science, society):
        self.name = name
        self.math = math
        self.japanese = japanese
        self.english = english
        self.science = science
        self.society = society

    def average_score(self):
        avg = (self.math + self.japanese + self.english + self.science + self.society) / 5
        return avg

student_1 = Student("斉藤そうま", 82, 74, 60, 92, 72)
s1_avg = student_1.average_score()
print(s1_avg)