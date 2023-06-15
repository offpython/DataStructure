# 리스트란?
# 여러 개의 데이터를 나열한 자료 구조

# '[]'를 이용해서 선언하고, 데이터 구분은 ','를 이용한다.
# 숫자, 문자, 논리형 등 모든 기본 데이터를 같이 저장할 수 있다.
student = '홍길동'
print(f'student : {student}')
print(type(student))

students = ['홍길동', '박찬호', '이용규', '박승철', '김지은']
print(f'students : {students}')
print(type(students))

numbers = [10, 20, 30, 40, 50, 60, 70]
print(f'numbers : {numbers}')
print(type(numbers))

strs = [3.14, '십', 20, 'one', '3.141592']
print(f'strs : {strs}')
print(type(strs))

# 실습1
myFamilyNames = ['홍아빠', '홍엄마', '홍길동', '홍동생']
print(myFamilyNames)

todaySchedule = ['10시-업무회의',
                 '12시-친구와 점심약속',
                 '3시-자료정리',
                 '6시-운동',
                 '9시-TV시청']
print(todaySchedule)


