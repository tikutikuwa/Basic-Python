while (True):
    mid, fin, re = map(int, input().split())
    if (mid == -1 and fin == -1 and re == -1):
        break

    score = mid+fin

    if (mid == -1 or fin == -1):
        grade = 'F'

    elif (score >= 80):
        grade = 'A'

    elif (65 <= score < 80):
        grade = 'B'

    elif (50 <= score < 65):
        grade = 'C'

    elif (30 <= score < 50):
        if (re >= 50):
            grade = 'C'
        else:
            grade = 'D'

    else:
        grade = 'F'

        print(grade)
