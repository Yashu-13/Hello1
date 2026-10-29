number = 0b11010101

# a) Rotate Right without Carry (ROR)
print("a) Rotate Right without Carry (ROR)")
print("Original number:", format(number, "08b"))

for i in range(3):
    lsb = number & 1
    number = (number >> 1) | (lsb << 7)
    print("Step", i + 1, ":", format(number, "08b"))

print("Final ROR result:", format(number, "08b"))

print()

# b) Rotate Right with Carry (RCR)
number = 0b11010101
carry = 0

print("b) Rotate Right with Carry (RCR)")
print("Original number:", format(number, "08b"))
print("Initial carry:", carry)

for i in range(3):
    lsb = number & 1
    number = (number >> 1) | (carry << 7)
    carry = lsb
    print("Step", i + 1, ":", format(number, "08b"),
          "Carry:", carry)

print("Final RCR result:", format(number, "08b"))
print("Final carry:", carry)

