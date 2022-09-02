"""IG: gxmp.a"""


def main(picking, score, ace):
    """Main function"""
    for _ in range(picking):
        card = input()
        if card == "J" or card == "Q" or card == "K":
            score += 10
        elif card == "A":
            score += 11
            ace += 1
        elif int(card) > 1 and int(card) < 11:
            score += int(card)

    while score > 21 and ace > 0:
        score -= 10
        ace -= 1
    print(score)


main(int(input()), 0, 0)
