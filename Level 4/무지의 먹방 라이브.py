import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return (-1)
    
    heap = []
    for i in range(len(food_times)):
        heapq.heappush(heap, (food_times[i], i + 1))
    
    previous = 0
    sum_value = 0
    length = len(food_times)
    while sum_value + ((heap[0][0] - previous) * length) <= k:
        now = heapq.heappop(heap)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now
    
    result = sorted(heap, key = lambda x : x[1])
    return (result[(k - sum_value) % length][1])