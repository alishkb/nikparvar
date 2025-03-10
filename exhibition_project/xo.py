win_list = {
    1: [[2, 3, 4], [6, 11, 16], [7, 13, 19]],
    2: [[1, 3, 4], [3, 4, 5], [7, 12, 17], [8, 14, 20]],
    3: [[1, 2, 4], [2, 4, 5], [8, 13, 18]],
    4: [[1, 2, 3], [8, 12, 16], [9, 14, 19]],
    5: [[2, 3, 4], [9, 13, 17], [10, 15, 20]],
    6: [[1, 11, 16], [11, 16, 21], [7, 8, 9], [12, 18, 24]],
    7: [[2, 12, 17], [12, 17, 22], [6, 8, 9], [8, 9, 10], [1, 13, 19], [13, 19, 25]],
    8: [[6, 7, 9], [7, 9, 10], [3, 13, 18], [13, 18, 23], [2, 14, 20], [4, 12, 16]],
    9: [[6, 7, 8], [7, 8, 10], [4, 14, 19], [14, 19, 24], [5, 13, 17], [13, 17, 21]],
    10: [[7, 8, 9], [5, 15, 20], [15, 20, 25], [14, 18, 22]],
    11: [[1, 6, 16], [6, 16, 21], [12, 13, 14]],
    12: [[11, 13, 14], [13, 14, 15], [2, 7, 17], [7, 17, 22], [6, 18, 24], [4, 8, 16]],
    13: [[11, 12, 14], [12, 14, 15], [3, 8, 18], [8, 18, 23], [1, 7, 19], [7, 19, 25], [5, 9, 17], [9, 17, 21]],
    14: [[11, 12, 13], [12, 13, 15], [4, 9, 19], [9, 19, 24], [2, 8, 20], [10, 18, 22]],
    15: [[12, 13, 14], [5, 10, 20], [10, 20, 25]],
    16: [[1, 6, 11], [6, 11, 21], [17, 18, 19], [4, 8, 12]],
    17: [[16, 18, 19], [18, 19, 20], [2, 7, 12], [7, 12, 22], [5, 9, 13], [9, 13, 21]],
    18: [[16, 17, 19], [17, 19, 20], [3, 8, 13], [8, 13, 23], [6, 12, 24], [10, 14, 22]],
    19: [[16, 17, 18], [17, 18, 20], [4, 9, 14], [9, 14, 24], [1, 7, 13], [7, 13, 25]],
    20: [[17, 18, 19], [5, 10, 15], [10, 15, 25], [2, 8, 14]],
    21: [[6, 11, 16], [22, 23, 24], [9, 13, 17]],
    22: [[21, 23, 24], [23, 24, 25], [7, 12, 17]],
    23: [[21, 22, 24], [22, 24, 25], [8, 13, 18]],
    24: [[21, 22, 23], [22, 23, 25], [9, 14, 19], [6, 12, 18]],
    25: [[22, 23, 24], [10, 15, 20], [7, 13, 19]],
}


def check_win(plate, position):
    for choice in win_list[position]:
        if plate[position] == plate[choice[0]] == plate[choice[1]] == plate[choice[2]]:
            return True
    return False


def show(plate):
    for i in range(0, 21, 5):
        for j in range(1, 6):
            print(plate[i + j], end='\t')
        print()


plate = {}
for i in range(1, 26):
    plate[i] = i

show(plate)
counter = 1
while True:
    position = int(input('Enter a number: '))
    if 0 < position < 26 and plate[position] == position:
        if counter % 2 == 0:
            player_sign = 'X'
        else:
            player_sign = 'O'
        plate[position] = player_sign
        counter += 1
        show(plate)

        if check_win(plate, position):
            print()
            print('* ' * 23)
            print('* ' * 23)
            print('* ' * 5, '                        ', '* ' * 5)
            print('* ' * 5, f'CONGRATULATION {player_sign} player!', '* ' * 5)
            print('* ' * 5, '                        ', '* ' * 5)
            print('* ' * 23)
            print('* ' * 23)
            break

        if counter > 25:
            print()
            print('* ' * 23)
            print('* ' * 23)
            print('* ' * 5, '                        ', '* ' * 5)
            print('* ' * 5, f'* Game Has Not Winner *', '* ' * 5)
            print('* ' * 5, '                        ', '* ' * 5)
            print('* ' * 23)
            print('* ' * 23)
            break

    else:
        print('*** your number is invalid ***')
        continue

print()
