scores = {"数学": 82, "国語": 74, "英語": 60, "理科": 92, "社会": 70}
## diff = scores["理科"] - scores["社会"]
## print(f"{diff}点")

scores_values = list(scores.values())
avg_score = sum(scores_values) / len(scores_values)
print(f"{avg_score}点")