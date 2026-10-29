def binary(n):
    return format(n & 0xFF, '08b')


# a) +46 + (+29)
a = 46
b = 29

print("a) +46 + (+29)")
print("+46 =", binary(a))
print("+29 =", binary(b))

result = a + b
print("Binary result =", binary(result))
print("Decimal result =", result)

# Check overflow
if result < -128 or result > 127:
    print("Arithmetic Overflow: Yes")
else:
    print("Arithmetic Overflow: No")

print()

# b) (-48) - (-23)
a = -48
b = -23

print("b) (-48) - (-23)")
print("-48 =", binary(a))
print("-23 =", binary(b))

# Subtraction: a - b
result = a - b
print("Binary result =", binary(result))
print("Decimal result =", result)

# Check overflow
if result < -128 or result > 127:
    print("Arithmetic Overflow: Yes")
else:
    print("Arithmetic Overflow: No")

