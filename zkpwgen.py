# -*- coding: utf-8; -*-
from __future__ import print_function
import shutil
import random
from argparse import ArgumentParser

hiragana = range(0x3041, 0x308f)
katakana = range(0x30a1, 0x30f3)
numbers = range(0xff10, 0xff19)
letters_upper = range(0xff21, 0xff31)
letters_lower = range(0xff41, 0xff5a)

blacklist = u'ゐゑヰヱ'


def choose(char_type):
    while True:
        i = random.choice(char_type)
        try:
            c = unichr(i)
        except NameError:
            c = chr(i)
        if c not in blacklist:
            return c


def maybe():
    return random.randint(0, 9) < 3


def generate(length, hira=True, kata=True, num=True, upper=True, lower=True):
    accum = []
    while True:
        if hira:
            accum.append(choose(hiragana))
        if len(accum) >= length:
            break
        if kata:
            accum.append(choose(katakana))
        if len(accum) >= length:
            break
        if num and maybe():
            accum.append(choose(numbers))
        if len(accum) >= length:
            break
        if upper and maybe():
            accum.append(choose(letters_upper))
        if len(accum) >= length:
            break
        if lower and maybe():
            accum.append(choose(letters_lower))
        if len(accum) >= length:
            break
    return ''.join(accum)


def main():
    parser = ArgumentParser(
        description='Generate random passwords of full-width Japanese characters')
    parser.add_argument('--secure', '-s', action='store_true',
                        help='generate completely random passwords')
    parser.add_argument('--one-column', '-1', action='store_true',
                        help="don't print the generated passwords in columns")
    parser.add_argument('--no-numerals', '-0', action='store_true',
                        help="don't include numbers in the password")
    parser.add_argument('--no-letters', '-L', action='store_true',
                        help="don't include Roman alphabet characters in the password")
    parser.add_argument('length', nargs='?', type=int,
                        default=8, help='the length of the password')
    parser.add_argument('count', nargs='?', type=int,
                        default=-1, help='the number of passwords to output')
    args = parser.parse_args()

    try:
        term_cols, _ = shutil.get_terminal_size((80, 20))
    except AttributeError:
        term_cols = 80
    num_cols = 1 if args.one_column else int(term_cols / (args.length * 2 + 1))
    num_pw = (args.count if args.count != -1 else
              1 if args.one_column else num_cols * 20)
    for n in range(num_pw):
        hira = args.secure or bool(random.getrandbits(1))
        upper = args.secure or (
            not args.no_letters and bool(random.getrandbits(1)))
        lower = args.secure or (not args.no_letters and not upper)
        pw = generate(args.length,
                      hira=hira,
                      kata=args.secure or not hira,
                      num=args.secure or not args.no_numerals,
                      upper=upper,
                      lower=lower)
        if n % num_cols == num_cols - 1 or n == num_pw - 1:
            print(pw, end='\n')
        else:
            print(pw, end=' ')


if __name__ == '__main__':
    main()
