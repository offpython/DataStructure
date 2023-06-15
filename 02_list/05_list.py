# 리스트와 for문_2
# for문을 이용한 조회

# for문과 if문을 이용해서 과락 과목 출력하기
minScore = 60
scores = [
    ['국어', 58],
    ['영어', 77],
    ['수학', 89],
    ['과학', 58],
    ['국사', 50]]

for item in scores:
    if item[1] < 60:
        print(f'과락 과목: {item[0]} (점수: {item[1]})')

for subject, score in scores:
    if score < minScore:
        print(f'과락한 과목: {subject}, 점수: {score}')

for subject, score in scores:
    if score >= minScore:
        continue
    print(f'과락인 과목: {subject} - 점수: {score}')


