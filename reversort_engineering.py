from typing import Optional, List

found = False

def find_compat_batch_costs(n: int, c: int, batch_costs: List[int] = [], current_pos: int = 1) -> List[List[int]]:
    global found
    if found or (sum(batch_costs) >= c and len(batch_costs) >= n) or (sum(batch_costs) + sum(range(current_pos + 1, n + 1)) < c):
        return []
    if current_pos >= n:
        if sum(batch_costs) != c:
            return []
        else:
            found = True 
            return [batch_costs]
    batch_costs_a = list(batch_costs) + [1]
    last_batch_cost_list_a = find_compat_batch_costs(n, c, batch_costs_a, current_pos + 1)

    batch_costs_b = list(batch_costs) + [current_pos + 1]
    last_batch_cost_list_b = find_compat_batch_costs(n, c, batch_costs_b, current_pos + 1)

    return last_batch_cost_list_a + last_batch_cost_list_b
        
# def find_list(n: int, batch_costs: List[int]) -> List[int]:
#     l = list(range(1, n+1))
#     for i in range(n - 2, -1, -1):
#         sub_list_size = n - 1 - i + 1
#         if sub_list_size in batch_costs:
#             l = l[:i] + l[i:][::-1]
#             batch_costs.remove(sub_list_size)
#         elif 1 in batch_costs:
#             batch_costs.remove(1)
#         else:
#             return
#     if len(batch_costs) == 0:
#         return l

def find_list(n: int, batch_costs: List[int]) -> List[int]:
    l = list(range(1, n+1))
    for i, cost in enumerate(batch_costs):
        if cost > 1:
            l = l[:n-i-2] + l[n-i-2:][::-1]
    return l

def main():
    global found
    t = int(input())
    for i in range(t):
        found = False
        inputs = input().split(' ')
        n = int(inputs[0])
        c = int(inputs[1])
        batch_costs_list = find_compat_batch_costs(n, c)
        # print(batch_costs_list)
        output = 'IMPOSSIBLE'
        for batch_costs in batch_costs_list:
            l = find_list(n, batch_costs)
            if l is not None:
                output = ' '.join([str(item) for item in l])
                break
        print(f'Case #{i+1}:', output)

if __name__ == '__main__':
    main()