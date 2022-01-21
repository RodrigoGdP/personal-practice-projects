#the first two variables contain lists with character that can make a password stronger
numbers = ['1','2','3','4','5','6','7','8','9','0']
SpecChar = ['!','@','#','$','¨','&','*','(',')','+','-','_','=',' ','{','}','[',']','?',':',';',',','.','<','>','/','|']

#the use is prompted into choosing a password
password = input("choose a password: ")

#this loop checks if the password is too short
while len(password) <= 5:
    print("\n*your password is too short*")
    password = input("\nchoose a bigger password: ")

#this function chooses how strong the password is and returns a message
def CheckPass(password):
    check = 0
    check2 = 0
    for i in password:
        if i in numbers:
            check += 1
        if i in SpecChar:
            check2 += 1

    if check and check2 > 0:
        result = '\nyour password is very strong'
    elif check or check2 > 0:
        result = '\nyour password is strong'
    else:
        result = '\n*your password is too weak*'
    return result

#the CheckPass function is run
print(CheckPass(password))

#this loop prompts the user into entering another password in case the first one is too weak
while CheckPass(password) == '\nthis is a weak password':
    password = input('\nchoose another one, and use numbers and special characters: ')
    print(CheckPass(password))

#if the password is strong or very strong, the user is prompted into confirming their password
passcon = input("\nconfirm the password: ")

#this loop checks if the password and the confirmation match
while passcon != password:
    print("\n*passwords don't match*")
    passcon = input("\nconfirm the password: ")

#final message displayed in case the password is at least strong and matches the confirmation
print('\npassword confirmed')


