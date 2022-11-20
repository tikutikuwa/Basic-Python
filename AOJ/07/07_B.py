while (True):
    pat, target = map(int, input().split())
    if (pat == 0 and target == 0):
        break

    count = 0

    # 重複なしのため最大値はpat-2,pat-1,patになるように調整
    for i in range(1, pat-1):
        if (i > target):
            break

        for j in range(i+1, pat):
            if (i+j > target):
                break

            for k in range(j+1, pat+1):
                if (i+j+k == target):
                    count += 1
                    break

    print(count)
