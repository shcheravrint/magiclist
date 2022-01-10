
from MagicList import MagicList, Person


def main():
    magic_list = MagicList(Person)
    tt = magic_list[0]
    tt = magic_list[1]
    magic_list[2].age = 5
    print(magic_list[2])

main()