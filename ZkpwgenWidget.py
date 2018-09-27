#!python3

import appex
import ui
import os
import random
import clipboard
import zkpwgen

widget_name = 'ZkpwgenView'

length_max = 20

length_percent = 8 / length_max
letters = True
numbers = True
secure = False


def regen(sender):
    update_view(sender.superview)


def set_length(sender):
    length_percent = sender.value
    update_view(sender.superview)


def set_numbers(sender):
    numbers = sender.value
    if not numbers:
        secure = False
    update_view(sender.superview)


def set_letters(sender):
    letters = sender.value
    if not letters:
        secure = False
    update_view(sender.superview)


def set_secure(sender):
    secure = sender.value
    update_view(sender.superview)


def init_view():
    v = ui.load_view(widget_name)
    update_view(v)
    return v


def generate():
    hira = secure or bool(random.getrandbits(1))
    kata = secure or not hira
    upper = secure or bool(random.getrandbits(1))
    lower = secure or not upper
    return zkpwgen.generate(pw_len,
                            hira=hira,
                            kata=kata,
                            num=secure or not numbers,
                            upper=upper,
                            lower=lower)


def update_view(view):
    view['NumbersSwitch'].value = numbers
    view['LettersSwitch'].value = letters
    view['SecureSwitch'].value = secure
    view['LengthSlider'].value = length_percent
    pw_len = round(length_percent * length_max)
    view['LengthValueLabel'].value = str(pw_len)
    pw = generate()
    view['PasswordField'].value = pw
    clipboard.set(pw)


def main():
    v = appex.get_widget_view()
    if v is not None and v.name == widget_name:
        return
    appex.set_widget_view(init_view())


if __name__ == '__main__':
    main()
