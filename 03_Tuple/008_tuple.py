# 튜플 아이템 정렬
## 튜플은 수정이 불가하기 떄문에 리스트로 변환 -> 정렬 -> 튜플 변환

## sorted() 함수를 이용하면 튜플도 정렬할 수 있다.
## -> sorted()는 리스트 자료형을 반환함
names = ('홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은')
print('names: {}'.format(names))
print('type : {}'.format(type(names)))

sortedNames = sorted(names)
print('names: {}'.format(sortedNames))
print('type : {}'.format(type(sortedNames)))

# 실습1
## 튜플을 이용한 점수표에서 최저/최고 점수를 삭제한 후 총점과 평균 출력
scores = (9.5, 8.9, 9.2, 9.8, 8.8, 9.0)
print('scores : {}'.format(scores))
print('type(scores): {}'.format(type(scores)))

sortedScores = sorted(scores)
print('type(scores): {}'.format(type(sortedScores)))

sortedScores.sort()
print('scores : {}'.format(sortedScores))
sortedScores.pop(0)
sortedScores.pop(len(sortedScores) - 1)

sortedScores = tuple(sortedScores)
print('type(scores): {}'.format(type(sortedScores)))
print('scores : {}'.format(sortedScores))

sum = 0
avg = 0
for score in sortedScores:
    sum += score

avg = sum / len(sortedScores)

print('총점 : %.2f' %sum)
print('평균 : %.2f' %avg)
