#! /usr/bin/python3

import os


def load_data(f):
    print('load_data called')
    filename = get_full_pathname(f)

    if os.path.exists(filename):
        print(filename)
        with open(filename) as fin:
            for line in fin.readlines():
                print('............' + line.rstrip())
        return

    print('file not found')
    return


def get_full_pathname(f):
    filename = os.path.abspath(f)
    return filename


def main():
    f = 'well.txt'
    load_data(f)
    return


if __name__ == '__main__':
    main()
