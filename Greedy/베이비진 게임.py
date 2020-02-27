def is_run(input_list):
    for j in range(0, len(input_list)-2):
        if input_list[j] >= 1 and input_list[j+1] >= 1 and input_list[j+2] >= 1:
            return True
    return False

def is_triplet(input_list):
    for k in range(len(input_list)):
        if input_list[k] >= 3:
            return True
    return False

for i in range(int(input())):

    num_list = map(int, input().split())
    player1 = [0]*10
    player2 = [0]*10
    winner = ''
    for idx, num in enumerate(num_list):
        if (idx+1) % 2:
            player1[num] += 1
            if idx >= 2:
                if is_run(player1) or is_triplet(player1):
                    winner = 'player1'
                    break
        else:
            player2[num] += 1
            if idx >= 2:
                if is_run(player2) or is_triplet(player2):
                    winner = 'player2'
                    break

    if winner == 'player1':
        print(f'#{i+1} 1')
    elif winner == 'player2':
        print(f'#{i+1} 2')
    else:
        print(f'#{i+1} 0')
