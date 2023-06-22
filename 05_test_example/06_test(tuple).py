# 튜플(01)

## 자주 접속하는 웹사이트 비번을 튜플에 저장

# passwds = ('password1234', 'abc123','qwerty','letmein', 'welcome00')
# print(type(passwds))
# print(f'passwds : {passwds}')

## 길동이의 1,2,3학년 성적(scores)은 다음과 같다.
## 졸업할 때 4.0 이상의 학점을 받기위해, 길동이가 받아야하는 4학년 1, 2학기의 최소 학점을 구해보자

scores = ((3.7, 4.2), (2.9, 4.3), (4.1, 4.2))

total = 0
for s1 in scores: # 작은 튜플
    for s2 in s1: # 튜플 개개값
        total += s2 # 튜플 개개값의 합

total = round(total, 1)
avg = round(total / 6, 1)
print(f'3학년 총 학점 : {total}')
print(f'3학년 평균 : {avg}')

grade4TargetScore = round((4.0 * 8 - total), 1)
minScore = round(grade4TargetScore / 2, 1)
print(f'4학년 목표 총 학점 : {grade4TargetScore}')
print(f'4학년 한 학기 최소 학점 : {minScore}')

# 튜플에 추가하기(리스트 변환 > 할당 > 튜플 변환)
scores = list(scores)
scores.append((minScore, minScore))
scores = tuple(scores)
print(f'scores : {scores}')