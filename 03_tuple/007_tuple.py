# 리스트와 튜플
## 튜플은 리스트와 달리 아이템 추가/변경/삭제가 불가하다.
## 튜플은 선언 시 괄호 생략이 가능하다.
students = '홍길동', '박찬호', '이용규', '강호동'
print('students: {}'.format(students))
print('type : {}'.format(type(students)))

# 리스트와 튜플은 자료형 변환이 가능하다.
students = ['홍길동', '박찬호', '이용규', '강호동']

students = tuple(students)
print('type(students): {}'.format(type(students)))

students = list(students)
print('type(students): {}'.format(type(students)))

# 실습1
## 튜플을 이용한 점수표에서 최저/최고 점수를 삭제한 후 총점과 평균 출력
scores = (9.5, 8.9, 9.2, 9.8, 8.8, 9.0)
print('scores : {}'.format(scores))
print('type(scores): {}'.format(type(scores)))

scores = list(scores)
print('type(scores): {}'.format(type(scores)))

scores.sort()
print('scores : {}'.format(scores))
scores.pop(0)
scores.pop(len(scores) - 1)

scores = tuple(scores)
print('type(scores): {}'.format(type(scores)))
print('scores : {}'.format(scores))

sum = 0
avg = 0
for score in scores:
    sum += score

avg = sum / len(scores)

print('총점 : %.2f' %sum)
print('평균 : %.2f' %avg)
