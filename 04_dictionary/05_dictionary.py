# # key()와 values()
# ## 전체 키와 값을 조회할 수 있다.
#
# memInfo = {'이름': '박경진', '메일': 'jin@naver.com', '학년': 3,'취미': ['요리', '여행']}
#
# ks = memInfo.keys()
# print(f'ks : {ks}')
# print(f'ks type : {type(ks)}')
#
# vs = memInfo.values()
# print(f'ks : {vs}')
# print(f'ks type : {type(vs)}')
#
# items = memInfo.items()
# print(f'ks : {items}')
# print(f'ks type : {type(items)}')
#
# ## 리스트로 변환하기
# ks = list(ks)
# print(f'ks : {ks}')
# print(f'ks type : {type(ks)}')
#
# vs = list(ks)
# print(f'ks : {vs}')
# print(f'ks type : {type(vs)}')
#
# items = list(items)
# print(f'ks : {items}')
# print(f'ks type : {type(items)}')
#
# ## for문을 이용한 조회
# for key in ks:
#     print(f'key : {key}')
#
# for idx, key in enumerate(ks):
#     print(f'idx, key : {idx}, {key}')
#
# for value in vs:
#     print(f'key : {value}')
#
# for idx, value in enumerate(vs):
#     print(f'idx, key : {idx}, {value}')
#
# for item in items:
#     print(f'key : {items}')
#
# for idx, items in enumerate(items):
#     print(f'idx, key : {idx}, {items}')
#
# ## for문을 이용한 조회
# for key in memInfo.keys():
#     print(f'{key} : {memInfo[key]}')

# 실습1
## 점수가 60 미만이면 'F(재시험)'으로 값 변경하는 코드를 keys()이용해서 작성
scores = {'kor':88, 'eng':55, 'mat':85, 'sci':57, 'his':82}
print(f'scores : {scores}')

minScore = 60
fStr = 'F(재시험)'
fDic = {}

for key in scores:
    if scores[key] < minScore:
        scores[key] = fStr
        fDic[key] = fStr # 과락(키/값) 따로 모음

print(f'scores : {scores}')
print(f'fDic : {fDic}')