# 리스트의 아이템 삭제
## pop() 함수를 이용하면 마지막 인덱스에 해당하는 아이템을 사용할 수 있다.
names = ['홍길동', '박찬호', '이용규', '박승철', '김지은', '강호동']
print('names : {}'.format(names))
print(f'length of names : {len(names)}')
print(f'length of names : {len(names) - 1}')

# pop(n) 함수를 n인덱스에 해당하는 아이템을 삭제할 수 있다.
names.pop(2)
print(f'names : {names}')
print(f'length of names : {len(names)}')
print(f'length of names : {len(names) - 1}')

# rValue 이용하면 삭제한 데이터 반환해서 사용할 수 있다.
rValue = names.pop()
print(f'rValue : {rValue}')
print(names)

# 실습1
scores = [9.5, 8.9, 9.2, 9.8, 8.8, 9.0]
print(f'playerScores : {scores}')

minScore = 0; maxScore = 0
minSScoreInx = 0; maxScordIdx = 0

for idx, score in enumerate(scores):
    if idx == 0 or minScore > score:
        minScoreInx = idx
        minScore = score

print('minScore : {}, minScoreIdx : {}'.format(minScore, minScoreInx))
scores.pop(minScoreInx)

for idx, score in enumerate(scores):
    if maxScore < score:
        maxScoreInx = idx
        maxScore = score

print('maxScore : {}, maxScoreIdx : {}'.format(maxScore, maxScoreInx))
scores.pop(maxScoreInx)

print(f'playerScores : {scores}')
