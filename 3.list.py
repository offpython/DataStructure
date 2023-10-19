# # 리스트 특정 위치에 아이템 추가
# students = ['홍길동', '박찬호', '이용규', '박승철', '김지은']
# students.insert(3, '강호동')
# print(students)
#
# words = ['I', 'a', 'Boy.']
# for word in words:
#     print(word, end = '')
# print()
#
# words.insert(1, 'am')
# for word in words:
#     print(f'{word} ', end = '')
# print()
#
# numbers = [1, 3, 6, 11, 45, 54, 62, 74, 85]
# inputNum = int(input('숫자 입력 : '))
# insertIdx = 0
#
# for idx, number in enumerate(numbers):
#     print(idx, number)
#     if insertIdx == 0 and inputNum < number:
#         insertIdx = idx
#
# numbers.insert(insertIdx, inputNum)
# print(numbers)
#
# # 리스트 아이템 삭제
# students = ['홍길동', '박찬호', '이용규', '박승철', '김지은', '강호동']
# students.pop()
# print(students)
# students.pop(2)
# print(students)
#
# rValue = students.pop()
# print(rValue)
#
# playerScore = [9.5, 8.9, 9.2, 9.8, 8.8, 9.0]
# print(playerScore)
# minScore = 0; maxScore = 0
# minScoreIdx = 0; maxScoreIdx = 0
#
# for idx, score in enumerate(playerScore):
#     if idx == 0 or minScore > score:
#         minScoreIdx = idx
#         minScore = score
# playerScore.pop(minScoreIdx)
#
# for idx, score in enumerate(playerScore):
#     if maxScore < score:
#         maxScoreIdx = idx
#         maxScore = score
# playerScore.pop(maxScoreIdx)
# print(playerScore)
#
# # 리스트 특정 아이템 삭제
# students = ['홍길동', '박찬호', '이용규', '박승철', '김지은', '강호동']
# students.remove('강호동')
# print(students)
#
# students = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은', '강호동']
# print(students)
# while '강호동' in students:
#     students.remove('강호동')
# print(students)
#
# myList = ['마케팅 회의', '회의록 정리', '점심 약속', '월간 업무 보고', '치과 방문', '마트 장보기']
# print(f'일정: {myList}')
# removeItem = input('삭제 일정 입력 : ')
# myList.remove(removeItem)
# print(f'일정: {myList}')
#
# subjects = ['국어', '영어', '수학', '과학', '국사', '수학']
# print(subjects)
#
# removeSubject = input('삭제 과목명 입력 : ')
# while removeSubject in subjects:
#     subjects.remove(removeSubject)
# print(subjects)

# 리스트 연결
group1 = ['홍길동', '박찬호', '이용규']
group2 = ['강호동', '박승철', '김지은']
group1.extend(group2)
print(f'{group1}')
print(f'{group2}')

result = group1 + group2
print(result)
print(f'{group1}')
print(f'{group2}')

myNum = [1, 3, 5, 6, 7]
friendNum = [2, 3, 5, 8, 10]
addList = myNum + friendNum
print(addList)

result = []
for number in addList:
    if number not in result:
        result.append(number)
print(result)

# 리스트 아이템 정렬
students = ['홍길동', '박찬호', '이용규', '박승철', '김지은', '강호동']
print(students)
students.sort()
print(students)
students.sort(reverse=True)
print(students)

numbers = [2, 50, 4, 0.12, 3.14, 100]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

playerScores = [9.5, 8.9, 9.2, 9.8, 8.8, 9.0]
print(playerScores)

playerScores.sort()
print(playerScores)

playerScores.pop(0)
playerScores.pop(len(playerScores)-1)
print(playerScores)

sum = 0
avg = 0
for score in playerScores:
    sum += score
avg = sum / len(playerScores)
print('sum : %.2f' % sum)
print('avg : %.2f' % avg)

# 리스트 아이템 순서 뒤집기
students = ['홍길동', '박찬호', '이용규', '박승철', '김지은', '강호동']
students.reverse()
print(students)

numbers = [9.5, 8.9, 9.2, 9.8, 8.8, 9.0]
numbers.reverse()
print(numbers)

secret = '27156231'
secretList = []
solvedList = ''

for cha in secret:
    secretList.append(int(cha))

print(secretList)
secretList.reverse()
print(secretList)

val = secretList[0]*secretList[1]
secretList.insert(2, val)

val = secretList[3]*secretList[4]
secretList.insert(5, val)

val = secretList[6]*secretList[7]
secretList.insert(8, val)

val = secretList[6]*secretList[7]
secretList.insert(8, val)

val = secretList[9]*secretList[10]
secretList.insert(11, val)

print(secretList)

# 리스트 슬라이스
students = ['홍길동', '박찬호', '이용규', '박승철', '김지은', '강호동']
print(students)
print(students[2:])
print(students[:4])
print(students[:-2])
print(students[4:-1])
print(students[-5:-2])

str = 'abcdefghijklmnopqrstuvwxyz'
print(str)
print(str[2:])
print(str[:4])
print(str[:-2])
print(str[4:-1])
print(str[-5:-2])

numbers = [2, 50, 0.12, 1, 9, 7, 17, 35, 100, 3.14]
print('numbers: {}'.format(numbers[2:-2]))
print('numbers: {}'.format(numbers[2:-2:2]))
print('numbers: {}'.format(numbers[:-2:2]))
print('numbers: {}'.format(numbers[::2]))

students = ['홍길동', '박찬호', '이용규', '박승철', '김지은', '강호동']
print(students)
students[1:4] = ['park', 'lee', 'ppark']
print(students)

students = ['홍길동', '박찬호', '이용규', '박승철', '김지은', '강호동']
print(students)
students[1:4] = ['park chanho', 'lee younggyu']
print(students)

students = ['홍길동', '박찬호', '이용규', '박승철', '김지은', '강호동']
print('students: {}'.format(students))
print('students: {}'.format(students[slice(2, 4)]))
print('students: {}'.format(students[slice(4)]))
print('students: {}'.format(students[slice(2, len(students))]))
print('students: {}'.format(students[slice(2, len(students)-2)]))
print('students: {}'.format(students[slice(len(students)-5, len(students)-2)]))