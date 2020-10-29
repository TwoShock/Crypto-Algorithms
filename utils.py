
def convertHexToBinary(hexStr):
    return bin(int(hexStr,16))[2:]
    
def convertBinaryToHex(binary):
    return str(hex(int(binary,2)))

def circularLeftShift(bits,n):
    bits = list(bits)
    return "".join(bits[n::] + bits[:n:])

def ciruclarRightShift(bits,n):
    bits = list(bits)
    return "".join(bits[n:len(bits):] + bits[0:n:])

def stringXOR(s1:str,s2:str)->str:
    """
    performs and xor operation on two binary strings
    returns xor result
    """
    assert(len(s1) == len(s2))
    return "".join(["0" if s1[i] == s2[i] else "1" for i in range(len(s1))])