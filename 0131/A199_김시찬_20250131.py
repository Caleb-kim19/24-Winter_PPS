N = int(input())
    
for i in range(N):
    line = " ".join(["*"] * N)
    if i % 2 == 1:
        line = " " + line
    print(line)