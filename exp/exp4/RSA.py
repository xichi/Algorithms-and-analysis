def exteuclid(a, b):
    if b == 0:         
        return 1, 0, a     
    else:         
        x, y, q = exteuclid(b, a % b)          
        x, y = y, (x - (a // b) * y)         
        return x, y, q

p = 823
q = 953
n = p * q
Pn = (p-1)*(q-1)

e = int(313)

print("public key: (n: %d, e: %d)" %(n, e))

x, d, r = exteuclid(Pn, e)
if r == 1:
    d = int(d)
    print("private key: (d: %d)" %d)

else:
    print("Multiplicative inverse for\
    the given encryption key does not \
    exist. Choose a different encrytion key ")

# Encryption process
M = 180304
S = (M**e) % n
M1 = (S**d) % n
print('Plaintext:', M)
print('Ciphertext:', S)
print('Decrypted text:', M1)