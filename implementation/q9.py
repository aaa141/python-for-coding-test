# https://programmers.co.kr/learn/courses/30/lessons/60057
def solution(s):
    result = []
    for i in range(1, len(s) // 2):
        aa = {0}
        for k in range(0, len(s) - 1, i):
            aa.add(s[k:k + i])
        result.append(len(aa))

    slice = result.index(min(result)) + 1

    ss = []
    count = 0
    for i in range(len // slice):
        if s[i:i + slice] in ss:
            count += 1
        else:
            ss.clear()
            ss.append(s[i:i + slice])

    answer = len(s) - slice * count + count

    return answer
