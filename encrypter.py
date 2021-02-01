import string


codex = list(string.ascii_uppercase + string.ascii_lowercase + string.punctuation + ' ')

password = input("Enter a password you want to encrypt: ")

encryption = list(password)

newpassword = []

##go through each letter and if even codex entry -- new letter is 5 indexes up
## if odd codex entry -- new letter is 5 indexes down
for i in encryption:
    entry = codex.index(i)
    
    if(entry % 2 == 0):
        if( (entry + 5) > len(codex) ):
            entry = 5 - ((len(codex)-1) - entry)
        else:
            entry += 5
        newpassword.append(codex[entry])

    else:
        if(entry - 5 < 0):
            entry = (len(codex)-1) - (5 - entry)
        else:
            entry -= 5
        newpassword.append(codex[entry])    
   
password = ""
for j in newpassword:
    password += j

print(password)
        