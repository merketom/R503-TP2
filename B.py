# Bob connaît la clé publique (n, e)
n = 61 * 53  # même n
e = 17       # reçu de Alice

# Message de Bob (un entier < n)
M = 65

# Chiffrement
C = pow(M, e, n)

print("Message clair M =", M)
print("Message chiffré C =", C)
