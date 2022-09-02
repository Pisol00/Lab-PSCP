"""IG: gxmp.a"""


def main(l_bread, r_bread):
    """Main function"""
    hamburger = (l_bread+r_bread)*2
    print("|"*l_bread + hamburger*"*" + "|"*r_bread)


main(int(input()), int(input()))
