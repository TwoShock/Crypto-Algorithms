import logging
logging.basicConfig(filename = './log/euclid.log',format='%(message)s', level=logging.INFO)
def extended_euclid(m:int,b:int)->int:
   a1,a2,a3 = (1,0,m) 
   b1,b2,b3 =(0,1,b)
   q = '-'
   logging.info(f'Q | A1 | A2 | A3 | B1 | B2 | B3')
   while(True):
        logging.info(f'{q} | {a1} | {a2} | {a3} | {b1} | {b2} | {b3}')
        q = int(a3/b3)
        t1,t2,t3 = (a1-q*b1,a2-q*b2, a3-q*b3)
        a1,a2,a3 = (b1,b2,b3)
        b1,b2, b3 = (t1,t2, t3)
        if b3 == 0:
            logging.info(f'{q} | {a1} | {a2} | {a3} | {b1} | {b2} | {b3}')
            return "No Inverse"
        if b3 == 1:
            logging.info(f'{q} | {a1} | {a2} | {a3} | {b1} | {b2} | {b3}')
            return b2
def gcd(x, y): 
   while(y): 
       logging.info(f'GCD({x},{y}) = GCD({y},{x%y})')
       x, y = y, x % y 
   return x 
gcd(24,12)