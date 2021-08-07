# https://programmers.co.kr/learn/courses/30/lessons/42891?language=python3

def solution(food_times, k):
    i = 0
    j = 0
    length = len(food_times)
    while True:
        a = food_times[j%length]
        if i == k-1:
            break
        if a == 0:
           continue
        else: i += 1
        j += 1
        answer = j%length

    return answer

