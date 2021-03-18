import re
value=[]
passwords = [i for i in input ("Please enter passwords: ").split(",")]

for password in passwords:
    if len(password)<8 or len(password)>12:
        continue
    else:
        pass

    if not re.search("[a-z]",password):
        continue
    elif not re.search("[A-Z]", password):
        continue
    elif not re.search([1-9], password):
        continue   
    elif not re.search("[#$@]", password):
        continue
    else:
        pass
    value.append(password)
print(",".join(value))