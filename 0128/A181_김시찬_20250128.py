num1 = int(input())
num2 = int(input())

third = num1 * (num2 % 10)
fourth = num1 * ((num2 // 10) % 10)
fifth = num1 * (num2 // 100)

sixth = num1 * num2

print(third)
print(fourth)
print(fifth)
print(sixth)