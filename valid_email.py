import re
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

n=int(input('enter num:'))
print(n)
guess_count=0
while guess_count < n:
    valid_email=input('')
    guess_count+=1
    if (re.search(regex,valid_email)):

        print(valid_email)

