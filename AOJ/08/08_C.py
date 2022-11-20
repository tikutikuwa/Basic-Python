count_ls = [0 for i in range(26)]

while (True):
    try:
        str = input().lower()
        for ch in str:
            if (ord("a") <= ord(ch) <= ord("z")):
                count_ls[ord(ch)-ord("a")] += 1
    except EOFError:
        break

for i in range(len(count_ls)):
    print("{0} : {1}".format(chr(i+ord("a")), count_ls[i]))
