rank_pat = 13
suit_pat = 4

cards = [[False for i in range(rank_pat)] for j in range(suit_pat)]
suit_ls = ["S","H","C","D"]

deck = int(input())

for i in range(deck):
    suit,rank = input().split()
    rank = int(rank)
    cards[suit_ls.index(suit)][rank-1] = True

for i in range(suit_pat):
    for j in range(rank_pat):
        if cards[i][j] == False:
            print(suit_ls[i],j+1)
