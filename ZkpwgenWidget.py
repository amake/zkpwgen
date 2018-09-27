#!python3

from collections import namedtuple
import appex
import ui
import os
import random
import clipboard
import zkpwgen

widget_name = 'ZkpwgenView'

ViewModel = namedtuple('ViewModel', ['length', 'letters', 'numbers', 'secure'])

current_model = ViewModel(8, True, True, False)


def copy_model():
    return ViewModel(**current_model._asdict())


def regen(sender):
    update_view(sender.superview)


def increment_length(sender):
    model = copy_model()
    model.length += 1
    update_view(sender.superview, model)


def decrement_length(sender):
    model = copy_model()
    model.length -= 1
    update_view(sender.superview, model)


def set_numbers(sender):
    model = copy_model()
    model.numbers = sender.value
    if not model.numbers:
        model.secure = False
    update_view(sender.superview, model)


def set_letters(sender):
    model = copy_model()
    model.letters = sender.value
    if not model.letters:
        model.secure = False
    update_view(sender.superview, model)


def set_secure(sender):
    model = copy_model()
    model.secure = sender.value
    if model.secure:
        model.letters = True
        model.numbers = True
    update_view(sender.superview, model)


def init_view():
    v = ui.load_view(widget_name)
    update_view(v, current_model)
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


def can_generate(length):
    try:
        generate(length)
        return True
    except:
        return False


def update_view(view, model):
    try:
        pw = generate(model.length)
        view['NumbersSwitch'].value = model.numbers
        view['LettersSwitch'].value = model.letters
        view['SecureSwitch'].value = model.secure
        view['LengthDownButton'].enabled = can_generate(model.length - 1)
        view['LengthValueLabel'].text = str(model.length)
        view['PasswordField'].text = pw
        clipboard.set(pw)
        global current_model
        current_model = model
    except:
        pass


def main():
    v = appex.get_widget_view()
    if v is not None and v.name == widget_name:
        return
    appex.set_widget_view(init_view())


if __name__ == '__main__':
    main()
