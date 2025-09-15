import math

# Données connues du hacker
n = 61 * 53
e = 17
C = 2790  # exemple chiffré envoyé par Bob

# Facteur n pour retrouver p et q (attaque brute force)
def factoriser(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i, n // i
    return None

p, q = factoriser(n)
phi = (p - 1) * (q - 1)

# Calcul de l'inverse de e mod phi
def euclide_etendu(a, b):
    if b == 0:
        return (1, 0)
    u, v = euclide_etendu(b, a % b)
    return (v, u - (a // b) * v)

def inverse_mod(e, phi):
    u, v = euclide_etendu(e, phi)
    return u % phi

d = inverse_mod(e, phi)

# Déchiffrement par le hacker
M = pow(C, d, n)

print("Hacker retrouve p, q =", p, q)
print("Il calcule d =", d)
print("Message retrouvé M =", M)
