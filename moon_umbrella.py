from typing import List

def cal_cost(x: int, y: int, text: str) -> int:
    if text == 'CJ':
        return x
    elif text == 'JC':
        return y
    return 0

def fill_space(mural: List[str], x: int, y: int):
    i = 0
    cost = 0
    last_no_space = ''
    filling = False
    for char in mural:
        if char != '?':
            if filling:
                c_cost = cal_cost(x, y, last_no_space + 'C') + cal_cost(x, y, 'C' + char)
                j_cost = cal_cost(x, y, last_no_space + 'J') + cal_cost(x, y, 'J' + char)
                cost += min(c_cost, j_cost)
            else:
                cost += cal_cost(x, y, last_no_space + char)
            filling = False
            last_no_space = char
        else:
            filling = True
    return cost

def main():
    x_list = []
    y_list = []
    murals = []
    t = int(input())
    for _ in range(t):
        line = input().split(' ')
        x_list.append(int(line[0]))
        y_list.append(int(line[1]))
        murals.append(list(line[2]))
    for i in range(t):
        x = x_list[i]
        y = y_list[i]
        mural = murals[i]
        cost = fill_space(mural, x, y)
        print(f'Case #{i+1}: {cost}')

if __name__ == '__main__':
    main()