
# Create password variable
password = '8xly@DrvW8&'


# Asking for data from costumer
answer = input('What is your password?')
attempt =  0

#Cheking password
while answer != password:
    attempt  += 1
    if attempt == 3:
        print('Sytem is closed. Please connect with Support team.')
        break
    print('Wrong paaswod. Please try again.')
    answer = input('What is your password?')


if attempt == password:
    print('Login was succesful')
