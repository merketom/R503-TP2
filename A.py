import random
import math

# Fonction pgcd
def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Algorithme d'Euclide étendu pour trouver l'inverse
def euclide_etendu(a, b):
    if b == 0:
        return (1, 0)
    u, v = euclide_etendu(b, a % b)
    return (v, u - (a // b) * v)

def inverse_mod(e, phi):
    u, v = euclide_etendu(e, phi)
    return u % phi

# -------------------------
# 1. Alice choisit deux nombres premiers
p = 61
q = 53
n = p * q
phi = (p - 1) * (q - 1)

# 2. Alice choisit e premier avec phi
e = 17  # choisi arbitrairement
assert pgcd(e, phi) == 1

# 3. Calcul de d
d = inverse_mod(e, phi)

print("Clé publique (n, e) =", (n, e))
print("Clé privée (n, d)   =", (n, d))

# -------------------------
# Déchiffrement
def dechiffrer(C, d, n):
    return pow(C, d, n)

# Exemple : si Alice reçoit C=...
# M = dechiffrer(C, d, n)
