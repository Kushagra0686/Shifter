"""CEASER CIPHER PROGRAM FOR DECRYPTION AND ENCRYPTION OF MESSAGES----BY KUSHAGRA VERMA
REQUIRED MODULES -- PyperClip , string & xclip->(on linux platforms)"""
# Importing Modules
import pyperclip as pc
import string
#
# Required Parameters
print("*" * 100)
print('''\033[1;32;40m                                                  
  .--.--.      ,---,                            ___                          
 /  /    '.  ,--.' |       ,--,      .--.,    ,--.'|_                        
|  :  /`. /  |  |  :     ,--.'|    ,--.'  \   |  | :,'               __  ,-. 
;  |  |--`   :  :  :     |  |,     |  | /\/   :  : ' :             ,' ,'/ /| 
|  :  ;_     :  |  |,--. `--'_     :  : :   .;__,'  /      ,---.   '  | |' | 
 \  \    `.  |  :  '   | ,' ,'|    :  | |-, |  |   |      /     \  |  |   ,' 
  `----.   \ |  |   /' : '  | |    |  : :/| :__,'| :     /    /  | '  :  /   
  __ \  \  | '  :  | | | |  | :    |  |  .'   '  : |__  .    ' / | |  | '    
 /  /`--'  / |  |  ' | : '  : |__  '  : '     |  | '.'| '   ;   /| ;  : |    
'--'.     /  |  :  :_:,' |  | '.'| |  | |     ;  :    ; '   |  / | |  , ;    
  `--'---'   |  | ,'     ;  :    ; |  : \     |  ,   /  |   :    |  ---'     
             `--''       |  ,   /  |  |,'      ---`-'    \   \  /            
                          ---`-'   `--'                   `----'                                                                                 
---BY KUSHAGRA VERMA ---
\033[m
''')
# Ceaser Function
def ceaser_cipher(message,key,mode):
    # Declaring all possible symbols allowed to function
    symbols = string.ascii_letters+string.punctuation
    # Storage for Result
    translated = ''
    # Accessing Symbols in Message
    for letter in message:
        if letter in symbols:
            letter_index = symbols.find(letter)     # Gets Index of Letter in Symbol
            # Perform Encryption or Decryption Based On Mode
            if mode == 'e':
                translated_index = letter_index + key
            elif mode == 'd':
                translated_index = letter_index - key
            else:
                print("-- Usage : ( 'e' for Encryption / 'd' for Decryption ) --")
                exit()
            # Perform Wraparound For Preventing Ceaser Index Out Of Range
            if translated_index >= len(symbols):
                translated_index = translated_index - len(symbols)
            elif translated_index < 0:
                translated_index = translated_index + len(symbols)
            # Result Compilation
            translated = translated + symbols[translated_index]
            #
        # If The Letter is Miscellaneous and Not in Symbol set
        else:
            translated = translated + letter
    # Output The Translated Message
    if mode == 'e':
        print()
        print("\033[1;32;40mEncryption Successful !!\033[m")
        print()
        print(f"Encrypted Message : \033[1;35;40m{translated}\033[m ")
    elif mode == 'd':
        print()
        print("\033[1;33;40mDecryption Successful !!\033[m")
        print()
        print(f"Decrypted Message :\033[1;35;40m {translated}\033[m")
    #
    print()
    copy = input(r"Do You Want To Copy The Result To Clipboard ('y' for yes / 'n' for 'no') :").lower()
    if copy == 'y':
        pc.copy(translated)
        print("\033[1;36;40mCopied To Clipboard Successfully ...\033[m")
        print("*" * 100)
    else :
        print("*" * 100)
        exit()
    #
print("*" * 100)


# MAIN

message = input("Enter The Message : ")
print()
mode = input("Enter The Mode ( 'e' for Encryption / 'd' for Decryption ) : ").lower()
print()
if mode == 'e':
    print("\033[1;36;40m------------ENCRYPTION MODE SELECTED------------\033[m")
    print()
    key = int(input("Enter The Key For (Encryption) : "))
elif mode == 'd':
    print("\033[1;36;40m------------DECRYPTION MODE SELECTED------------\033[m")
    print()
    key = int(input("Enter The Key For (Decryption) : "))
ceaser_cipher(message,key,mode)

# END OF PROGRAM








