#!python3

import appex
import ui
import os
import random
import clipboard
import zkpwgen

widget_name = 'ZkpwgenView'

length = 8
letters = True
numbers = True
secure = False


def regen(sender):
    update_view(sender.superview)


def increment_length(sender):
    global length
    length += 1
    update_view(sender.superview)


def decrement_length(sender):
    global length
    if length > 1:
        length -= 1
        update_view(sender.superview)


def set_numbers(sender):
    global numbers, secure
    numbers = sender.value
    if not numbers:
        secure = False
    update_view(sender.superview)


def set_letters(sender):
    global letters, secure
    letters = sender.value
    if not letters:
        secure = False
    update_view(sender.superview)


def set_secure(sender):
    global secure, letters, numbers
    secure = sender.value
    if secure:
        letters = True
        numbers = True
    update_view(sender.superview)


def init_view():
    v = ui.load_view(widget_name)
    update_view(v)
    return v


def generate(length):
    hira = secure or bool(random.getrandbits(1))
    kata = secure or not hira
    upper = secure or bool(random.getrandbits(1))
    lower = secure or not upper
    return zkpwgen.generate(length,
                            hira=hira,
                            kata=kata,
                            num=secure or not numbers,
                            upper=upper,
                            lower=lower)


def update_view(view):
    view['NumbersSwitch'].value = numbers
    view['LettersSwitch'].value = letters
    view['SecureSwitch'].value = secure
    view['LengthDownButton'].enabled = length > 1
    view['LengthValueLabel'].text = str(length)
    pw = generate(length)
    view['PasswordField'].text = pw
    clipboard.set(pw)


def main():
    v = appex.get_widget_view()
    if v is not None and v.name == widget_name:
        return
    appex.set_widget_view(init_view())


if __name__ == '__main__':
    main()
