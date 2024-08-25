A = {1, 2, 3, 4, 5}
B = {2, 5}

print(f"El conjunto A: {A}\nEl conjunto B: {B}")
print(f"A es un superconjunto de B (issuperset)? {A.issuperset(B)}")
print(f"A es un superconjunto de B (>=)? {A.issuperset(B)}")

B = {1, 2, 3, 4, 5}
print(f"El conjunto A: {A}\nEl conjunto B: {B}")
print(f"A es un superconjunto de B (>)? {A > B}")
