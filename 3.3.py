scores = []
score = 0


while score != -1:
    score = int(input("輸入學生成績 (-1 to end): "))
    if score != -1:
        scores.append(score)


num_students = len(scores)
passing_students = len([s for s in scores if s >= 60])
failing_students = num_students - passing_students
average_score = sum(scores) / num_students if num_students > 0 else 0


print(f'全班人數: {num_students}')
print(f'及格人數: {passing_students}')
print(f'不及格人數: {failing_students}')
print(f'全班平均值: {average_score:.2f}')