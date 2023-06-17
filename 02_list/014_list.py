# 리스트 아이템 정렬
## sort() 함수를 이용하면 아이템을 정렬할 수 있다.
names = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은']
print('names : {}'.format(names))

# 오름차순
names.sort()
print('names : {}'.format(names))

# 내림차순
names.sort(reverse=True)
print('names : {}'.format(names))

## 숫자형으로도 정렬 가능핟
numbers = [2, 50, 0.12, 1, 9, 17, 35, 100, 3.14]
print('numbers : {}'.format(numbers))

numbers.sort()
print('numbers : {}'.format(numbers))

numbers.sort(reverse=True)
print('numbers : {}'.format(numbers))

# 실습1
## 최고/최저 점수를 삭제한 후 총점과 평균 출력
scores = [9.5, 8.9, 9.2, 9.8, 8.8, 9.0]
print('scores : {}'.format(scores))

scores.sort()
print('scores : {}'.format(scores))
scores.pop(0)
scores.pop(len(scores) - 1)
print('scores : {}'.format(scores))

sum = 0
avg = 0
for score in scores:
    sum += score

avg = sum / len(scores)

print('총점 : %.2f' % sum)
print('평균 : %.2f' % avg)