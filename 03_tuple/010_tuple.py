# 튜플과 for문(2)
## for문과 if문을 이용해서 과락 과목 출력하기
minSocre = 60
scores = (
    ('국어', 58),
    ('영어', 77),
    ('수학', 89),
    ('과학', 99),
    ('국사', 50),
)

for item in scores:
    if item[1] < minSocre:
        print('과락 과목 : {} (점수 : {})'.format(item[0], item[1]))

for subject, score in scores:
    if score < minSocre:
        print('과락 : {} , 점수 : {}'.format(subject, score))

for subject, score in scores:
    if score >= minSocre:
        continue
    print('과락 : {} -> 점수 : {}'.format(subject, score))

# 실습1
minScore = 60

korScore = int(input('국어 점수 : '))
engScore = int(input('영어 점수 : '))
matScore = int(input('수학 점수 : '))
sciScore = int(input('과학 점수 : '))
hisScore = int(input('역사 점수 : '))

scores = (
    ('국어', korScore),
    ('영어', engScore),
    ('수학', matScore),
    ('과학', sciScore),
    ('역사', hisScore),
)

for subject, score in scores:
    if score < minScore:
        print('과락 : {} (점수 : {})'.format(subject, score))

# 실습2
studentCnts = (
    (1, 18),
    (2, 19),
    (3, 23),
    (4, 21),
    (5, 20),
    (6, 22),
    (7, 17),
)

minClssNo = 0; maxClassNo = 0
minCnt = 0; maxCnt = 0

for classNo, cnt in studentCnts:
    if minCnt == 0 or minCnt > cnt:
        minClssNo = classNo
        minCnt = cnt

    if maxCnt < cnt:
        maxClassNo = classNo
        maxCnt = cnt

print('학생 수가 가장 적은 학급 수 : {} (학생수 :{})'.format(minClssNo, minCnt))
print('학생 수가 가장 많은 학급 수 : {} (학생수 :{})'.format(maxClassNo, maxCnt))