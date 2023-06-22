# 딕셔너리(04)

## 딕셔너리를 이용해서 5명의 회원을 가입 받고, 전체회원 정보를 출력하는 프로그램

members = {}

n = 1
while n < 6:
    mail = input('메일 입력 : ')
    pw = input('비번 입력 : ')

    # 메일 중복 방지
    if mail in members:
        print('이미 사용중인 메일 계정입니다.')
        continue
    else:
        members[mail] = pw
        n += 1

for key in members.keys():
    print(f'{key} : {members[key]} ')

## 위의 프로그램을 이용해서 특정 회원 계정을 삭제하는 프로그램 만들기

while True:
    delMail = input('삭제할 계정(메일) 입력 : ')

    if delMail in members:
        delPw = input('비번 입력 : ')
        if members[delMail] == delPw:
            del members[delMail]
            print(f'{delMail} 계정 삭제 완료!')
            break
        else:
            print(f'비번 확인 요망!')
    else:
        print('계정 확인 요먕!!')

