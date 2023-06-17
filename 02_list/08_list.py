# # enumerate() 함수
# ## enumerate()함수를 이용하면 아이템을 열거할 수 있다.
#
# sports = ['농구', '수구', '축구', '마라톤', '테니스']
#
# # 이전 방식
# for i in range(len(sports)):
#     print('{} : {}'.format(i, sports[i]))
#
# # enumerate() 함수 사용
# for idx, value in enumerate(sports):
#     print('{} : {}'.format(idx, value))
#
# # enumerate()는 문자열에서도 적용 가능
# str = "hello python"
#
# for idx, value in enumerate(str):
#     print('{} : {}'.format(idx, value))
#
# 실습1
## 가장 좋아하는 스포츠가 몇 번째에 있는지 출력하는 프로그램

sports = ['농구', '수구', '축구', '마라톤', '테니스']
favoriteSports = input('가장 좋아하는 스포츠 입력 : ')
bestSportsIndex = 0

for idx, value in enumerate(sports):
    if value == favoriteSports:
        bestSportsIndex = idx + 1

print('{}는 {}번째에 있습니다.'.format(favoriteSports, bestSportsIndex))

# 실습2
message = input('메세지 입력 : ')
cnt = 0

for idx, value in enumerate(message):
    if value == ' ':
       cnt += 1

print('공백 갯수 : {}'.format(cnt))