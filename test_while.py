flag = True
number = 1

while flag:
    if number <=3:
        answer = input('为什么超级英雄都穿紧身衣')
        if answer == '救人要紧':
            flag = False
            print('恭喜你答对了')
        else:
            print('回答错误')
    else:
        print('次数用完了')
        break

    print(f'这是你的第{number}次回答')
    number += 1
            
