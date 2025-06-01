import json
from random import choice


def gen_person():
    key_tel = ''
    name = ''
    tel = ''

    letters = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'e', 'k', 'l', 'm', 'n']
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(key_tel) != 10:
        key_tel += choice(num)

    while len(name) != 7:
        name += choice(letters)

    while len(tel) != 10:
        tel += choice(num)

    person = {key_tel: {'name': name, 'tel': tel}}
    return person


def write_json(person_dict):
    try:
        data = json.load(open('persons.json'))
    except FileNotFoundError:
        data = {}

    data.update(person_dict)
    with open('persons.json', 'w') as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(gen_person())
