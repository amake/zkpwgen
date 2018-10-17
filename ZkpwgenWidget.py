#!python3

from collections import namedtuple
import appex
import ui
import os
import json
import random
import clipboard
import zkpwgen

widget_name = 'ZkpwgenView'

ViewModel = namedtuple('ViewModel', ['length', 'letters', 'numbers', 'secure'])

current_model = ViewModel(8, True, True, False)

settings_file = '.ZkpwgenWidget.json'


def copy_model(model=None, **kwargs):
    if model is None:
        model = current_model
    curr_vals = model._asdict()
    curr_vals.update(kwargs)
    return ViewModel(**curr_vals)


try:
    with open(settings_file) as f:
        persist_vals = json.load(f)
        current_model = copy_model(**persist_vals)
except:
    pass


class TextFieldDelegate(object):
    def textfield_should_begin_editing(self):
        return False


def regen(sender):
    update_view(sender.superview, current_model)


def increment_length(sender):
    model = copy_model(length=current_model.length + 1)
    update_view(sender.superview, model)


def decrement_length(sender):
    model = copy_model(length=current_model.length - 1)
    update_view(sender.superview, model)


def set_numbers(sender):
    vals = {'numbers': sender.value}
    if not sender.value:
        vals['secure'] = False
    model = copy_model(**vals)
    update_view(sender.superview, model)


def set_letters(sender):
    vals = {'letters': sender.value}
    if not sender.value:
        vals['secure'] = False
    model = copy_model(**vals)
    update_view(sender.superview, model)


def set_secure(sender):
    vals = {'secure': sender.value}
    if sender.value:
        vals['letters'] = True
        vals['numbers'] = True
    model = copy_model(**vals)
    update_view(sender.superview, model)


def init_view():
    v = ui.load_view(widget_name)
    v['PasswordField'].delegate = TextFieldDelegate
    update_view(v, current_model)
    return v


def generate(model):
    return zkpwgen.generate_simple(model.length,
                                   letters=model.letters,
                                   numerals=model.numbers,
                                   secure=model.secure)


def can_generate(model):
    try:
        generate(model)
        return True
    except:
        return False


def update_view(view, model):
    try:
        pw = generate(model)
        view['NumbersSwitch'].value = model.numbers
        view['LettersSwitch'].value = model.letters
        view['SecureSwitch'].value = model.secure
        view['LengthDownButton'].enabled = can_generate(
            copy_model(model, length=model.length - 1))
        view['LengthValueLabel'].text = str(model.length)
        view['PasswordField'].text = pw
        clipboard.set(pw)
        persist_model(model)
    except:
        update_view(view, current_model)


def persist_model(model):
    global current_model
    current_model = model
    with open(settings_file, 'w') as f:
        json.dump(model._asdict(), f)


def main():
    v = appex.get_widget_view()
    if v is not None and v.name == widget_name:
        return
    appex.set_widget_view(init_view())


if __name__ == '__main__':
    main()
