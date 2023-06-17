# 딕셔너리 삭제
## del과 key를 이용한 삭제
memInfo = {'이름': '박경진', '메일': 'jin@naver.com', '학년': 3,'취미': ['요리', '여행']}
print(f'memInfo : {memInfo}')

del memInfo['메일']
print(f'memInfo : {memInfo}')

del memInfo['취미']
print(f'memInfo : {memInfo}')

## pop()와 key를 이용한 item 삭제
memInfo = {'이름': '박경진', '메일': 'jin@naver.com', '학년': 3,'취미': ['요리', '여행']}
print(f'memInfo : {memInfo}')

returnValue = memInfo.pop('이름')
print(f'memInfo : {memInfo}')
print(f'returnValue : {returnValue}')

returnValue = memInfo.pop('취미')
print(f'memInfo : {memInfo}')
print(f'returnValue : {returnValue}')

# 실습1
scores = {'score1':8.9, 'score2':8.1, 'score3':8.5, 'score3':8.9, 'score4':9.8, 'score':8.8}

minScore = 10; minScoreKey = ' '
maxScore = 0; minScoreKey = ' '

for key in scores.keys():
    if scores[key] < minScore:
        minScore = scores[key]
        minScoreKey = key

    if scores[key] > maxScore:
        maxScore = scores[key]
        maxScoreKey = key

print(f'minScore : {minScore}')
print(f'minScoreKey : {minScoreKey}')
print(f'maxScore : {maxScore}')
print(f'maxScoreKey : {maxScoreKey}')

del scores[minScore7Key]
del scores[maxScoreKey]

print(f'scores : {scores}')