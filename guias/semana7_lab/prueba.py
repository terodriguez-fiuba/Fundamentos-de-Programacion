a = 256
b = 255+1

r = 257
s = 256+1

print(r is s)       

print(a is b)

# Comprobación de la Caché Global (<= 256)
a = 256
b = 255 + 1
print("256 calculado dinámicamente:", a is b)  # ¡Da TRUE! La caché global lo reconoce.

# Comprobación de que no hay caché para >= 257
p = 257
q = 256 + 1
print("257 calculado dinámicamente:", p is q)  # ¡Da FALSE! El compilador no lo agrupó y no hay caché.
