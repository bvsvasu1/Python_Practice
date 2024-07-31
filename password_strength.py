def strength(password):
    length_chk = False
    if (len(password)>=8):
        length_chk = True
    
    digits_chk = False
    uppercase_chk =False
    for i in password:
        if i.isdigit():
            digits_chk = True
        if i.isupper():
            uppercase_chk = True
    
    if digits_chk and uppercase_chk and length_chk:
        print("Strong Password")
    else:
        print("Weak Password")
        
password = input("Enter password: ")
strength("password")