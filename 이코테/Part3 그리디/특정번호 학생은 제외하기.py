scores = [90, 85, 77, 65, 97]
cheating_student_list = {2, 4}

for i in range(5):
    if i + 1 in cheating_student_list:
        continue
    if scores[i] >= 85:
        print(i + 1, '번 학생은 합격입니다.')