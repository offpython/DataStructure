# 튜플(04)

## 다음 튜플의 과일 개수에 대해서 오름차순 및 내림차순으로 정렬해보자
fruits = ({'수박':8}, {'포도':13}, {'참외':12}, {'사과':17}, {'자두':19}, {'자몽':15})
fruits = list(fruits) # 튜플 > 리스트 변환

# value값 기준으로 인덱스 비교
cIdx = 0  #기준(현재) 인덱스
nIdx = 1 #비교 인덱스
eIdx = len(fruits) - 1 #끝 인덱스

flag = True
while flag:
    curDic = fruits[cIdx]  # 위치변함없음
    nextDic = fruits[nIdx] # 포도 > 참외 > 사과 > 자두 > 자몽 (비교를위해)

    # value값 뽑기
    curDicCnt = list(curDic.values())[0]
    nextDicCnt = list(nextDic.values())[0]

    # 비교
    if nextDicCnt < curDicCnt: # 자리바꿈 필요   ## 부등호 바꾸면 내림차순
        fruits.insert(cIdx, fruits.pop(nIdx)) # 자르고 넣기
        nIdx = cIdx + 1
        continue

    nIdx += 1 # 자리바꿈 안필요한 경우
    if nIdx > eIdx:
        cIdx += 1
        nIdx = cIdx + 1

        if cIdx == 5:
            flag = False

print(tuple(fruits))