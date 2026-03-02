class schoolReport:
    def __init__(self, student_name,
                 math_score, jp_score, en_score):
        self.student_name = student_name
        self.math_score = math_score
        self.jp_score = jp_score
        self.en_score = en_score

    def calc_avg_score(self):
        avg_score = (self.math_score
                     + self.jp_score
                     + self.en_score) / 3
        return avg_score

sr_a = schoolReport("田中 A", 100, 30, 50)
avg_a = sr_a.calc_avg_score()
print(f"Aさんの3教科の平均点：{avg_a}")

sr_b = schoolReport("鈴木 B", 20, 59, 20)
avg_b = sr_b.calc_avg_score()
print(f"Bさんの3教科の平均点：{avg_b}")

sr_c = schoolReport("斎藤 C", 19, 22, 19)
avg_c = sr_c.calc_avg_score()
print(f"Cさんの3教科の平均点：{avg_c}")