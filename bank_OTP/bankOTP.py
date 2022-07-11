
import random

def generate_OTP():
    bankOTPStr = ""

    # since the first digit cannot be 0
    num = str(random.randint(1,9))
    bankOTPStr += num

    # generating the rest of the digits
    for i in range(3):
        num = str(random.randint(0,9))
        bankOTPStr += num
    bankOTP = int(bankOTPStr)
    return bankOTP

bankOTP = generate_OTP()
print("This is your OTP:",bankOTP)

numTries = 1

while numTries < 4: 
    userInput = int(input("Enter your OTP: "))
    if userInput == bankOTP:
        print("User authenticated")
        break
    else:
        print("Wrong OTP. Tries left:", 3 - numTries)
    numTries += 1

