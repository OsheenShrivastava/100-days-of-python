
# Subscripting
print("Hello"[0])

# Strings
print("123" + "345")

# Integers
print(123 + 345)

# Large Integers
print(123456789)

# Floats
print(3.14159)

# Boolean
print(True)
print(False)

# Type Error
# len(12345)

# Type Checking
print(type("Hello"))
print(type(123))
print(type(3.14))
print(type(True))

# Type Conversion
name_of_the_user = input("Enter your name ")
length_of_name = len(name_of_the_user)

print(type("Number of letters in your name: "))
print(type(length_of_name))

print("Number of characters in your name: " + str(length_of_name))

# Mathematical Operations - PEMDAS - () ** * / + -
print(123 + 456)
print(7 - 3)
print(2 * 3)
print(5 / 3)
print(5 // 3)
print(2 ** 3)

print(3 * 3 + 3 / 3 - 3)

# round function
bmi = 84 / 1.65 ** 2
print(bmi)

print(int(bmi))
print(round(bmi))
print(round(bmi, 2))

# f-strings
score = 0

score += 1
print(score)

print(f"Your score is {score}")