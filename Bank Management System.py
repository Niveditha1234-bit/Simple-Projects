import pandas as pd
from datetime import datetime
import random
pb = {
    'Type': [],
    'Amount': [],
    'Current Balance': []
}
mpin = '0012'
bal = 100000
print('---***Bank of Baroda***----')
t = 1
while t <= 3:
    otp = random.randint(1000, 9999)
    print(f'Enter the OTP sent to your registered mobile: {otp}')
    upin = input('Enter the OTP: ')
    if upin == str(otp):
        print('Validation is successful')
        print('Account holder name: Niveditha P')
        while True:
            print('1-Deposit\t2-Withdraw\t3-Balance Enquiry\t4-PassBook\t0-Exit')
            ch = input('Enter your choice: ')
            if ch == '0':
                break
            elif ch == '1':
                ty = 'Deposit'
                amt = int(input('Enter the amount to deposit: '))
                bal += amt
                print('Your new balance is', bal)
                pb['Type'].append(ty)
                pb['Amount'].append(amt)
                pb['Current Balance'].append(bal)
                now = datetime.now()
                print('Deposited on', now)
            elif ch == '2':
                ty = 'Withdraw'
                amt = int(input('Enter the amount to withdraw: '))
                if amt > bal:
                    print('Insufficient balance')
                else:
                    bal -= amt
                    print('Your new balance is', bal)
                    pb['Type'].append(ty)
                    pb['Amount'].append(amt)
                    pb['Current Balance'].append(bal)
                    now = datetime.now()
                    print('Withdrawn on', now)
            elif ch == '3':
                print('Your current balance is', bal)
            elif ch == '4':
                passbook = pd.DataFrame(pb)
                print(passbook)
                now = datetime.now()
                print('Passbook printed on', now)
            else:
                print('Invalid choice, please select a valid option.')
                
        break
    else:
        if t == 3:
            print('Sorry, account blocked')
        else:
            print('Invalid OTP, try again')
        t += 1