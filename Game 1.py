import random
while True:
    a =None
    option=['rock','paper','scissors']
    while a not in option:
        a=input('enter your choice:').lower()
    b=random.choice(option)
    print('player choice:',a)
    print('computer choice:',b)
    if a==b:
        print("Tie")
    elif a=='rock' and b=='paper':
        print('computer wins')
    elif a=='paper' and b=='Rock':
        print('you win')
    elif a=='paper' and b=='scissors':
        print('computer wins')
    elif a=='rock' and b=='scissors':
        print('you win')
    elif a=='scissors' and b=='rock':
        print('computer wins')
    play_again=input('Do you want to play again (yes/no)?:' ).lower()
    if play_again=='no':
        break
print('SEEE YA')