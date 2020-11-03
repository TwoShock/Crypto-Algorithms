import  string
char2Num = {char:i for i,char in enumerate(string.ascii_lowercase)}
num2Char = {value:key for key, value in char2Num.items()}

def affineCipherEncrypt(msg,a,b):
    output = [(a*char2Num[msg[i]]+b)%26 for i in range(len(msg))]
    return "".join([num2Char[output[i]] for i in range(len(output))])

def affineCipherDecrypt(cipher,a,b):
    aInverse = 1
    for aInverse in range(1,26):
        if((aInverse*a)%26 == 1):
            break
    output = [(aInverse*(char2Num[cipher[i]] - b)) % 26 for i in range(len(cipher))]
    return "".join([num2Char[output[i]] for i in range(len(output))])
def vigenereEncrypt(msg,key):
    extended_key = ""
    for i in range(len(msg)):
        extended_key += key[i%len(key)]
    output = [(char2Num[msg[i]]+char2Num[extended_key[i]]) % 26 for i in range(len(msg))]
    return "".join([num2Char[i] for i in output])

    