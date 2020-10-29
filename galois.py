from utils import circularLeftShift,stringXOR
import functools

def multiplyByX(p1):
    if p1[0] == '0':
        return circularLeftShift(p1,1)
    elif p1[0] == '1':
        p2 = p1
        p2 = '0' + p2[1:]
        p2 = circularLeftShift(p2,1)
        return stringXOR(p2,'00011011')

def multiplyByXPowerN(p1,n):
    answer = p1
    for i in range(n):
        answer = multiplyByX(answer)
    return answer

def multiply(p1,p2):
    """
    multiplies two  polynomials in galois field 2^8
    """
    out = []
    i = len(p1)-1 
    for b in p2:
        if(b == '1'):
            out.append(multiplyByXPowerN(p1,i))
        i-=1
    answer = functools.reduce(lambda a,b:stringXOR(a,b),out)
    return answer
    