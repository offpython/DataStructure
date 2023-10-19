# enumerate

sports = ['농구', '축구', '야구', '마라톤', '테니스']
for i in range(len(sports)):
    print(f'{i} : {sports[i]}')
for idx, value in enumerate(sports):
    print(f'{idx} : {value}')

str = 'Hello Future'
for idx, value in enumerate(str):
    print(f'{idx} : {value}')

sports = ['농구', '수구', '축구', '마라톤', '테니스']
favoriteSport = input('가장 좋아하는 스포츠 입력 : ')

bestSportIdx = 0
for idx, value in enumerate(sports):
    if value == favoriteSport:
        bestSportIdx = idx + 1

print(f'{favoriteSport}는 {bestSportIdx}번 째에 있습니다.')

message = input('메세지 입력 : ')
cnt = 0
for idx, value in enumerate(message):
    if value == ' ':
        cnt += 1
print(f'공백 갯수 : {cnt}')