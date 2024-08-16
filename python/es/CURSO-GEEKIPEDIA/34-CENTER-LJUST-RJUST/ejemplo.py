string = "menu"

print("\n\tMetodos con espacios:")
print(f"\t{string.center(10)}")
print(f"\t{string.ljust(10)}")
print(f"\t{string.rjust(10)}")

print("\n\tMetodos sin espacios:")
print(f"\t{string.center(10, '-')}")
print(f"\t{string.ljust(10, '-')}")
print(f"\t{string.rjust(10, '-')}")