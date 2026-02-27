import os
import json
import random

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "id.json")
lettersENN = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','1','2','3','4','5','6','7','8','9','0']


def load_id():
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_id(new_data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(new_data, f, indent=4, ensure_ascii=False)

def id_exists(id_to_check):
    id_data = load_id()
    if "id_taken" in id_data:
        return str(id_to_check) in id_data["id_taken"]
    return False

def gen(symbols):
    gen_save = load_id()
    gen = "none"
    while id_exists(gen):
        gen = "none"
        gen = ''.join(random.choice(lettersENN) for _ in range(symbols))
    gen_save["id_taken"][gen] = 1
    save_id(gen_save)
    return gen