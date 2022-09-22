heigh = int(input())
length = int(input())
count_pieces = heigh * length
pieces_taken = input()

while pieces_taken != "STOP":
    cur_piece = int(pieces_taken)
    count_pieces -= cur_piece
    if count_pieces <= 0:
        break
    pieces_taken = input()

if pieces_taken  == "STOP":
    print(f'{count_pieces} pieces are left.')

if count_pieces <= 0:
    pieces_left = abs(count_pieces)
    print(f'No more cake left! You need {pieces_left} pieces more.')

