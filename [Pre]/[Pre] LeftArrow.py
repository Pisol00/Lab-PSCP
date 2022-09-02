"""IG: gxmp.a"""


def main(range_arrow, height_arrow):
    """Main function"""
    space = int((height_arrow-1)/2)
    for _ in range(space, -1-space, -1):
        print((" "*abs(_)) + "*"*range_arrow)


main(int(input()), int(input()))
