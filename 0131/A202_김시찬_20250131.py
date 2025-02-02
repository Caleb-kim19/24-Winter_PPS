N = int(input())
expression = input().strip()
values = [int(input()) for _ in range(N)]

stack = []
for char in expression:
    if 'A' <= char <= 'Z':
        stack.append(values[ord(char) - ord('A')])
    else:
        b = stack.pop()
        a = stack.pop()
        if char == '+':
            stack.append(a + b)
        elif char == '-':
            stack.append(a - b)
        elif char == '*':
            stack.append(a * b)
        elif char == '/':
            stack.append(a / b)

result = stack[0]
print(f"{result:.2f}")