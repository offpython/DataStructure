# # 딕셔너리의 유용한 기능
# ## in, not in : 키 존재 유/무 판단
# memInfo = {'이름': '박경진', '메일': 'jin@naver.com', '학년': 3,'취미': ['요리', '여행']}
# print('이름' in memInfo)
# print('이름' not in memInfo)
# print('name' in memInfo)
# print('name' not in memInfo)
#
# ## len() : 딕셔너리 길이를 알 수 있다.
# print(f'len(memInfo) : {len(memInfo)}')
#
# ## clear() : 모든 아이템을 삭제한다.
# memInfo.clear()
# print(f'len(memInfo) : {memInfo}')

# 실습1
## 개인정보에 '연락처'와 '주민번호'가 있다면 삭제하는 코드 작성
myInfo = {'이름': '박경진', '연락처': '010-1234-5678', '나이': 30,'주민번호': '12345-67890'}

deleteItems = ['연락처', '주민번호']

for item in deleteItems:
    if (item in deleteItems):
        del myInfo[item]

print(f'myInfo : {myInfo}')