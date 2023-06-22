# 딕셔너리(05)

## 파이썬에서 학생 정보를 가장 효율적으로 저장하고 관리할 수 있는 자료구조를 선택해서 컨테이너 자료형으로 만들기
## 리스트_튜플_딕셔너리(선택)

students = {'S21-0001':{'이름':'최성훈',
                        '성구분':'M',
                        '전공':'디자인',
                        '연락처':'010-1234-5678',
                        '메일':'hun@gmail.com',
                        '취미':['농구', '음악']},
            'S21-0002':{'이름':'탁영우',
                                    '성구분':'M',
                                    '전공':'바리스타',
                                    '연락처':'010-5678-9012',
                                    '메일':'yeong@gmail.com',
                                    '취미':['축구']},

            'S21-0003':{'이름':'황진영',
                                    '성구분':'F',
                                    '전공':'음악',
                                    '연락처':'010-9012-3456',
                                    '메일':'jin@gmail.com',
                                    '취미':['수영', '코딩']}}

print(students)

for k1 in students.keys():
    print('-'*40)
    print(f'학생 번호 : {k1}')

    student = students[k1]
    for k2 in student.keys():
        print(f'{k2} : {student[k2]}')

# 특정 정보 조회
studentNo = input('조회 대상 학생 번호 입력 : ')
print(f'{studentNo} : {students[studentNo]}')