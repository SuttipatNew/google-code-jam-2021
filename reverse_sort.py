from typing import List

def calculate_cost(l: List[int]) -> int:
    cost = 0
    for i in range(len(l) - 1):
        min_value = min(l[i:])
        j = l[i:].index(min_value) + i
        l = l[:i] + l[i:j+1][::-1] + l[j+1:]
        cost += j - i + 1
        print(l)
        print(cost)
    return cost

def main():
    test_cases_count = int(input())
    l_list = []
    for _ in range(test_cases_count):
        _ = int(input())
        l_list.append([int(item) for item in input().split(' ')])
    for it, l in enumerate(l_list, start=1):
        cost = calculate_cost(l)
        print(f'Case #{it}: {cost}')

if __name__ == '__main__':
    main()