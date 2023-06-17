# # 딕셔너리 추가
# ## '딕셔너리이름[키]=값'형대로 아이템을 추가한다.
# myInfo = {}
#
# myInfo['이름'] = '박경진'
# myInfo['전공'] = 'computer'
# myInfo['메일'] = 'jin@naver.com'
# myInfo['학년'] = 3
# myInfo['주소'] = '대한민국 서울'
# myInfo['취미'] = ['요리', '여행']
# print(myInfo)
#
# myInfo['메일'] = 'jin@gmail.com'
# print(myInfo)
#
# # 실습1
# students = {}
#
# students['name'] = input('이름 입력 :')
# students['grade'] = input('학년 입력 :')
# students['address'] = input('주소 입력 : ')
# students['addr'] = input('취미 입력 : ')
# print(f'students : {students}')

# 실습2
factorialDic = {}

for i in range(11):
    if i == 0:
        factorialDic[i] = 1
    else:
        for j in range(1, (i+1)):
            factorialDic[i] = factorialDic[j-1] * j

print(f'factorialDic : {factorialDic}')

