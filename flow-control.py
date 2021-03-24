#Flow control practice

user1 = 'Yuri'
pass1 = 'Password'

username = input('Enter your username: ')
userage = input('Confirm your age: ')
if username == user1:
    print('Hello ' + user1 + ', Welcome back!')
    temppass = input('Enter your password: ')
    if temppass == pass1:
        print('Access granted')
    else:
        print('Access Denied')
elif int(userage) < 18:
    print('18+ Only')
else:
    print('User not found.')
