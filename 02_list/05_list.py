# # 리스트와 for문_2
# # for문을 이용한 조회
#
# # for문과 if문을 이용해서 과락 과목 출력하기
# minScore = 60
# scores = [
#     ['국어', 58],
#     ['영어', 77],
#     ['수학', 89],
#     ['과학', 58],
#     ['국사', 50]]
#
# for item in scores:
#     if item[1] < 60:
#         print(f'과락 과목: {item[0]} (점수: {item[1]})')
#
# for subject, score in scores:
#     if score < minScore:
#         print(f'과락한 과목: {subject}, 점수: {score}')
#
# for subject, score in scores:
#     if score >= minScore:
#         continue
#     print(f'과락인 과목: {subject} - 점수: {score}')
#
# # 실습1
# # 사용자가 점수를 입력하면 과락 과목과 점수를 출력하는 프로그램을 만들어보자
# minscore = 60
#
# korScore = int(input('국어 점수 : '))
# engScore = int(input('영어 점수 : '))
# matScore = int(input('수학 점수 : '))
# sciScore = int(input('과학 점수 : '))
# hisScore = int(input('역사 점수 : '))
#
# scores = [
#     ['국어', korScore],
#     ['영어', engScore],
#     ['수학', matScore],
#     ['과학', sciScore],
#     ['역사', hisScore]]
#
# for subject, score in scores:
#     if score < minscore:
#         print('과락 과목 : {} -> 점수 : {}'.format(subject, score))
#
# 실습2
## 학급 학생 수가 가장 작은 학급과 가장 많은 학급을 출력
studentsCnts = [
    [1, 18],
    [2, 19],
    [3, 23],
    [4, 21],
    [5, 20],
    [6, 22],
    [7, 17],
]

minClssNo = 0
maxClassNo = 0

minCnt = 0
maxCnt = 0

for classNo, cnt in studentsCnts:
    if minCnt == 0 or minCnt > cnt:
        minClssNo = classNo
        minCnt = cnt

    if maxCnt < cnt:
        maxClassNo = classNo
        maxCnt = cnt

print('학생 수가 가장 적은 학급(학생수) : {}학급 {}명'.format(minClssNo, minCnt))
print('학생 수가 가장 많은 학급(학생수) : {}학급 {}명'.format(maxClassNo, maxCnt))
