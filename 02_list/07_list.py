# # 리스트와 while문_2
#
# # while문과 if문을 이용해서 과락 과목 출력하기
# minScore = 60
# scores = [
#     ['국어', 58],
#     ['영어', 77],
#     ['수학', 89],
#     ['과학', 99],
#     ['역사', 50],
# ]
#
# n = 0
# while n < len(scores):
#     if scores[n][1] >= 60:
#         n += 1
#         continue
#
#     print('과락 과목 : {} (점수 : {}점) '.format(scores[n][0], scores[n][1]))
#     n += 1
#
# # 실습1
# ## while문을 이용해서 점수를 입력하면 과락 과목과 점수를 출력하는 프로그램
# minScore = 60
#
# korScore = int(input('국어 : '))
# engScore = int(input('영어 : '))
# matScore = int(input('수학 : '))
# sciScore = int(input('과학 : '))
# hisScore = int(input('역사 : '))
#
# scores = [
#     ['국어', korScore],
#     ['영어', engScore],
#     ['수학', matScore],
#     ['과학', sciScore],
#     ['역사', hisScore],
# ]
#
# n = 0
# while n < len(scores):
#     if scores[n][1] < minScore:
#         print(f'과락 과목 : {scores[n][0]}, 점수 : {scores[n][1]}')
#
#     n += 1

# 실습2
studentCnts = [[1, 18], [2, 19],[3, 23],[4, 21],[5, 20],[6, 22],[7, 17]]

minClassNo = 0; maxClassNo = 0;
minCnt = 0; maxCnt = 0;

n = 0
while n < len(studentCnts):
    if minCnt == 0 or minCnt > studentCnts[n][1]:
        minClassNo = studentCnts[n][0]
        minCnt = studentCnts[n][1]

    if  maxCnt < studentCnts[n][1]:
        maxClassNo = studentCnts[n][0]
        maxCnt = studentCnts[n][1]

    n += 1

print('학생 수가 가장 적은 반(학생수) : {}반({}명)'.format(minClassNo, minCnt))
print('학생 수가 가장 많은 반(학생수) : {}반({}명)'.format(maxClassNo, maxCnt))

