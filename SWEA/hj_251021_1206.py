T = 10
for test_case in range(1, T+1):
    N = int(input())

    B = list(map(int, input().split()))

    cnt = 0

    if N < 5:
        print(f"#{test_case} {cnt}")
        continue

    for i in range(2, N-2):
        if B[i] == 0:
            continue
        else:
            prev_1 = B[i-1]
            prev_2 = B[i-2]
            next_1 = B[i+1]
            next_2 = B[i+2]
            now = B[i]
            if now < next_1 or now < next_2 or now < prev_1 or now < prev_2:
                continue
            else:
                cnt += now - max(prev_1, prev_2, next_1, next_2)
    
    print(f"#{test_case} {cnt}")
            


