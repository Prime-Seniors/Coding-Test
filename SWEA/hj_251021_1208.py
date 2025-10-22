T = 10

for test_case in range(1, T+1):
    D = int(input())
    B = list(map(int, input().split()))

    for i in range(D):
        B.sort()
        B[0] += 1
        B[-1] -= 1

    B.sort()

    print(f"#{test_case} {B[-1]-B[0]}")
        