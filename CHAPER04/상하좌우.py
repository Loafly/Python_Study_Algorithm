SIZE = int(input())

command = list(input().split())

current_row = 1
current_col = 1

for i in range(len(command)):
    current_command = command[i]

    # 아래
    if current_command == 'D' and current_row < SIZE:
        current_row += 1
    
    # 위
    elif current_command == 'U' and current_row > 1:
        current_row -= 1
    
    # 오른쪽
    elif current_command == 'R' and current_col < SIZE:
        current_col += 1

    # 왼쪽
    elif current_command == 'L' and current_col > 1:
        current_col -= 1
    
print(current_row, current_col)